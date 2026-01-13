# MapReduce

> *Write your code using MapReduce in Python and Jupyter Notebook to resolve the following two tasks:*
> 
> 1. *To count each hashtag that appears in the ID-Hashtag file*
> 2. *To return the hashtag with the highest appearance frequency*
> 
> *NB: Think how these two tasks are correlated but different, and how you may reuse your code as much as possible.*
> 

## Task Correlation Analysis

| Aspect | Task 1: Count All | Task 2: Find Max |
| --- | --- | --- |
| Map Phase | Same (emit hashtag, 1) | Same (reuse) |
| Reduce Phase | Sum counts per hashtag | Sum + find maximum |
| Output | {hashtag → count} | Single (hashtag, count) |

**Key Insight:** Task 2 builds on Task 1 — first count all, then find max.

---

## Pseudocode

### Task 1: Count All Hashtags

```
FUNCTION map(line):
    FOR each word in line:
        IF word starts with '#':
            EMIT(word, 1)

FUNCTION reduce(hashtag, counts_list):
    total = SUM(counts_list)
    EMIT(hashtag, total)

FUNCTION count_hashtags(dataset):
    intermediate = empty key-value store
    
    // Map Phase
    FOR each line in dataset:
        FOR each (hashtag, 1) from map(line):
            intermediate[hashtag].APPEND(1)
    
    // Reduce Phase
    result = empty key-value store
    FOR each (hashtag, counts_list) in intermediate:
        result[hashtag] = reduce(hashtag, counts_list)
    
    RETURN result
```

## Task 2: Find Most Frequent Hashtag

```
FUNCTION find_max_hashtag(dataset):
    // Reuse Task 1
    hashtag_counts = count_hashtags(dataset)
    
    // Find maximum
    max_hashtag = NULL
    max_count = 0
    
    FOR each (hashtag, count) in hashtag_counts:
        IF count > max_count:
            max_count = count
            max_hashtag = hashtag
    
    RETURN (max_hashtag, max_count)
```

---

## Python Implementation

```python
from collections import defaultdict
from typing import List, Dict, Tuple

class MapReduce:
    """MapReduce framework for hashtag processing"""
    
    def __init__(self):
        self.intermediate = defaultdict(list)
        self.result = defaultdict(int)
    
    def mapper(self, line: str) -> None:
        """
        Map Phase: Extract hashtags and emit (hashtag, 1) pairs
        
        Pseudocode:
            FOR each word in line:
                IF word starts with '#':
                    EMIT(word, 1)
        """
        hashtags = [word for word in line.split() if word.startswith('#')]
        for hashtag in hashtags:
            self.intermediate[hashtag].append(1)
    
    def reducer(self) -> Dict[str, int]:
        """
        Reduce Phase: Sum counts for each hashtag
        
        Pseudocode:
            FOR each (hashtag, counts_list) in intermediate:
                result[hashtag] = SUM(counts_list)
        """
        for hashtag, counts in self.intermediate.items():
            self.result[hashtag] = sum(counts)
        return dict(self.result)

# =============================================================================
# Task 1: Count All Hashtags
# =============================================================================

def count_hashtags(dataset: List[str]) -> Dict[str, int]:
    """
    Process dataset and return all hashtag counts
    
    Pseudocode:
        intermediate = {}
        FOR each line in dataset:
            map(line) -> append to intermediate
        FOR each key in intermediate:
            result[key] = reduce(key, intermediate[key])
        RETURN result
    """
    mapred = MapReduce()
    
    # Map phase
    for line in dataset:
        mapred.mapper(line)
    
    # Reduce phase
    hashtag_counts = mapred.reducer()
    
    return hashtag_counts

# =============================================================================
# Task 2: Find Most Frequent Hashtag
# =============================================================================

def find_top_hashtag(dataset: List[str]) -> Tuple[str, int]:
    """
    Find the hashtag with highest frequency (reuses Task 1)
    
    Pseudocode:
        counts = count_hashtags(dataset)  // Reuse Task 1
        max_tag, max_count = NULL, 0
        FOR each (tag, count) in counts:
            IF count > max_count:
                max_tag, max_count = tag, count
        RETURN (max_tag, max_count)
    """
    # Reuse Task 1
    hashtag_counts = count_hashtags(dataset)
    
    # Find maximum
    top_hashtag = max(hashtag_counts.items(), key=lambda x: x[1])
    
    return top_hashtag

# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    # Sample dataset
    posts = [
        "1020253525161283584 #Hartberg #Finance #Job #Jobs #Hiring",
        "1020253526789456123 #coffee #Finance",
        "1020253527891234567 #sunset #Job #coffee",
        "1020253528912345678 #coffee #Finance #Job"
    ]
    
    # Task 1: Count all hashtags
    print("=" * 50)
    print("Task 1: Count All Hashtags")
    print("=" * 50)
    result = count_hashtags(posts)
    for hashtag, count in sorted(result.items()):
        print(f"  {hashtag}: {count}")
    
    # Task 2: Find most frequent
    print("\n" + "=" * 50)
    print("Task 2: Most Frequent Hashtag")
    print("=" * 50)
    top_tag, top_count = find_top_hashtag(posts)
    print(f"  {top_tag}: {top_count}")
```