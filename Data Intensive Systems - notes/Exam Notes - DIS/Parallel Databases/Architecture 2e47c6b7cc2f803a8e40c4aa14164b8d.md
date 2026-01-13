# Architecture

# Definition

**Parallel Databases** link multiple smaller machines (processors and disks) to achieve the throughput and performance of a single large machine. The system executes operations in parallel whenever possible to improve and I/O speeds.

# Core Idea

Parallel database architectures are defined by how processors, memory and disks are connected and shared.

[Shared Memory](Architecture/Shared%20Memory%202e47c6b7cc2f807d9f19ca3ca4f9eea8.md)

[Shared Disk](Architecture/Shared%20Disk%202e47c6b7cc2f8051ab85d344e8a72aac.md)

[Shared Nothing](Architecture/Shared%20Nothing%202e47c6b7cc2f8010a04ef3f9e1bdf347.md)

[Hierarchical](Architecture/Hierarchical%202e47c6b7cc2f80588a81cb732448b055.md)

# Summary Table

| **Architecture** | **Shared Resource** | **Scalabilty** | **Bottleneck** |
| --- | --- | --- | --- |
| **Shared Memory** | Memory & Disk | Low (<64 CPUs) | System Bus |
| **Shared Disk** | Disk | Medium | Disk Interconnection |
| **Shared Nothing** | None (Network only) | High (1000s) | Network Latency |
| **Hierarchical** | Hybrid | High | Hybrid |