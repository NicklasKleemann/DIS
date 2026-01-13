# Question Lookup

# Data Intensive Systems

## Multiple Choice

**Which design principle ensures that a system can automatically add or remove resources according to workload changes?**

1. Reliability
2. **Elasticity (An elastic system can automatically adjust resources based on workload changes)**
3. Simplicity
4. Operability

**Which NoSQL data model is specifically designed to treat relationships as “first-class citizens” equally important to the data itself?**

1. Key-Value Store
2. Document Store
3. **Graph Database (Graph databases are designed to treat relationships between data as equally important to the data itself)**
4. Wide-Column Store

**In a Distributed Database, which type of fragmentation involves splitting the schema into smaller schemas that must contain a common key?**

1. Horizontal fragmentation
2. **Vertical fragmentation (Vertical fragmentation splits a relation by columns (attributes), and all resulting schemas must contain a common key for reconstruction)**
3. Hybrid fragmentation
4. Primary copy replication

**What is the primary function of a “standby namenode” in a Hadoop cluster?**

1. To store data blocks in parallel
2. **To act as a backup in case the primary namenode fails (single point of failure) (Because the namenode is a single point of failure, a warm standby is used for recovery)**
3. To execute map tasks on local data
4. To coordinate the “Shuffle and Spot”

**Which design principle allows a system to remain functional even when individual components (hardware or software) fail?**

1. Evolvability
2. **Reliability (Fault-tolerance) (A reliable system is resilient or fault-tolerant continuing to work correctly in the face of adversity)**
3. Simplicity
4. Scalability

**In a shared-nothing architecture, which of the following is true?**

1. All processors share a common disk subsystem
2. All processors share a common memory bus
3. **Each node has its own dedicated disk and memory (In shared-nothing, each processor has its own local memory and disk, communicating via an interconnection network)**
4. Communication between nodes is assumed to have zero cost

**What is the primary purpose of a “surrogate key” in a data warehouse dimension table?**

1. To provide a meaningful description of the data for end-users
2. **To avoid using information-bearing keys from source systems (like CPR numbers) and enable stable links to the fact table (Surrogate keys are meaningless integer keys that allow linking between dimension and fact tables, avoiding unstable or sensitive production codes from source systems)**
3. To reduce the number of rows in the fact table
4. To implement horizontal fragmentation

**Which type of spatial query identifies the single closest object in a dataset relative to a query point?**

1. Range query
2. Spatial selection
3. **Nearest Neighbor (NN) query (A nearest neighbor query finds the object in a relation $R$ that has the minimum distance to a query point $q$**
4. Spatial Join

**In a distributed transaction using the 2-Phase Commit (2PC) protocol, what happens if a participating site fails before responding to a “prepare” message?**

1. The coordinator waits indefinitely
2. The coordinator must decide to commit the transaction
3. **The coordinator must decide to abort the transaction (If the coordinator receives no response (due to failure), it assumes the participant is not ready and must abort the transaction)**
4. The transaction is automatically committed at all other sites

## Written Questions

**Explain the “2-Phase Commit (2PC)” protocol and its purpose in distributed transactions**

- The **2PC protocol** is used to ensure atomicity in distributed transactions across multiple sites. It consists of a **Prepare phase**, where the coordinator asks all participants to prepare for a commit, and a **Commit phase**, where the coordinator informs all participants of the final decision to either commit or abort. It is designed to handle various failures, though a coordinator failure can lead to a **blocking problem** where active sites must wait for recovery

**Describe the "Filter-Refinement" steps used in processing spatial queries**

- Because evaluating spatial relationships on exact geometries is slow, a two-step process is used
    1. **Filter Step:** The system approximates spatial objects using **Minimum Bounding Rectangles (MBRs)** and tests them against the query predicate. This is fast and prunes many objects
    2. **Refinement Step:** The **exact geometry** of the objects that passed the filter step (the candidates) is tested to find the actual results, removing any "false hits"

# Data Mining

## Multiple Choice

**In Association Rule Mining, which measure refers to the increase in the ratio of the sale of Y when X is sold?**

1. Support
2. Confidence
3. **Lift** **(Lift refers to the increase in the ratio of sale of Y when X is sold; a value $>1$ indicates a positive assoication**
4. Gini Index

**Which of the following is a “Lazy Learner” that waits until a new instance must be classified before performing significant processing?**

1. Decision Tree
2. **K-Nearest Neighbors (KNN) (KNN is a lazy learner because it simply stores training data as instances and waits until classification is requested to perform distance measurements)**
3. Random Forest
4. Naïve Bayes

**The “Elbow Method” is used in K-means clustering to determine the optimal value for:**

1. The distance threshold (Eps)
2. The minimum number of points (MinPts)
3. **The number of clusters (K) (The Elbow Method helps find the value of K after which the reduction in the Sum of Squared Errors (SSE) becomes insignificant)**
4. The random seed for initialization

## Written Questions

**Explain the “Apriori Principle” and how it is used to improve the efficiency of frequent itemset mining**

- The **Apriori Principle** states that if an itemset is frequent, all of its subsets must also be frequent; conversely, if an itemset is infrequent, all of its supersets must be infrequent. This allows the algorithm to perform **level-wise pruning**, where it uses frequent k-itemsets to explore $(k+1)$-itemsets, significantly reducing the number of candidate sets it needs to count in the database

**Define the “Silhouette Coefficient” and explain what it measures in the context of clustering**

- The **Silhouette Coefficient** is a clustering validation metric used to compare the **cohesion** (intra-cluster similarity) and **separation** (inter-cluster dissimilarity) of clusters. A higher score indicates that objects are well-matched to their own cluster and poorly matched to neighboring clusters. It is particularly useful when the ground truth of the dataset is unavailable