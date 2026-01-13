# Round-Robin Partitioning

## Round-Robin Partitioning

### Term definition table

| Term | Definition |
| --- | --- |
| Round-Robin Partitioning | A **data partitioning** method that distributes tuples evenly across nodes in a cyclic order. |
| Partition | A subset of a database stored on one node. |
| Node | A machine in a parallel or distributed database system. |
| Tuple | A row in a table. |
| Load Balancing | Evenly spreading data across nodes. |
| Coordinator | System component that assigns incoming tuples to nodes. |
| Skew | Uneven data distribution across nodes. |

---

### Definition about the algorithm

**Round-Robin Partitioning** assigns each incoming record to the **next node in sequence**, cycling through all nodes.

It guarantees an **even distribution** of rows, making it useful when the system wants balanced storage and parallel query processing.

---

### Advantages / disadvantages

**Advantages**

- Very simple.
- Perfect load balancing.
- No need to know data values.
- Good for full-table scans.

**Disadvantages**

- Does not preserve locality of related data.
- Joins are expensive.
- No support for range or key-based queries.

---

### Math equation

For tuple number iii and NNN nodes:

$node = i \bmod N$

---

### Runtime

Let:

- n = number of tuples

**Partitioning**

- Best & Worst: $O(n)$

**Lookup**

- Best: $O(N)$
- Worst: $O(N)$

---

### Python-like pseudo code

```python
def round_robin_partition(data, N):
    partitions = [[]for _inrange(N)]

for i, rowinenumerate(data):
        node = i % N
        partitions[node].append(row)

return partitions
```

---

### Step-by-step through the algorithm

1. Start with the first node.
2. Assign the first tuple to node 0.
3. Assign the second tuple to node 1.
4. Continue until the last node.
5. Cycle back to node 0.
6. Repeat until all data is assigned.