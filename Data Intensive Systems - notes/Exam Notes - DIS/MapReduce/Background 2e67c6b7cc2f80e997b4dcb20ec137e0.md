# Background

- Scale-up vs Scale-out
- Definition of Scalability
- Vertical Scaling (Scale-up)
- Horizontal Scaling (Scale-out)
- Programming Challenges in Parallel & Distributed Systems

### **Scalability in Computation**

- Demand for Efficiency
- Adding Capacity to Infrastructure
- Performance Bottlenecks
- Long-term vs Flexible Scaling
- Commodity Machines and Clusters

### **Big Ideas behind MapReduce**

- Scale-out, Not Scale-up
- Commodity Hardware
- Fault Tolerance
- Moving Computation to Data
- Sequential Processing
- Hiding System-Level Details
- Seamless Scalability

# Background – MapReduce

## Key Terms

| Term | Definition |
| --- | --- |
| Scalability | A system’s ability to increase or decrease computing, storage, or networking power to handle changing workloads. In data systems, it means processing more data, possibly faster. |
| Scale-up (Vertical Scaling) | Increasing the power of a single machine by adding better CPUs, more RAM, or larger disks. |
| Scale-out (Horizontal Scaling) | Increasing capacity by adding more computers and distributing the workload across them. |
| Commodity Machines | Low-end, inexpensive servers used in large numbers instead of a few powerful machines. |
| Fault Tolerance | The ability of a system to keep working even when some machines fail. |
| Moving computation to data | Executing programs where the data is stored instead of transferring large data sets over the network. |

---

## Why Scalability Is Needed

The slides state that **demand for efficiency is the driving force** behind scalability. As data grows, a system must be able to handle:

- More data
- Faster processing
- More users

Scalability means **adding capacity to the infrastructure** so that the system can keep working efficiently when data or workload increases.

---

## Step-by-Step: How Systems Become Scalable

### Step 1 – Detect a bottleneck

A system becomes slow because of:

- Limited CPU
- Limited memory
- Limited I/O
    
    This increases latency and causes performance bottlenecks.
    

### Step 2 – Decide how to add capacity

You can either:

- Add more power to one machine (scale-up), or
- Add more machines (scale-out).

---

## Scale-Up (Vertical Scaling)

### What it is

Scale-up means improving one machine by adding:

- Faster CPUs
- More RAM
- Larger disks

### When to use it

According to the slides:

- When there is a performance bottleneck
- When current hardware cannot be optimized further

### Advantages

- Faster processing (e.g., dual processors, faster memory)
- Simple architecture (no new machines)
- Cheaper than buying many machines
- Lower energy use

### Disadvantages

- Latency still exists
- Risk when upgrading
- Hardware becomes outdated

---

## Scale-Out (Horizontal Scaling)

### What it is

Scale-out means adding more computers and forming a **cluster** so work is shared.

### When to use it

- When long-term growth is expected
- When flexibility is needed
- When storage and processing must be distributed

### Advantages

- Can use newer machines
- Easy to adapt to demand
- Cost-effective: uses low-end commodity servers

### Disadvantages

- Needs physical rack space
- Higher operational costs
- Higher initial setup cost

---

## Programming Challenges in Distributed Systems

The slides emphasize that programming for distributed systems is **very difficult** because of:

- Race conditions
- Deadlocks
- Coordination between machines

Programmers spend too much time handling:

- Networking
- Failures
- Synchronization

Instead of solving the real problem.

### The ideal situation

A good system should:

- Hide system-level details
- Automatically scale with data
- Run twice as slow when data doubles
- Run in the same time if both data and cluster size double

---

## Scalability in Computation

Scalability in computing means:

- Being able to add infrastructure when needed
- Avoiding performance bottlenecks
- Using clusters of machines rather than one big server

The slides show that modern systems prefer **commodity machines and clusters** instead of expensive servers.

---

## Big Ideas Behind MapReduce

MapReduce was designed to solve these scalability problems.

### Core principles

1. **Scale-out, not scale-up**
    
    Use many small machines instead of one powerful one.
    
2. **Use commodity hardware**
    
    Low-end machines are cheaper and easier to replace.
    
3. **Fault tolerance**
    
    Failures are assumed to be common, so the system is built to survive them.
    
4. **Move computation to the data**
    
    Instead of sending large data over the network, programs run where the data is stored.
    
5. **Sequential processing**
    
    Data is processed in large blocks sequentially to avoid slow random disk access.
    
6. **Hide system-level details**
    
    Programmers do not need to manage networking, failures, or scheduling.
    
7. **Seamless scalability**
    
    The same program can run on small or very large clusters without changes.
    

---

## Why This Leads to MapReduce

From the slides, the goal is clear:

> Build a system that lets programmers focus on logic, while the system automatically handles:
> 
- Parallelism
- Failures
- Data movement
- Scaling

This is exactly what **MapReduce** provides.