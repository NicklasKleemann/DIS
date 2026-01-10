import argparse
import collections
import math
import os
import re
import sys
from multiprocessing import Pool, cpu_count
from typing import Counter, Dict, Iterable, List, Tuple


# Match '#' followed by at least one non-space, non-'#' character
# This is more permissive than \w+ and handles digits and underscores, while ignoring standalone '#'
# Include bare '#' and hashtags with any non-space continuation
HASHTAG_REGEX = re.compile(r"#\S*")


def parse_hashtags(line: str, lowercase: bool = True) -> List[str]:
	"""Extract hashtags from a line.

	Rules:
	- Hashtags are tokens starting with '#', optionally followed by non-space characters.
	- Standalone '#' is counted.
	- Multiple hashtags per line are supported.
	- Returned hashtags are lowercased by default (treat hashtags case-insensitively).
	"""
	tags = HASHTAG_REGEX.findall(line)
	if lowercase:
		tags = [t.lower() for t in tags]
	return tags


def chunk_indices(n_items: int, n_chunks: int) -> List[Tuple[int, int]]:
	"""Return (start, end) half-open index ranges that partition n_items into n_chunks as evenly as possible."""
	n_chunks = max(1, min(n_chunks, n_items or 1))
	base = n_items // n_chunks
	rem = n_items % n_chunks
	ranges: List[Tuple[int, int]] = []
	start = 0
	for i in range(n_chunks):
		size = base + (1 if i < rem else 0)
		end = start + size
		ranges.append((start, end))
		start = end
	return ranges


def worker_count_all(lines: List[str], lowercase: bool = True) -> Dict[str, int]:
	"""Count all hashtags in the given lines and return a dict of frequencies."""
	counter: Counter[str] = collections.Counter()
	for line in lines:
		for tag in parse_hashtags(line, lowercase=lowercase):
			counter[tag] += 1
	return dict(counter)


def worker_count_single(lines: List[str], target_tag: str, lowercase: bool = True) -> int:
	"""Count occurrences of a specific hashtag in the given lines and return the total count."""
	if lowercase:
		target_tag = target_tag.lower()
	total = 0
	for line in lines:
		# Early filter: only scan if '#' present
		if '#' not in line:
			continue
		for tag in parse_hashtags(line, lowercase=lowercase):
			if tag == target_tag:
				total += 1
	return total


def aggregate_counters(partials: Iterable[Dict[str, int]]) -> Dict[str, int]:
	agg: Counter[str] = collections.Counter()
	for part in partials:
		agg.update(part)
	return dict(agg)


def read_lines(file_path: str) -> List[str]:
	with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
		return f.readlines()


def ensure_hashtag_format(tag: str) -> str:
	tag = tag.strip()
	if not tag:
		return tag
	return tag if tag.startswith('#') else f'#{tag}'


def count_all_hashtags(file_path: str, m: int, lowercase: bool, top_k: int | None = 20) -> Dict[str, int]:
	lines = read_lines(file_path)
	# Pure serial path if m <= 1
	if m <= 1:
		agg = worker_count_all(lines, lowercase=lowercase)
		if top_k is not None and top_k > 0:
			return dict(collections.Counter(agg).most_common(top_k))
		return agg
	ranges = chunk_indices(len(lines), m)
	shards = [lines[s:e] for s, e in ranges if e > s]
	if not shards:  # empty file safeguard
		return {}

	with Pool(processes=max(1, len(shards))) as pool:
		partials = pool.map(worker_count_all, shards)

	agg = aggregate_counters(partials)
	# Fallback to single-process if parallel returned nothing but the file likely contains hashtags
	if not agg:
		# Quick heuristic: if any line contains '#', try serial
		if any('#' in ln for ln in lines):
			agg = worker_count_all(lines, lowercase=lowercase)
	if top_k is not None and top_k > 0:
		# Proper top-k by value from the aggregated dict
		top_items = sorted(agg.items(), key=lambda kv: (-kv[1], kv[0]))[:top_k]
		return dict(top_items)
	return agg


def count_single_hashtag(file_path: str, m: int, target_tag: str, lowercase: bool) -> int:
	lines = read_lines(file_path)
	# Pure serial path if m <= 1
	if m <= 1:
		return worker_count_single(lines, ensure_hashtag_format(target_tag), lowercase)
	ranges = chunk_indices(len(lines), m)
	shards = [lines[s:e] for s, e in ranges if e > s]

	target_tag = ensure_hashtag_format(target_tag)

	# Use starmap-like invocation by binding target
	args = [(shard, target_tag, lowercase) for shard in shards]
	if not args:  # empty file safeguard
		return 0
	with Pool(processes=max(1, len(shards))) as pool:
		partials = pool.starmap(worker_count_single, args)
	total = int(sum(partials))
	# Fallback to single-process count in case of any multiprocessing anomalies (e.g., CWD/path/env issues)
	if total == 0:
		return worker_count_single(lines, target_tag, lowercase)
	return total


def main(argv: List[str] | None = None) -> int:
	# Resolve default data file relative to this script to avoid CWD confusion
	script_dir = os.path.dirname(os.path.abspath(__file__))
	default_file = os.path.join(script_dir, "hashtags.txt")
	parser = argparse.ArgumentParser(description="Shared-nothing hashtag counter simulation (master/worker)")
	parser.add_argument("--file", default=default_file, help="Path to the ID-Hashtag input file")
	parser.add_argument("--mode", choices=["all", "single"], help="Counting mode: all hashtags or a single hashtag")
	parser.add_argument("--m", type=int, default=cpu_count(), help="Number of worker processors (default: CPU count)")
	parser.add_argument("--hashtag", default="", help="Target hashtag for --mode single (with or without leading #)")
	parser.add_argument("--no-lower", action="store_true", help="Disable lowercasing (hashtags treated case-sensitively)")
	parser.add_argument("--top", type=int, default=20, help="Top-K results to display for --mode all (set 0 for all)")
	parser.add_argument("-i", "--interactive", action="store_true", help="Launch interactive menu instead of using flags")

	args = parser.parse_args(argv)

	def prompt(prompt_text: str, default: str | None = None) -> str:
		try:
			sfx = f" [{default}]" if default is not None else ""
			val = input(f"{prompt_text}{sfx}: ").strip()
			return val if val else (default or "")
		except (EOFError, KeyboardInterrupt):
			print("\nAborted.")
			raise SystemExit(130)

	def prompt_int(prompt_text: str, default: int) -> int:
		while True:
			val = prompt(prompt_text, str(default))
			try:
				return int(val)
			except ValueError:
				print("Please enter a valid integer.")

	def prompt_bool(prompt_text: str, default: bool) -> bool:
		d = "y" if default else "n"
		while True:
			val = prompt(f"{prompt_text} (y/n)", d).lower()
			if val in ("y", "yes"): return True
			if val in ("n", "no"): return False
			print("Please answer y or n.")

	def run_once(file_path: str, mode: str, m: int, lowercase: bool, top_k: int, target: str) -> None:
		if not os.path.exists(file_path):
			print(f"Input file not found: {file_path}", file=sys.stderr)
			return
		if mode == "all":
			mp_m = max(1, m)
			results = count_all_hashtags(file_path, m=mp_m, lowercase=lowercase, top_k=(top_k if top_k > 0 else None))
			# Auto-retry serial if empty
			if not results and mp_m > 1:
				results = count_all_hashtags(file_path, m=1, lowercase=lowercase, top_k=(top_k if top_k > 0 else None))
			shown = len(results)
			print(f"\nTop {shown} hashtags (mode=all, m={mp_m if shown else 1}):")
			for tag, cnt in sorted(results.items(), key=lambda kv: (-kv[1], kv[0])):
				print(f"{tag}\t{cnt}")
		else:
			if not target:
				print("Target hashtag is required in single mode.", file=sys.stderr)
				return
			mp_m = max(1, m)
			total = count_single_hashtag(file_path, m=mp_m, target_tag=target, lowercase=lowercase)
			if total == 0 and mp_m > 1:
				total = count_single_hashtag(file_path, m=1, target_tag=target, lowercase=lowercase)
			print(f"\n{ensure_hashtag_format(target)}\t{total}")

	# Decide interactive vs. flags
	use_interactive = args.interactive or (args.mode is None and (argv is None or len(argv) == 0))

	if not use_interactive:
		file_path = args.file
		lowercase = not args.no_lower
		m = max(1, args.m)
		if args.mode == "all":
			run_once(file_path, "all", m, lowercase, args.top, args.hashtag)
		else:
			if not args.hashtag:
				print("--hashtag is required for --mode single", file=sys.stderr)
				return 2
			run_once(file_path, "single", m, lowercase, args.top, args.hashtag)
		return 0

	# Interactive menu loop
	while True:
		print("\n=== Hashtag Counter (Shared-Nothing) ===")
		print("1) Count ALL hashtags")
		print("2) Count a SINGLE hashtag")
		print("9) Debug: sample parsed tags")
		print("3) Exit")
		choice = prompt("Choose an option", "1")
		if choice == "3":
			return 0
		if choice not in ("1", "2", "9"):
			print("Invalid choice. Try again.")
			continue

		if choice == "9":
			file_path = prompt("Input file path", args.file)
			if not os.path.exists(file_path):
				print(f"Input file not found: {file_path}", file=sys.stderr)
				continue
			lines = read_lines(file_path)
			# Show a few parsed tags to validate regex on this machine
			parsed = []
			for ln in lines[:100]:
				parsed.extend(parse_hashtags(ln, lowercase=not args.no_lower))
			print(f"\nFirst 30 parsed tags: {parsed[:30]}")
			# Small serial frequency from first 1000 lines
			sample = worker_count_all(lines[:1000], lowercase=not args.no_lower)
			top_items = sorted(sample.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
			print("Top in first 1000 lines:")
			for tag, cnt in top_items:
				print(f"{tag}\t{cnt}")
			continue

		mode = "all" if choice == "1" else "single"
		file_path = prompt("Input file path", args.file)
		m = prompt_int("Number of worker processes (m)", max(1, args.m))
		lowercase = not prompt_bool("Case-sensitive hashtags?", default=False if not args.no_lower else True)

		if mode == "all":
			top_k = prompt_int("Show Top-K (0 = show all)", args.top)
			run_once(file_path, mode, m, lowercase, top_k, target="")
		else:
			target = prompt("Hashtag to search (with or without leading #)", args.hashtag or "")
			run_once(file_path, mode, m, lowercase, top_k=args.top, target=target)

		again = prompt_bool("Run another task?", True)
		if not again:
			return 0


if __name__ == "__main__":
	raise SystemExit(main())

