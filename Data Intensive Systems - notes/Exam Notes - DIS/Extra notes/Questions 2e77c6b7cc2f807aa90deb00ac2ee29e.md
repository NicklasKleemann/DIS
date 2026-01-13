# Questions

# 📊 2. Big Data Characteristics (The “Vs”)

Big data is not just “large”. It is defined by several dimensions:

### Volume

How much data exists.

Modern systems deal with terabytes, petabytes, or more.

### Velocity

How fast data is produced and must be processed.

Examples:

- Stock trades
- Sensor streams
- User clicks

### Variety

Data is no longer just tables.

It includes:

- Text
- Images
- Video
- Logs
- JSON
- Graphs

### Veracity

Data is often noisy, incomplete, or incorrect.

A system must deal with uncertainty.

### Value

The goal is not storing data, but extracting useful information from it.

Some IT concepts (virtual machines, containers, etc.) are infrastructure tools, not data characteristics.

---

# 🌐 3. Distributed Systems and the CAP Theorem

In distributed databases, data is stored across many machines that communicate over a network.

Networks can fail.

Machines can crash.

Messages can be delayed.

This leads to the **CAP theorem**:

A distributed system can guarantee **only two** of the following three at the same time:

### Consistency

Every client sees the same data at the same time.

### Availability

Every request gets a response, even if some machines fail.

### Partition Tolerance

The system keeps working even when the network splits into disconnected parts.

Because network failures are unavoidable, modern systems must support **partition tolerance**.

That forces a trade-off between consistency and availability.

Relational databases usually choose consistency.

NoSQL systems often choose availability.

---

# 🧪 4. ACID vs BASE

Traditional databases are based on **ACID**:

| Property | Meaning |
| --- | --- |
| Atomicity | A transaction happens fully or not at all |
| Consistency | Database rules are always preserved |
| Isolation | Concurrent transactions do not interfere |
| Durability | Data is not lost after commit |

These are essential for:

- Banking
- Payments
- Inventory systems

NoSQL systems use **BASE**:

| Property | Meaning |
| --- | --- |
| Basically Available | The system always replies |
| Soft State | Data may change over time |
| Eventual Consistency | Data becomes consistent later |

This fits:

- Social networks
- Logs
- Click tracking
- Recommendation systems

Speed and availability are more important than perfect accuracy.

---

# 🗄️ 5. How Data Is Stored

Different workloads require different storage layouts.

### Row-oriented storage

Stores entire rows together.

Good for:

- Inserts
- Updates
- Reading complete records

Typical for transactional systems.

### Column-oriented storage

Stores columns together.

Good for:

- Aggregations
- Analytics
- Scanning only certain attributes

Typical for data warehouses.

### NoSQL storage models

- Key-value stores: fast lookups
- Document stores: flexible structure
- Wide-column stores: massive scale
- Graph databases: relationships

---

# 🧱 6. Partitioning and Distribution

Large datasets must be split across machines.

### Round-robin

Data is distributed evenly but without meaning.

### Hash partitioning

A hash function assigns each row to a node based on a key.

### Range partitioning

Data is split by value ranges.

Each method affects:

- Load balance
- Query performance
- Data locality

---

# 🧩 7. Shared-Nothing Architecture

In shared-nothing systems:

- Each node has its own CPU
- Its own memory
- Its own disk

Nodes do not share hardware.

This allows:

- Horizontal scaling
- Fault isolation
- Massive parallelism

---

# 🔗 8. Distributed Joins

When data is distributed, joins become expensive.

### Partitioned parallel join

Both tables are partitioned using the same join key.

Matching rows meet on the same node.

### Fragment-and-replicate join

A small table is copied to all nodes.

The large table is partitioned.

Each node joins locally.

The strategy depends on data size and distribution.

---

# 📑 9. Fragmentation and Transparency

Fragmentation means splitting data across sites.

- Horizontal: by rows
- Vertical: by columns

**Fragmentation transparency** means the user does not need to know where data is stored.

The system handles it automatically.

This simplifies queries and enables optimization.

---

# 🔁 10. Replication

Replication keeps multiple copies of data.

Benefits:

- Higher availability
- Faster reads
- Fault tolerance

Costs:

- More storage
- Harder updates
- Consistency challenges

---

# ⚡ 11. Performance Metrics

| Metric | Meaning |
| --- | --- |
| Latency | Time to serve one request |
| Response time | How long a query takes |
| Throughput | Operations per second |
| Availability | % of time system is up |

---

# 📈 12. Data Mining Foundations

Data mining extracts patterns from data.

Tasks include:

- Classification
- Clustering
- Association rules
- Outlier detection

---

# 🧮 13. Association Rule Mining

Used to find patterns like:

“People who buy A also buy B”

Key measures:

| Measure | Meaning |
| --- | --- |
| Support | How often a pattern occurs |
| Confidence | How often B occurs when A occurs |
| Lift | How strong the rule is compared to chance |

Apriori uses the fact that infrequent patterns cannot produce frequent supersets.

FP-Growth compresses data into a tree for efficiency.

---

# 🧠 14. Clustering

Clustering groups similar data.

Methods:

- K-means → centroid based
- Hierarchical → tree of clusters
- DBSCAN → density based
- Spectral → graph based

DBSCAN is good for irregular shapes and noise.

---

# 🤖 15. Classification

Supervised learning uses labeled data.

Examples:

- Spam detection
- Disease prediction

Evaluation metrics:

- Precision
- Recall
- F1-score

Accuracy is misleading when classes are imbalanced.

---

# 📊 16. Model Evaluation

Techniques:

- Train-test split
- k-fold cross-validation
- Leave-one-out
- Bootstrap

These estimate how well a model generalizes.

---

# 📏 17. Feature Scaling

Features with different units must be normalized.

Important for:

- KNN
- k-means
- SVM

---

# 🌐 18. Online vs Batch Learning

Some algorithms can update their model as new data arrives (online), instead of retraining from scratch (batch).