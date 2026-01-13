# Round-Robin Partitioning

# Definition

The system distributes tuples sequentially across disks in a strict order

- **Method:** Send the $i^{th}$ tuple to disk $i \text{ mod }n$ (where $n$ is the number of disks)

$t_1,t_2,t_3$ are spread across Disk 0, 1 and 2 respectively, followed by $t_4, t_5, t_6$ repeating the pattern. This ensures the volume of data is perfectly even.

![image.png](Round-Robin%20Partitioning/image.png)

---

# Characteristics

- **Pros:**
    - **Perfect Load Balancing:** All disks have almost an equal number of tuples
    - **Sequential Scan:** Best suited for scanning the *entire* relation, as all disk can work in parallel at full speed
- **Cons:**
    - **No Clustering:** Tuples are scattered randomly regarding their content
    - **Inefficient Search:** Difficult to answer range or point queries because the system does not know where specific values are; it must search **all** disks ($n$ disks searched)
- **When to choose this strategy:** You should pick Round-Robin when your primary workload involves **Sequential Scans** of the entire relation
- **Why?**
    - **Condition:** You need to guarantee **Perfect Load Balancing.** Because data is cyclical distributed one-by-one, every disk has almost exactly the same number of tuples
    - **Trade-off:** You **cannot** frequently perform **Point Queries** (specific value lookups) or **Range Queries**. Since the data is scattered randomly without semantic logic, the system must search **all** disks for every query, which is inefficient for specific lookups