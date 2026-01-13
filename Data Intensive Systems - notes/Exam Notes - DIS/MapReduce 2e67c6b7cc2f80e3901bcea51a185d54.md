# MapReduce

# Definition

| Term | Definition |
| --- | --- |
| Scalability | A system’s ability to swiftly enlarge or reduce infrastructure power or size, or the ability to process larger amounts of data |
| Scale-up (Vertical) | Adding more capacity to existing resources, such as equipping a computer with better CPUs, more RAM, or larger hard disks |
| Scale-out (Horizontal) | Adding more computers to a system to spread the workload across a cluster of machines |
| MapReduce | A paradigm encompassing a programming model, an execution framework, and a software implementation (like Hadoop) for processing large datasets |
| Map Function | A function that takes an input key/value pair and produces a set of intermediate key/value pairs |
| Reduce Function | A function that takes an intermediate key and a list of all values associated with that key, merging them to form a smaller set of values |
| Shuffle and Sort | The phase acting as a barrier between map and reduce that aggregates values by keys and ensures intermediate data arrives at reducers in order |
| Combiner | An optimization component acting as a "mini-reducer" that performs local aggregation before the Shuffle and Sort phase |
| Partitioner | A component that divides the intermediate key space and assigns specific key-value pairs to specific reducers (often using hashing) |
| Distributed File System (DFS) | A storage system that abandons the separation of computation and storage by dividing data into blocks and replicating them across cluster nodes |
| Namenode | The master node in HDFS responsible for managing metadata, the directory structure, and the file namespace |
| Datanode | The slave node in HDFS that maps block IDs to physical locations and manages the actual data blocks on its local disk |
| JobTracker | The specific submission node in Hadoop that coordinates the execution of programs |

---

[Background](MapReduce/Background%202e67c6b7cc2f80e997b4dcb20ec137e0.md)

[**Programming Model**](MapReduce/Programming%20Model%202e67c6b7cc2f8099828bf3bf85735320.md)

[Execution Framework](MapReduce/Execution%20Framework%202e67c6b7cc2f80eda3dcf61fa844d74d.md)

[Software Implementation](MapReduce/Software%20Implementation%202e67c6b7cc2f801283a7e81b283cd654.md)

[MapReduce and Databases](MapReduce/MapReduce%20and%20Databases%202e67c6b7cc2f8030b1d9ffb13a0b9967.md)