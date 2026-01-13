# Software Implementation

- Distributed File System (DFS)
- Google File System (GFS)
- Hadoop Distributed File System (HDFS)
- HDFS Architecture
- Replication and Immutability
- Hadoop Cluster Architecture
- MapReduce on Hadoop
- Execution Overview

## Key Terms

| Term | Definition |
| --- | --- |
| DFS | A Distributed File System that stores data across many machines and brings computation computation close to data. |
| GFS | Google File System, Google’s distributed file system used by MapReduce. |
| HDFS | Hadoop Distributed File System, the open-source version inspired by GFS. |
| NameNode | The master node that manages metadata in HDFS. |
| DataNode | A slave node that stores actual data blocks. |
| Block | A large chunk of a file stored in HDFS. |
| Replica | A copy of a data block stored on another machine for reliability. |

---

## Why MapReduce Needs a Distributed File System

The slides explain that traditional clusters keep:

- Storage and computation separate

DFS changes this by:

- Storing data on the same machines that perform computation
- Reducing network transfer
- Improving performance 4. Distributed Systems

DFS divides files into **large blocks** and distributes and replicates them across the cluster.

---

## Google File System (GFS) and HDFS

MapReduce was designed to work on top of **Google File System (GFS)**.

Hadoop uses **HDFS**, which is based on GFS.

Both systems:

- Use large blocks
- Replicate data
- Use a master–slave design 4. Distributed Systems

---

## HDFS Architecture

HDFS has:

### One Master

**NameNode**

- Stores metadata
- Directory structure
- File-to-block mapping
- Block locations
- Access permissions

**Secondary NameNode**

- Helps maintain the NameNode state

### Many Slaves

**DataNodes**

- Store actual data blocks on local disks
- Map block IDs to physical disk locations
- Send data directly to clients

Important:

**Data never goes through the NameNode — only metadata does.** 

---

## Step-by-Step: How a Client Reads a File

1. Client asks NameNode for block locations
2. NameNode returns which DataNodes store the blocks
3. Client reads blocks directly from DataNodes

This avoids overloading the NameNode. 

---

## Replication and Immutability

HDFS uses:

- **Three replicas per block by default**
- Replicas are placed on different racks

This provides:

- Reliability
- Availability
- Performance

Files are:

- **Write Once, Read Many (WORM)**
- They can only be appended, not modified

This simplifies consistency and fault handling. 

---

## NameNode Responsibilities

The NameNode:

- Manages the namespace
- Coordinates file operations
- Monitors the health of the file system

Because it is a **single point of failure**, a warm standby NameNode is used. 

---

## Hadoop Cluster Architecture

The cluster contains:

### Master Nodes

- NameNode (HDFS)
- JobTracker (MapReduce)

### Slave Nodes

- DataNode (storage)
- TaskTracker (computation)

These can be on the same machine in small clusters. 

---

## MapReduce on Hadoop

Hadoop has two layers:

- **HDFS layer** → stores data
- **MapReduce layer** → runs computation

MapReduce tasks are scheduled on the same machines that store the data blocks.

This implements **moving computation to data**. 

---

## Execution Overview (High Level)

The slides show the following process:

1. User program submits a job
2. Master assigns map and reduce tasks
3. Workers read input splits
4. Mappers write intermediate data locally
5. Reducers read intermediate data remotely
6. Reducers write final output files

Files can be local or distributed. 

---

## Why This Design Works

HDFS and MapReduce together provide:

- Fault tolerance
- Data locality
- Scalability
- Low cost using commodity machines

This combination is what made Hadoop and MapReduce successful for big data.