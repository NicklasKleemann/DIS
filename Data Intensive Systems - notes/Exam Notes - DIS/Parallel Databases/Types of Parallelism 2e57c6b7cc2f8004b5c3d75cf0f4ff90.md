# Types of Parallelism

# Definition

**Parallelism** in database systems refers to the execution of operations simultaneously across multiple processors or disks. The specific type of parallelism chosen depends on whether the goal is to increase the volume of work done (throughput) or to decrease the time it takes to finish a single job (response time)

---

# Core Idea

Parallelism is categorised into two main levels:

[Interquery Parallelism](Types%20of%20Parallelism/Interquery%20Parallelism%202e57c6b7cc2f80068c0efea92fa989d3.md)

[Intraquery Parallelism](Types%20of%20Parallelism/Intraquery%20Parallelism%202e57c6b7cc2f80a3a47bfc86cffa6fa3.md)

<aside>
💡

**Inter = Between** (between different queries)
**Intra = Within** (within a single query)

</aside>

---

# Intraquery Parallelism for Relational Operations

[Parallel Selection](Types%20of%20Parallelism/Parallel%20Selection%202e57c6b7cc2f8041b9dfdf5768f6df7e.md)

[Parallel Sort](Types%20of%20Parallelism/Parallel%20Sort%202e57c6b7cc2f80afb742f3f8860673a5.md)

[Parallel Join](Types%20of%20Parallelism/Parallel%20Join%202e57c6b7cc2f801ebb55fe836216c5f5.md)

# Interquery vs Intraquery Parallelism

| Aspect | Interquery | Intraquery |
| --- | --- | --- |
| Unit of parallelism | Whole query | Parts of single query |
| Goal | $\uparrow$ Throughput | $\downarrow$ Response time |
| Speedup per query | None | Yes |
| Use case | OLTP (many small queries) | OLAP (few complex queries) |
| Complexity | Lower | Higher |

```mermaid
flowchart TB
    subgraph "INTERQUERY Parallelism"
        direction LR
        QA["Query A\n(complete)"] --> PA["Proc 1"]
        QB["Query B\n(complete)"] --> PB["Proc 2"]
        QC["Query C\n(complete)"] --> PC["Proc 3"]
    end
    
    subgraph "INTRAQUERY Parallelism"
        direction LR
        Q1["Single Query"] --> F1["Fragment 1"] --> P1["Proc 1"]
        Q1 --> F2["Fragment 2"] --> P2["Proc 2"]
        Q1 --> F3["Fragment 3"] --> P3["Proc 3"]
        P1 --> M["Merge"]
        P2 --> M
        P3 --> M
        M --> R["Result"]
    end
```

---

# Combining Inter and Intra Query Parallelism

Modern systems use **both:**

```mermaid
flowchart TB
    subgraph "Hybrid Approach"
        Q1["Query 1 (complex)"] --> IP1["Intraquery Parallel"]
        Q2["Query 2 (simple)"] --> S2["Single Processor"]
        Q3["Query 3 (complex)"] --> IP3["Intraquery Parallel"]
    end
    
    IP1 --> P1["Proc 1"]
    IP1 --> P2["Proc 2"]
    S2 --> P3["Proc 3"]
    IP3 --> P4["Proc 4"]
    IP3 --> P5["Proc 5"]
```

- Simple queries: single processor (interquery only)
- Complex queries: multiple processors (intraquery)
- All queries run concurrently (interquery)