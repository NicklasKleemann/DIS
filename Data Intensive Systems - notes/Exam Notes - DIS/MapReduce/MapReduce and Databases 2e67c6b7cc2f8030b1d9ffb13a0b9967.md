# MapReduce and Databases

- Hadoop vs Databases
- MapReduce vs Parallel Databases
- Schema and Indexing
- Programming Model
- Fault Tolerance
- Hybrid Systems

## Key Terms

| Term | Definition |
| --- | --- |
| Hadoop | An open-source framework for large-scale data processing based on MapReduce and HDFS. |
| Relational Database (RDBMS) | A database system designed for structured data using tables and schemas. |
| Parallel Database | A relational database system that runs on multiple machines to execute queries in parallel. |
| Schema | The predefined structure of data in a database. |
| Index | A data structure used by databases to speed up data access. |
| Hybrid System | A system that combines Hadoop and databases to get benefits of both. |

---

## Hadoop vs Databases

The slides clearly state:

> Hadoop is not a relational database system.
> 

### Data Type

- **Hadoop**
    
    Works well with both **structured and unstructured data**.
    
- **Databases**
    
    Designed mainly for **structured data**.
    

### Scalability

- **Databases**
    
    Work best for **constant and predictable workloads**.
    
- **Hadoop**
    
    Works better when data volume keeps increasing.
    

### Cost

- **Hadoop**
    
    Uses **low-end commodity machines** and open-source software → cheaper.
    
- **Databases**
    
    Typically require expensive hardware and licenses.
    

### Speed

- **Databases**
    
    Better for **time-sensitive queries**.
    
- **Hadoop**
    
    Better for **large-scale batch analytics**. 
    

---

## MapReduce vs Parallel Databases

### Schema

| Parallel Database | MapReduce |
| --- | --- |
| Data must fit a schema | No schema required |
| Data is parsed at load time | Data must be parsed by the programmer |
| Constraints are enforced | Programmer must check constraints |
| Helps compression and optimization | More flexible, but slower |

Schemas help databases optimize queries, but reduce flexibility.

MapReduce is flexible but shifts work to the programmer. 

---

### Indexing

| Parallel Database | MapReduce |
| --- | --- |
| Built-in indexes | No built-in indexes |

Databases can quickly locate records using indexes.

MapReduce must scan data unless the user builds something manually. 
4. Distributed Systems

---

### Programming Model

| Parallel Database | MapReduce |
| --- | --- |
| SQL (declarative) | MapReduce (declarative overall, imperative inside functions) |
| User specifies what they want | User writes how to process data |
| Easy to maintain | Harder to maintain |

MapReduce is easier to start with but harder to manage long-term. 
4. Distributed Systems

---

### Fault Tolerance

| Parallel Database | MapReduce |
| --- | --- |
| Must restart entire query if failure occurs | Only re-computes failed tasks |
| Runs on fewer, reliable machines | Runs on many unreliable machines |

MapReduce handles failures better, but is slower and needs more machines. 

---

## Hybrid Systems

The slides conclude that:

- Hadoop is good for large-scale, growing data
- Databases are good for fast and structured queries

So it is useful to build **hybrid systems** that:

- Use Hadoop for big data processing
- Use databases for fast querying

There is **no one-size-fits-all solution**.

The choice depends on data and workload. 

---

## Final Conclusion from the Slides

> MapReduce is one of the most successful abstractions for large-scale computing, but it is not perfect.
> 

Some problems are easier with MapReduce, others with databases.

The right tool depends on:

- Data size
- Data structure
- Workload type