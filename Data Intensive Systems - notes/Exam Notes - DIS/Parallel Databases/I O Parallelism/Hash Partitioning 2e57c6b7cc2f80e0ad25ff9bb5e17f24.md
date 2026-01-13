# Hash Partitioning

# Definition

Hash partitioning is a data partition technique in parallel databases where tuples are assigned to disks/nodes using **hash function** applied to one or more **partitioning attributes.**

It ensures that tuples with the **same attribute value** always go to the **same partition**, which enables efficient point queries and parallel joins

---

# Motivation

In parallel databases:

- Data must be distributed across multiple disk/processors
- We want **load balancing** (even distribution)
- We need **efficient point queries** on the partitioning attribute
- We need to support **parallel equi-joins**

Hash partitioning achieves all of these goals

---

# How Hash Partitioning Works

1. Choose one or more attributes **partitioning attributes**
2. Choose a **hash function** $h$ with range $0$ to $n-1$ (where $n = \text{number of disks}$)
3. For each tuple, compute $h(\text{attribute value})$
4. Send the tuple to disk $i$ where $i=h(\text{attribute value})$

---

# Hash Partitioning Formula

$\text{Disk}_i=h(\text{attribute value) mod } n$

Where:

- $h=\text{hash function}$
- $n=\text{number of disks/partitions}$

---

# Example (from the slides)

| **Tuple** | $x$ value | $h(x)=x\mod 3$ | Assigned Disk |
| --- | --- | --- | --- |
| $t_1$ | 1 | 1 | Disk 1 |
| $t_2$ | 2 | 2 | Disk 2 |
| $t_3$ | 15 | 0 | Disk 0 |
| $t_4$ | 6 | 0 | Disk 0 |
| $t_5$ | 7 | 1 | Disk 1 |
| $t_6$ | 9 | 0 | Disk 0 |
| $t_7$ | 12 | 0 | Disk 0 |
| $t_8$ | 5 | 2 | Disk 2 |
| $t_9$ | 8 | 2 | Disk 2 |
- **Result:**
    - Disk 0: $t_3,t_4,t_6,t_7$
    - Disk 1: $t_1,t_5$
    - Disk 2: $t_2,t_8,t_9$

---

# Query Performance with Hash Partitioning

## Point Query on Partitioning Attribute (e.g., “Find $x=8$”)

| Scenario | Disks Searched | Response Time |
| --- | --- | --- |
| Without local index | 1 | $m$ (all buckets) |
| With local index | 1 | 1 |

**Key insight:** Only **1 disk** needs to be searched (compute $h(8)=8\mod3=2\rarr$ Disk 2)

## Range Query on Partitioning Attribute (e.g., “Find $5<x \le 8$”)

| **Scenario** | Disks Searched  | Response Time |
| --- | --- | --- |
| Without local index | All $n$ disks | $m$ |
| With local index | All $n$ disks | 1 |

**Problem:** Hash destroys ordering $\rarr$ must search **all disks**

## Query NOT on Partitioning Attribute

- Must search **all $n$ disks** regardless
- No advantage over other partitioning methods

---

# Advantages of Hash Partitioning

1. **Good for point queries** on partitioning attribute (only 1 disk accessed)
2. **Well-balanced distribution** if hash function is good and attributes from a key
3. **Efficient parallel joins** using same hash function on join attributes
4. **Local indexes** can be maintained per disk

---

# Disadvantages of Hash Partitioning

1. **Poor for range queries $\rarr$** no clustering, must access all disks
2. **Skew possible** if many tuples have same attribute value
3. **Redistribution required** when adding/removing disks

---

# Hash Partitioning for Parallel Joins

**Critical concept for exams:**

For **partitioned parallel join** on $r\bowtie s$

1. Both relations must be hash partitioned on **join attributes**
2. Must use the **same hash functions**
3. Each processor computes local join: $r_i\bowtie s_i$

**Why same hash function?** Matching tuples (same join key) go to same processor

---

# Partitioned Parallel Hash Join Algorithm

1. Hash partition relation $s$ using $h_1$ on join attribute $\rarr$ distrbute to processors
2. At each processor, further partition using $h_2$ (for local hash join)
3. Hash partition relation $r$ using same $h_1 \rarr$ distribute to processors
4. Each processor $P_i$ performs local hash join on $r_i$ and $s_i$
5. Union of all local results = final result 

# Common Exam Questions

1. **“Which partitioning is best for point queries?” $\rarr$** Hash or Range
2. **“Why must both relations use same hash functions for joins?” $\rarr$** Matching tuples must be co-located
3. **“What happens with range queries on hash partitioned data?” $\rarr$** All disks must be searched
4. **“Calculate which disk a tuple goes to” $\rarr$** Apply $h(x)\mod n$