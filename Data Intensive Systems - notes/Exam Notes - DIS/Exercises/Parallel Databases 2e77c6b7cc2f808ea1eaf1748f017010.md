# Parallel Databases

# 1. Count All Hashtags

> We want to count each hashtag that appears in the ID-Hashtag file. If you have a shared-nothing cluster with m processors, how can that help to speed up the counting? Describe your data partitioning strategy and counting algorithm.
> 

## Data Partitioning Strategy

**Horizontal partitioning (by lines):**

- Master splits file into $m$ roughly equal chunks
- Each worker receives $n/m$ lines
- Workers process independently (shared-nothing)

**Counting Algorithm**

```
1. MASTER: Split file into m partitions, send to workers
2. WORKERS: Each builds local KV store {hashtag → count}
3. MASTER: Merge all partial results by summing counts
```

## Complexity

- **Parallel time:** $O(n/m)$ for counting + $O(k)$ for merging ($k =$ unique hashtags)
- **Speedup:** ~m times faster than sequential

```python
from collections import defaultdict
from multiprocessing import Pool

def count_hashtags_local(lines):
    """Worker: count hashtags in assigned lines"""
    local_counts = defaultdict(int)
    for line in lines:
        hashtags = [w for w in line.split() if w.startswith('#')]
        for tag in hashtags:
            local_counts[tag] += 1
    return dict(local_counts)

def merge_counts(partial_results):
    """Master: merge all partial counts"""
    final_counts = defaultdict(int)
    for partial in partial_results:
        for tag, count in partial.items():
            final_counts[tag] += count
    return dict(final_counts)

def parallel_count_all(filename, m):
    # Master: read and partition data
    with open(filename) as f:
        lines = f.readlines()
    
    chunk_size = len(lines) // m
    partitions = [lines[i*chunk_size:(i+1)*chunk_size] for i in range(m)]
    
    # Workers: count in parallel
    with Pool(m) as pool:
        partial_results = pool.map(count_hashtags_local, partitions)
    
    # Master: merge results
    return merge_counts(partial_results)
```

---

## 2. Count Specific Hashtag

> *If we only want to know the frequency of a given specific hashtag, how can you make use of the shared-nothing architecture? Describe your data partitioning strategy and counting algorithm.*

### Data Partitioning Strategy
**Same horizontal partitioning:**
- Master splits file into m chunks
- Each worker searches only for target hashtag

### Counting Algorithm
```
1. MASTER: Broadcast target hashtag + data partition to workers
2. WORKERS: Count only target hashtag occurrences locally
3. MASTER: Sum all partial counts (single integer from each)
```