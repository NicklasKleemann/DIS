# Shared Memory

# Definition

Processors and disks share a common memory, typically connected via a high-speed bus.

Observe how all Processors (P) and Disks are connected to single large Memory block (M) via a central bus line. This illustrates why the bus becomes a bottleneck

![image.png](Shared%20Memory/image.png)

---

# Characteristics

- **Access**: Any processor can access data in the shared memory without software overhead
- **Pros:** Extremely efficient communication between processors
- **Cons: Not scalable** beyond 32 or 64 processors because the bus becomes a bottleneck
- **Usage:** Common for lower degrees of parallelism