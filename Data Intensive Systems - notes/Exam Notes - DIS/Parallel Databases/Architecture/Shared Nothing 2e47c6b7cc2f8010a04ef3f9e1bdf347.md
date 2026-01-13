# Shared Nothing

# Definition

Each node consists of a **processor, memory** and **disk**. Nodes communicate only via a high-speed network. This is the architecture used by most distributed databases and modern cluster systems

The system is broken into independent vertical “nodes”. Each node has its own P, M and Disk. They are only connected by the vertical line on the left (the network), meaning they share no physical hardware resources

![image.png](Shared%20Nothing/image.png)

# Characteristics

- **Structure:** Each node acts as a server for the data on its own disks
- **Pros:**
    - **Highly Scalable:** Can scale to thousands of processors because there is no resource sharing interference
    - **Local Access:** Data accessed locally doest not pass through the network
- **Cons:**
    - **Communication Cost:** High cost for non-local disk access
    - **Complexity:** Sending data requires software interaction at both ends