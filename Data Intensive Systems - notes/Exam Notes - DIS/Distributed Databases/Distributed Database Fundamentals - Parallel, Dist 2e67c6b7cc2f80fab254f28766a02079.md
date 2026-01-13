# Distributed Database Fundamentals - Parallel, Distributed, Heterogeneous and Homogeneous

This section covers the foundational concepts of distributed databases: what they are, how they differ from parallel databases, and the key architectural choices.

## Topics

| Topic | Key Question |
| --- | --- |
| Parallel vs Distributed | Why does the cost model change with distance? |
| DDBS Characteristics | What makes a database "distributed"? |
| Homogeneous vs Heterogeneous | What happens when sites use different software? |

### **Core Principle**

A distributed database system consists of **loosely coupled sites** that share no physical components. The sites are independent but cooperate to serve queries and transactions.

---

## **Page: Parallel vs Distributed Databases**

These are **not** the same thing, even though both involve multiple machines.

| Aspect | Parallel Database | Distributed Database |
| --- | --- | --- |
| **Physical Location** | Same data center, often same rack | Geographically dispersed (different cities, continents) |
| **Network** | High-speed LAN (10+ Gbps), near-zero latency | Public internet, WAN—high latency, variable bandwidth |
| **Communication Cost** | Negligible—ignored in cost models | *Critical*—often the dominant cost factor |
| **Primary Goal** | Raw performance via parallelism | Availability, geographic locality, organizational autonomy |
| **Typical Architecture** | Shared-memory, shared-disk, or shared-nothing | Almost always shared-nothing |

**Why this matters:** The cost model changes everything. In parallel systems, you optimize for CPU and disk I/O. In distributed systems, you obsess over *network transfers*—moving data is expensive.

---

## **Page: Distributed Database Systems**

### **Definition**

A distributed database system consists of **loosely coupled sites** that share no physical components. Database systems that run on different sites are independent of each other, but transactions and queries may access data at one or more sites.

### **Key Characteristics**

- **No shared physical components:** Each site has its own CPU, memory, and storage
- **Logical cooperation:** Sites agree to participate in a unified system
- **Local autonomy:** Each site can process local transactions independently
- **Global coordination:** Cross-site transactions require cooperation

### **Why Distribute Data?**

| Reason | Explanation |
| --- | --- |
| **Locality** | Store data near where it's used (e.g., European customers in EU data center) |
| **Availability** | If one site fails, others keep running |
| **Scalability** | Add capacity by adding sites, not upgrading one machine |
| **Organizational** | Different departments/companies maintain their own data |

---

## **Page: Heterogeneous and Homogeneous Databases**

### **Homogeneous Distributed Databases**

**Definition:** All sites run the *same* DBMS software with *identical* schemas.

**Characteristics:**

- Sites are fully aware of each other
- Appears as a single logical database to users
- Sites surrender some autonomy for seamless integration
- Query optimization can leverage global knowledge

**Example:** A company with Oracle databases in New York, London, and Tokyo—all with the same table structures.

### **Heterogeneous Distributed Databases**

**Definition:** Sites run *different* DBMS software and/or have *different* schemas.

Think of this as database integration rather than database distribution.

**Challenges:**

| Challenge | Why It's Hard |
| --- | --- |
| **Schema matching** | `Customer.name` in System A might be `client.full_name` in System B |
| **Data type differences** | Date formats, character encodings, numeric precision vary |
| **Query translation** | SQL dialects differ; some systems may not even be SQL-based |
| **Transaction coordination** | Not all systems support the same commit protocols |

**Solution approaches:**

- **Middleware/Mediators:** Translation layers that map between schemas
- **Federated databases:** Each system retains autonomy; a global layer handles integration