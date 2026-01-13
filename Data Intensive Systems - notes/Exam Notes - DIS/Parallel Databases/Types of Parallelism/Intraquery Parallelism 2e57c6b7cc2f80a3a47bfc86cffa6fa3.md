# Intraquery Parallelism

# Definition

**Intraquery parallelism** is a form of parallelism where a **single query is executed in parallel** across multiple processors by breaking it into smaller tasks

The goal is to **reduce response time** for individual queries, especially complex ones

---

# Key Concept

```mermaid
flowchart TB
    Q["Single Query"] --> D["Decompose"]
    D --> T1["Task 1"]
    D --> T2["Task 2"]
    D --> T3["Task 3"]
    T1 --> P1["Processor 1"]
    T2 --> P2["Processor 2"]
    T3 --> P3["Processor 3"]
    P1 --> M["Merge Results"]
    P2 --> M
    P3 --> M
    M --> R["Final Result"]
```

- **One query = Multiple Processors**
- Reduces **response time** for complex queries
- Essential for **decision support / OLAP** workloads

---

# Two Types of Intraquery Parallelism

1. **Intraoperation Parallelism**

Parallelism **within a single operation** (e.g., a single `SELECT`, `JOIN` or `SORT`).

**Example:** Parallel table scan

- Relation partitioned across $n$ disks
- Each processor scans its partition simultaneously
- Results merged

```mermaid
flowchart LR
    subgraph "Parallel Table Scan"
        R["Relation R"] --> P1["Proc 1 scans Disk 1"]
        R --> P2["Proc 2 scans Disk 2"]
        R --> P3["Proc 3 scans Disk 3"]
    end
    P1 --> M["Merge"]
    P2 --> M
    P3 --> M
```

1. **Interoperation Parallelism**

Parallelism **between different operations** in a query plan

**Two sub-types:**

- **Pipelined parallelism:** Output of one operation feeds directly into next
- **Independent parallelism:** Unrelated operations run simultaneously

```mermaid
flowchart LR
    subgraph "Pipelined Parallelism"
        Scan["Scan R"] -->|"tuples flow"| Join["Join"]
        Join -->|"tuples flow"| Proj["Project"]
    end
```

```mermaid
flowchart LR
    subgraph "Independent Parallelism"
        S1["Scan R"] --> J["Join R ⋈ S"]
        S2["Scan S"] --> J
    end
```

---

# Intraoperation vs Interoperation

| Aspect | Intraoperation | Interoperation |
| --- | --- | --- |
| Parallelism within | Single operation | Multiple operations |
| Scalabilty | High (scales with data) | Limited by query structure |
| Example | Parallel scan, parallel join | Pipeline, independent scans |
| Speedup potential | High | Moderate |

# Parallel Scan

Given: Relation $R$ partitioned across 4 disks

**Sequential scan:** Read all 4 partitions one by one $\rarr$ Time = 4 units

**Parallel scan:** Each processor reads it partition simultaneously $\rarr$ Time = 1 unit

$$
\text{Speedup}=\frac{\text{Sequential Time}}{\text{Parallel Time}}=\frac{4}{1}=4
$$

---

# Speedup and Scaleup

## Speedup

**Definition:** How much fast a query runs with more processors

$$
\text{Speedup}=\frac{\text{Time with 1 processor}}{\text{Time with }n\text{ processors}}
$$

**Ideal (linear) speedup: $\text{Speedup} =n\text{ with }n \text{ processors}$**

```mermaid
flowchart LR
    subgraph "Speedup"
        direction TB
        T1["1 proc: 100 sec"]
        T4["4 proc: 25 sec"]
        SP["Speedup = 4"]
    end
```

## Scaleup

**Definition:** Ability to handle larger problems with more resources

$$
\text{Scaleup}=\frac{\text{Problem size with }n \text{ processors}}{\text{Problem size with 1 processor}}
$$

**Ideal scaleup:** Handle $n\times$more data with $n$ processors in same time

---

# Factors Limiting Speedup

1. **Startup Cost**
    
    Time to initiate parallel operations:
    
    - Process creation
    - Communication setup
    - Task distribution
2. **Interference**
    
    Contention for shared resources:
    
    - Memory bus
    - Disk I/O bandwidth
    - Network
3. **Skew**
    
    **Uneven distribution of work** among processors
    
    **Types of skew:**
    
    - **Attribute-value skew:** Some values much more common
    - **Partition skew:** Unequal partition sizes
    - **Execution skew:** Some tasks take longer

```mermaid
flowchart LR
    subgraph "Skew Problem"
        P1["Proc 1: 10 tuples (done quickly)"]
        P2["Proc 2: 10 tuples (done quickly)"]
        P3["Proc 3: 1000 tuples (BOTTLENECK)"]
    end
```

**Result:** System waits for slowest processor $\rarr$ poor speedup

---

# Effect of Skew

**Without skew (balanced):**

- 4 processors, 1000 tuples each
- Each finishes in 10 sec
- Total time: 10 sec
- Speedup: 4

**With skew (unbalanced):**

- 3 processors, 100 tuples each (finish in 1 sec)
- 1 processors: 3700 tuples (finishes in 37 sec)
- Total time: 37 sec (waiting for slowest)
- Speedup $\frac{40}{37}\approx1.08$ (terrible!)

---

## Parallel Selection $(\sigma)$

### Point query on partitioning attribute

- Hash/Range: Only 1 processor works
- Round-robin: All processors work

### Range query on partitioning attribute

- Range: Few processors (those with relevant ranges)
- Hash/Round-robin: All processors

## Parallel Sort

[Parallel ](Intraquery%20Parallelism/Parallel%202e57c6b7cc2f8047929cf776ae850c3f.md)

Two main approaches:

### Range-Partitioning Sort

![image.png](Intraquery%20Parallelism/image.png)

1. **Redistribute by range on sort attribute**

![image.png](Intraquery%20Parallelism/image%201.png)

1. **Each processors sort locally**

![image.png](Intraquery%20Parallelism/image%202.png)

1. **Concatenate results (trivial merge!)**

![image.png](Intraquery%20Parallelism/image%203.png)

---

### Parallel External Sort-Merge

![image.png](Intraquery%20Parallelism/image%204.png)

1. **Each processors sorts local data**

![image.png](Intraquery%20Parallelism/image%205.png)

1. **Merge sorted runs across processors**

![image.png](Intraquery%20Parallelism/image%206.png)

![image.png](Intraquery%20Parallelism/image%207.png)

![image.png](Intraquery%20Parallelism/image%208.png)

![image.png](Intraquery%20Parallelism/image%209.png)

![image.png](Intraquery%20Parallelism/image%2010.png)