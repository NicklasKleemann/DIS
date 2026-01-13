# Shared Disk

# Definition

All processors can directly access all disks via an interconnection network, but each processor has its own private memory

Notice that every Processor (P) has its own small Memory block (M) attached to it. However, they all share the same connection to the Disks on the right

![image.png](Shared%20Disk/image.png)

# Characteristics

- **Access:** Processors share disk but no RAM
- **Pros:**
    - **Fault Tolerance:** If a processor fails, other can take over since data is on shared disks
    - **Scalability:** Scales somewhat better than shared memory (memory bus is not the bottleneck)
- **Cons:** The bottleneck shifts to the interconnection to the disk subsystem; communication is slower than shared memory