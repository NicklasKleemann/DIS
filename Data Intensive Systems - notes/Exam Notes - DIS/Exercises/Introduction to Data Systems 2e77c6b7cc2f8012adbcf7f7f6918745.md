# Introduction to Data Systems

# Tweet Hashtag Analysis: Data Models & Implementation

## Recommended Data Model: Key-Value Store

A key-value store (e.g., Redis, Python dictionary) is ideal here because:

- Hashtags are natural keys with counts as values
- $O(1)$ lookup for frequency queries
- Simple increment operations
- Built-in sorting capabilities (Redis sorted sets)

---

## 1. Hashtag Frequency Queries

> We may want to know the frequency of an arbitrary hashtag. How do you implement this if our requests are sparse? Will you implement in the same way if our requests are frequent?
> 

**Sparse Requests**

```
Linear scan approach:
- Read file line by line
- Check if target hashtag exists in each line
- Increment counter on match
- Time: O(n) per query
```

**Why:** No preprocessing overhead; acceptable for infrequent queries

**Frequent Requests**

```
Cached approach:
- Use KV store as cache: {hashtag → count}
- On query: check cache first
- Cache miss → scan file → store result
- Time: O(1) for cache hits
```

**Why:** Amortizes computation cost across repeated queries

---

## 2. Top-10 Frequent Hashtags

> *How do you implement if we want to return the top-10 frequent hashtags?*
> 

```
Full aggregation approach:
1. Scan entire file once
2. Build KV store: {hashtag → count}
3. Sort by value descending
4. Return top 10

Alternative: Use Redis Sorted Set (ZREVRANGE)
```

---

## **3. Handling Continuous Appends**

> If new lines are appended to the original raw file continuously, what would you change for your implementations in 1 and 2?
> 

### For Frequency (Question 1)

- **Invalidate or update cache** when new lines arrive
- Process only new lines, increment existing cache entries

### For Top-10 (Question 2)

- Maintain **two structures**:
    1. Full KV store: `{hashtag → count}`
    2. Top-10 cache (sorted set or min-heap)

On new line:

- Update counts in KV store
- Compare updated counts against 10th place
- Promote to top-10 cache if threshold exceeded

---

## Summary Table

| Scenario | Data Structure | Complexity |
| --- | --- | --- |
| Sparse frequency | Linear scan | O(n) per query |
| Frequent frequency | KV cache | O(1) hit, O(n) miss |
| Top-10 | KV store + sorted structure | O(n) initial, O(k) update |
| Streaming updates | KV + Top-10 cache | O(1) incremental |