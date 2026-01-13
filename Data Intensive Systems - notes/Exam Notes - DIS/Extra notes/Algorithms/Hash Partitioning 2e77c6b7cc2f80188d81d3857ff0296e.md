# Hash Partitioning

## Hash Partitioning

### Term definition table

| Term | Definition |
| --- | --- |
| Hash Partitioning | A **data partitioning** method that assigns records to nodes using a **hash function** on a key. |
| Partition | Subset of data stored on one node. |
| Hash Function | Function that maps a key to a numeric value. |
| Partition Key | Attribute used to compute the hash (e.g., customer_id). |
| Node | A machine in a distributed database. |
| Collision | When different keys map to the same hash bucket. |
| Load Balancing | Even distribution of data. |

---

### Definition about the algorithm

**Hash Partitioning** distributes data by applying a **hash function** to a chosen key and assigning the record to a node based on the hash value.

This ensures that rows with the same key always go to the **same node**, making joins and lookups efficient.

---

### Advantages / disadvantages

**Advantages**

- Even data distribution.
- Fast equality lookups.
- Good for joins on the partition key.

**Disadvantages**

- Poor for range queries.
- Repartitioning is expensive when nodes change.
- Hash function choice matters.

---

### Math equation

For key k and N nodes:

$node = h(k) \bmod N$

---

### Runtime

Let:

- n = number of records

**Partitioning**

- Best & Worst: $O(n)$

**Lookup by key**

- Best & Worst: $O(1)$

---

### Python-like pseudo code

```python
def hash_partition(data, N, key):
    partitions = [[]for _inrange(N)]

for rowin data:
        node =hash(row[key]) % N
        partitions[node].append(row)

return partitions
```

---

### Step-by-step through the algorithm

1. Choose a partition key.
2. Apply a hash function to the key.
3. Take modulo by number of nodes.
4. Assign the row to that node.
5. Repeat for all records.