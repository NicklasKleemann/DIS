# Execution Framework

- Job Submission
- Task Scheduling
- Data & Code Co-location
- Shuffle and Sort
- Synchronization Barrier
- Error and Fault Handling
- Combiners and Partitioners

## Key Terms

| Term | Definition |
| --- | --- |
| Job | A MapReduce program consisting of mapper, reducer, (optional) combiner and partitioner code plus configuration. |
| JobTracker | The submission node in Hadoop that receives jobs and manages execution. |
| Task | A unit of work created from a job, either a map task or a reduce task. |
| Shuffle and Sort | The system phase that transfers intermediate key–value pairs and groups them by key. |
| Combiner | A mini-reducer that performs local aggregation before data is sent over the network. |
| Partitioner | A function that decides which reducer should receive each intermediate key. |
| Data locality | Running a task on the machine that already stores the needed data. |

---

## What the Execution Framework Does

The slides state that MapReduce **separates the “what” from the “how”**:

- The programmer writes **map** and **reduce**
- The execution framework handles:
    - Scheduling
    - Data movement
    - Synchronization
    - Fault handling
    - Parallelism

This is what makes MapReduce scalable and easy to use. 
4. Distributed Systems

---

## Step-by-Step: How a MapReduce Job Runs

### 1. Job Submission

The developer submits a job containing:

- Mapper code
- Reducer code
- Optional combiner and partitioner
- Configuration (input and output locations)

The job is sent to the **JobTracker** (submission node). 

---

### 2. Task Scheduling

The framework divides the job into **tasks**:

- **Map tasks** → based on splits of input key–value pairs
- **Reduce tasks** → based on partitions of the intermediate key space

Tasks are assigned to machines in the cluster.

Coordination is handled automatically. 

---

### 3. Data & Code Co-location

The scheduler tries to place tasks:

- On the machine that already stores the needed data
- If not possible, data is streamed over the network

The system prefers:

- Intra-rack communication over inter-rack communication
    
    because it is faster and cheaper. 
    

---

### 4. Shuffle and Sort

After all mappers finish:

- Their intermediate key–value pairs are copied across the network
- Pairs with the same key are grouped together
- Data is sorted by key

This is a **distributed “group by”** operation. 

---

### 5. Synchronization Barrier

Reduce cannot start until:

1. All mappers have finished
2. All intermediate data has been shuffled and sorted

This barrier ensures correctness but introduces waiting time. 

---

### 6. Reduce Phase

Each reducer:

- Receives all values for a given key
- Applies the reduce function
- Writes output to disk

Reducers also run in parallel. 

---

### 7. Error and Fault Handling

The execution framework operates in an environment where:

- Machines fail
- Disks crash
- Software bugs occur

The runtime:

- Detects failures
- Re-runs failed tasks on other machines
- Keeps the job running despite failures

This is essential because MapReduce runs on **low-end commodity servers**. 

---

## Combiners

A **combiner**:

- Runs on mapper nodes
- Performs local aggregation before Shuffle and Sort
- Reduces the amount of data sent over the network

It acts like a **mini-reducer**.

Example:

In WordCount, a combiner can sum word counts locally before sending them to reducers. 

---

## Partitioners

A **partitioner**:

- Decides which reducer gets which key
- Is used during Shuffle and Sort
- Uses hashing by default

Its job is to split the key space so reducers can work in parallel. 

---

## Why the Execution Framework Is Powerful

Because the system handles:

- Scheduling
- Data transfer
- Faults
- Synchronization

The programmer only focuses on:

- Writing map
- Writing reduce

This is the key reason MapReduce scales to thousands of machines.