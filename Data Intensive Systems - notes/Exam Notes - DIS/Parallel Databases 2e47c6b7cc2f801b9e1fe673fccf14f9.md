# Parallel Databases

# Definition

| Term | Definition |
| --- | --- |
| Parallel DBMS | A database system that runs across multiple processors and disks, designed to execute operations in parallel to improve throughput and processing speeds |
| Shared Memory | An architecture where processors share a common memory (and disks) via a bus, allowing efficient communication but limited scalability due to bus bottlenecks |
| Shared Disk | An architecture where processors have private memories but can access all disks via an interconnection network, offering fault tolerance but potential bottlenecks at the disk connection |
| Shared Nothing | An architecture where each node has its own processor, memory, and disks, communicating only via network; this minimizes resource interference and scales well |
| Hierarchical Architecture | A hybrid structure where the top level is shared-nothing (nodes connected by network), but individual nodes may be shared-memory systems |
| I/O Parallelism | Reducing the time required to retrieve relations from disk by partitioning the relations across multiple disks |
| Horizontal Partitioning | The technique of dividing the tuples of a relation among many disks such that each tuple resides on exactly one disk |
| Round-robin Partitioning | A strategy where the *i*th tuple is sent to disk *i mod n*; it ensures balanced retrieval but makes range queries difficult |
| Hash Partitioning | A strategy where a hash function is applied to an attribute to determine the disk assignment; excellent for point queries and sequential access |
| Range Partitioning | A strategy where tuples are distributed based on value intervals (e.g., *x* < 5); this supports range queries but can lead to execution skew if data is unbalanced |
| Interquery Parallelism | The execution of multiple distinct queries or transactions simultaneously to increase overall system throughput |
| Intraquery Parallelism | The execution of a single query in parallel across multiple processors or disks to speed up long-running tasks |
| Intraoperation Parallelism | A form of intraquery parallelism where a single operation (like a join or sort) is split so different subsets of data are processed in parallel |
| Interoperation Parallelism | A form of intraquery parallelism where different operations within the same query are executed simultaneously |
| Partitioned Parallel Join | A join algorithm where both relations are partitioned on the join attributes and sent to specific processors to be joined locally |
| Fragment-and-Replicate Join | A join technique (often for non-equi joins) where one relation is partitioned while the other is replicated across all processors |

# Goal

Improve processing and I/O speeds using multiple CPUs and disks

# Difference vs. Distributed DBs

- **Parallel**: Physically close, high-speed LAN, small communication cost
- **Distributed:** Geographically separated (latency matters), public networks, shared-nothing usually

[Architecture](Parallel%20Databases/Architecture%202e47c6b7cc2f803a8e40c4aa14164b8d.md)

[I/O Parallelism](Parallel%20Databases/I%20O%20Parallelism%202e47c6b7cc2f8087b40de7e4d296675a.md)

[**Types of Parallelism**](Parallel%20Databases/Types%20of%20Parallelism%202e57c6b7cc2f8004b5c3d75cf0f4ff90.md)