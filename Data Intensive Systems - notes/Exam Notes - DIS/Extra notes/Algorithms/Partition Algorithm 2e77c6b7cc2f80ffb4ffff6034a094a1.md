# Partition Algorithm

## Partition Algorithm (for Frequent Itemset Mining)

### Term definition table

| Term | Definition |
| --- | --- |
| Partition Algorithm | A parallel algorithm for mining **frequent itemsets** by splitting the database into partitions. |
| Partition | A subset of the transaction database. |
| Local Frequent Itemset | Itemsets frequent in one partition. |
| Global Frequent Itemset | Itemsets frequent in the whole database. |
| Support | Fraction of transactions containing an itemset. |
| Minimum Support | Threshold for frequency. |
| Candidate Set | Union of all local frequent itemsets. |
| Data Scan | One full pass over the database. |

---

### Definition about the algorithm

The **Partition Algorithm** reduces the number of full database scans by splitting the dataset into **smaller partitions**, finding frequent itemsets locally, and then verifying them globally.

It is designed to work efficiently on **large or distributed datasets**.

---

### Advantages / disadvantages

**Advantages**

- Requires only **two full scans** of the database.
- Suitable for parallel and distributed systems.
- Much faster than Apriori on large data.

**Disadvantages**

- Still generates many candidates.
- Local frequent sets may be large.
- Requires merging and re-counting.

---

### Math equation

An itemset X is **globally frequent** if:

$support(X) = \sum_{i=1}^{p} support_i(X) \ge \text{min\_support}$

where p is the number of partitions.

---

### Runtime

Let:

- n = number of transactions
- p = number of partitions

**Best & Worst**

$O(n)$

(two scans over all data)

---

### Python-like pseudo code

```python
def partition_algorithm(transactions, min_support):
     partitions = split(transactions)
     candidates =set()

 for partin partitions:
         local_frequent = apriori(part, min_support)
         candidates |= local_frequent
 
     global_frequent = []
 for itemsetin candidates:
 if support(itemset, transactions) >= min_support:
             global_frequent.append(itemset)

return global_frequent
```

---

### Step-by-step through the algorithm

1. Divide the database into partitions.
2. Mine frequent itemsets in each partition.
3. Collect all local frequent itemsets.
4. Merge them into a global candidate set.
5. Scan the full database again.
6. Keep only those meeting minimum support.
7. Output global frequent itemsets.