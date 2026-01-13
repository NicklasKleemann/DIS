## Definitions

| Term | Definition |
| --- | --- |
| **Data-Intensive Application** | Applications where the primary challenge is the quantity, complexity, or speed of data change, rather than CPU cycles.

 |
| **Reliability** | The system's ability to continue working correctly even when facing adversity (faults).

 |
| **Scalability** | The ability of a system to cope with increased load.

 |
| **Maintainability** | The ease with which a system can be modified, adapted, or fixed by engineering teams.

 |
| **Latency** | The duration a request waits to be handled (network and queuing delay).

 |
| **Response Time** | The total time elapsed between a client sending a request and receiving a response (Latency + Processing Time).

 |
| **Throughput** | The number of operations processed per second, typically used as a metric for batch processing.

 |
| **ACID** | A set of properties (Atomicity, Consistency, Isolation, Durability) provided by relational databases to guarantee valid transactions.

 |
| **BASE** | An alternative consistency model for NoSQL (Basically Available, Soft-state, Eventually consistent) favoring availability over strict consistency.

 |
| **CAP Theorem** | The theorem stating a distributed data system can simultaneously provide only two of three guarantees: Consistency, Availability, and Partition Tolerance.

 |
| **ORM (Object-Relational Mapping)** | A translation layer used to map objects in application code to rows and columns in relational tables.

 |

## System Goals

| Goal/Concept | Objective |
| --- | --- |
| **Scalability** | To handle growth in data volume or user traffic by either adding resources (vertical) or adding nodes (horizontal).

 |
| **Reliability** | To remain fault-tolerant and resilient against hardware, software, and human errors, ensuring minimal downtime.

 |
| **Operability** | To make it easy for operations teams to keep the system running smoothly through monitoring and automation.

 |
| **Simplicity** | To reduce accidental complexity and make the system easier for new engineers to understand, often via abstraction.

 |
| **Evolvability** | To allow engineers to easily make changes to the system as requirements or technologies shift (Agility).

 |

---

## 1. Introduction to Data Systems

### Data-Intensive vs. Compute-Intensive

Modern applications are increasingly **data-intensive**, meaning their primary bottleneck is the volume, complexity (variety/veracity), and speed (velocity) of data. This contrasts with traditional **compute-intensive** applications where CPU cycles were the limiting factor.

The "5Vs" of Big Data characterize these systems:

* Volume
* Variety
* Veracity
* Velocity
* Value.



> **Real World Examples of Data Sources:**
> * **Internet Companies:** Google, Facebook, LinkedIn (Social graphs, user activity).
> * **Online Business:** Amazon, eBay (Transaction logs, inventory).
> * **IoT:** Weather monitoring, smart transportation.
> * **Traditional Business:** Banks (Danske Bank), Airlines (SAS) digitizing operations.
> 
> 

### Components of a Data System

A "data system" is rarely a single tool. It is often a composition of various building blocks stitched together via APIs in application code.

Common building blocks include:

* 
**Persistent Storage:** Databases.


* 
**Cache:** Reuse of expensive operation results (e.g., In-memory cache).


* 
**Indexes:** Efficient data search (e.g., Full-text index).


* 
**Stream Processing:** Asynchronous message handling.


* 
**Batch Processing:** Periodic handling of accumulated data.



---

## 2. Design Principles

### Reliability

The goal is to be **fault-tolerant** (resilient), not necessarily fault-free. The system must cure faults to prevent total system failure.

* **Hardware Faults:** Random and independent (e.g., disk failure).
* **Software Errors:** Systemic, harder to predict (e.g., cascading failures).
* **Human Errors:** Configuration mistakes (the leading cause of outages).

**Design Strategies for Reliability:**

* Decoupling and sandboxing.


* Thorough automated testing at all levels.


* Clear monitoring to detect issues early.



### Scalability

Scalability is not a static property but a response to increased load parameters.

#### Reasoning Chain: Measuring Performance Under Load

* **The Problem:** Simply saying "the system is slow" is imprecise. We need to know how performance degrades as specific load parameters increase.
* **The Approach:** Define load parameters specific to the domain:
* 
*Web Server:* Requests per second.


* 
*Database:* Read/Write ratio.


* 
*Chatroom:* Concurrent users.




* 
**The Metric:** Measure the resource increase required to maintain performance, OR the performance degradation if resources remain constant.


* 
*Online Systems:* Focus on **Response Time** (Client view) and **Latency** (Service view).


* 
*Batch Systems:* Focus on **Throughput** (Operations per second).





#### Scaling Strategies

| Strategy | Description | Implication |
| --- | --- | --- |
| **Scale-Up (Vertical)** | Adding more power (CPU, RAM) to a single machine.

 | Simpler architecture but expensive and limited by hardware caps. |
| **Scale-Out (Horizontal)** | Adding more machines to a cluster.

 | Complex to manage (requires distributed system logic) but theoretically unlimited growth. |
| **Elastic Scaling** | Automatically adding/removing resources based on workload.

 | Optimizes cost and performance dynamically. |

### Maintainability

Maintenance is often the most painful part of the software lifecycle. Good design minimizes this pain through three sub-principles:

1. 
**Operability:** Visibility and control for admins (monitoring, automation, self-healing).


2. **Simplicity:** Managing complexity via **abstraction**. Removing "accidental complexity" (complexity not inherent to the problem).


3. 
**Evolvability:** Facilitating agile changes (refactoring) as requirements shift.



---

## 3. Architecture Evolution

### Evolution of Deployment

1. 
**Mainframe Era:** Centralized computing.


2. 
**PC Era:** Client/Server model, desktop applications.


3. 
**Web Era:** Browser clients, application servers, and databases over the internet.


4. **Cloud Era:**
* 
**VM:** Virtual Machines deployed on cloud infrastructure.


* 
**DBaaS:** Database-as-a-Service, where the provider manages scaling and maintenance (e.g., AWS RDS, MongoDB Atlas).





### Parallel & Distributed Systems

* 
**Shared Memory:** Processors share RAM (Scale-up).


* 
**Shared Disk:** Independent processors share storage.


* 
**Shared Nothing:** Independent nodes connected via network (Scale-out/Distributed). This is the basis for modern distributed data systems.



---

## 4. Relational Databases (RDBMS)

Relational databases organize data into **relations** (tables) defined by a strict **schema** (columns/types).

### Storage Models

There are two primary ways to store relational data on disk:

| Storage Type | Mechanism | Best Use Case | Pros/Cons |
| --- | --- | --- | --- |
| **Row-Oriented** | Stores all data for one record contiguously.

 | Transactional workloads (CRUD) where full records are accessed.

 | <br>**Pros:** Fast writes/updates for single entities.<br>

<br>**Cons:** Slow for analytics; reads unnecessary data if only specific columns are needed.

 |
| **Column-Oriented** | Stores all data for one column contiguously.

 | Analytical queries (OLAP), e.g., `SELECT *` or aggregates.

 | <br>**Pros:** Only reads relevant data; efficient compression.<br>

<br>**Cons:** Updates to single records are slow (requires multiple I/O).

 |

### The Object-Relational Impedance Mismatch

* 
**The Problem:** Application code typically uses Object-Oriented Programming (OOP) with rich structures (nesting, inheritance), while RDBMS uses flat tables.


* **The Friction:** Developers need a translation layer to convert objects to rows.
* 
**The Solution:** **ORM (Object-Relational Mapping)** frameworks (e.g., Hibernate) handle this translation, though they can introduce performance overhead or complexity.



---

## 5. NoSQL Databases

NoSQL databases emerged to solve problems RDBMS struggled with: massive scalability (Web 2.0), unstructured data, and the impedance mismatch.

### CAP Theorem

In a distributed system, you can only guarantee two of the three:

1. 
**Consistency (C):** Every read receives the most recent write or an error.


2. 
**Availability (A):** Every request receives a response (even if data is stale).


3. 
**Partition Tolerance (P):** System operates despite network failures between nodes.


* 
Note: In distributed systems, P is usually mandatory, forcing a choice between CP and AP.





### ACID vs. BASE

| Feature | Relational (ACID) | NoSQL (BASE) |
| --- | --- | --- |
| **Philosophy** | Consistency over Availability.

 | Availability over Consistency.

 |
| **Guarantees** | **A**tomicity<br>

<br>**C**onsistency<br>

<br>**I**solation<br>

<br>**D**urability | <br>**B**asically **A**vailable<br>

<br>**S**oft-state<br>

<br>**E**ventually consistent.

 |
| **Transaction** | Strict commit/rollback.

 | Writes may not be immediately persistent or consistent. |

### Types of NoSQL Systems

#### 1. Key-Value Stores

* **Data Model:** Associative array (Map/Dictionary). Keys are unique strings; values can be anything (text, image, JSON).


* 
**Pros:** Fast, simple, highly scalable for distributed systems.


* 
**Cons:** No complex queries (filters), no joins, no foreign keys.


* 
**Use Cases:** Session management, user profiles, caching (e.g., Redis, DynamoDB).



#### 2. Document Stores

* 
**Data Model:** Stores data in encoded formats like JSON, XML, or BSON.


* **Structure:** Documents are grouped into **Collections** (similar to tables). Unlike RDBMS, documents in a collection do not need a uniform schema.


* **Comparison:**
* RDBMS: Table  Row  Column.
* Document DB: Collection  Document  Field.




* 
**Use Cases:** Content management, catalogs (e.g., MongoDB).



#### 3. Graph Databases

* 
**Data Model:** Defined as  where  are nodes (entities) and  are edges (relationships).


* 
**Core Philosophy:** Relationships are as important as the data itself.


* **Models:**
* 
*Property Graph:* Nodes and edges have internal properties (key-value pairs) (e.g., Neo4j).


* 
*Triple-Store:* Data stored as `(Subject, Predicate, Object)` statements (e.g., RDF, SPARQL).




* 
**Pros:** High performance for traversing deep relationships (social networks, recommendation engines).


* 
**Cons:** Difficult to scale (partitioning a graph is hard), lack of standard languages.



---

## 6. Summary Comparison: Which to Choose?

| Factor | Relational (SQL) | Key-Value | Document | Graph |
| --- | --- | --- | --- | --- |
| **Structure** | Structured (Schema) | Unstructured | Semi-structured | Connected |
| **Scaling** | Vertical (mostly) | Horizontal | Horizontal | Vertical (mostly) |
| **Relationships** | Joins (Expensive) | None (App side) | Embedded/Ref | Native (Fast) |
| **Best For** | Financial systems, legacy apps, strict data integrity. | Caching, sessions, shopping carts. | CMS, catalogs, flexible data. | Social networks, fraud detection, routing. |