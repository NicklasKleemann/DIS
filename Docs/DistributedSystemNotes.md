# Distributed Databases

> **Core Insight:** A distributed database is essentially a database that lives across multiple computers. The fundamental challenge is making this collection of machines *appear* as a single, coherent system—while dealing with the reality that networks are slow, unreliable, and machines fail independently.

---

# 📖 Key Definitions

| Term | Definition |
| :--- | :--- |
| **Distributed Database System (DDBS)** | A collection of logically related databases spread across a network. Sites are *loosely coupled*—they share no physical components but cooperate to serve queries. |
| **Homogeneous DDBS** | All sites run identical DBMS software and share the same schema. Simplest to manage—looks like one big database. |
| **Heterogeneous DDBS** | Sites run different DBMS software and/or have different schemas. Think: integrating Oracle, MySQL, and PostgreSQL. Requires translation layers. |
| **Replication** | Storing copies of the same data at multiple sites. Improves availability and read performance, but complicates writes. |
| **Fragmentation** | Splitting a table into pieces stored at different sites. Each piece is called a *fragment*. |
| **Transparency** | Hiding complexity from users. They shouldn't need to know *where* data lives, *how* it's split, or *whether* copies exist. |
| **Semijoin** | A join optimization: $r_1 \ltimes r_2 = \Pi_{R_1}(r_1 \bowtie r_2)$. Ships only join keys first, then fetches only matching rows. |
| **Transaction Coordinator (TC)** | The site that initiates a distributed transaction and orchestrates the commit/abort decision across all participants. |
| **Transaction Manager (TM)** | Local role at each site—maintains log, handles recovery, manages local locks, processes subtransactions. |
| **Two-Phase Commit (2PC)** | A protocol ensuring atomicity across sites: first get everyone to *promise* they can commit (Phase 1), then tell everyone the final decision (Phase 2). |
| **Fail-Stop Model** | Assumption that failed sites simply stop working and don't cause harm (no incorrect messages sent). |

---

# 📂 Introduction

This section covers the foundational concepts of distributed databases: what they are, how they differ from parallel databases, and the key architectural choices.

### What You'll Learn

| Topic | Key Question |
|:------|:-------------|
| Parallel vs Distributed | Why does the cost model change with distance? |
| DDBS Characteristics | What makes a database "distributed"? |
| Homogeneous vs Heterogeneous | What happens when sites use different software? |

### Core Principle

A distributed database system consists of **loosely coupled sites** that share no physical components. The sites are independent but cooperate to serve queries and transactions.

---

## Page: Parallel vs Distributed Databases

These are **not** the same thing, even though both involve multiple machines.

| Aspect | Parallel Database | Distributed Database |
|:-------|:------------------|:---------------------|
| **Physical Location** | Same data center, often same rack | Geographically dispersed (different cities, continents) |
| **Network** | High-speed LAN (10+ Gbps), near-zero latency | Public internet, WAN—high latency, variable bandwidth |
| **Communication Cost** | Negligible—ignored in cost models | *Critical*—often the dominant cost factor |
| **Primary Goal** | Raw performance via parallelism | Availability, geographic locality, organizational autonomy |
| **Typical Architecture** | Shared-memory, shared-disk, or shared-nothing | Almost always shared-nothing |

**Why this matters:** The cost model changes everything. In parallel systems, you optimize for CPU and disk I/O. In distributed systems, you obsess over *network transfers*—moving data is expensive.

---

## Page: Distributed Database Systems

### Definition

A distributed database system consists of **loosely coupled sites** that share no physical components. Database systems that run on different sites are independent of each other, but transactions and queries may access data at one or more sites.

### Key Characteristics

- **No shared physical components:** Each site has its own CPU, memory, and storage
- **Logical cooperation:** Sites agree to participate in a unified system
- **Local autonomy:** Each site can process local transactions independently
- **Global coordination:** Cross-site transactions require cooperation

### Why Distribute Data?

| Reason | Explanation |
|:-------|:------------|
| **Locality** | Store data near where it's used (e.g., European customers in EU data center) |
| **Availability** | If one site fails, others keep running |
| **Scalability** | Add capacity by adding sites, not upgrading one machine |
| **Organizational** | Different departments/companies maintain their own data |

---

## Page: Heterogeneous and Homogeneous Databases

### Homogeneous Distributed Databases

**Definition:** All sites run the *same* DBMS software with *identical* schemas.

**Characteristics:**
- Sites are fully aware of each other
- Appears as a single logical database to users
- Sites surrender some autonomy for seamless integration
- Query optimization can leverage global knowledge

**Example:** A company with Oracle databases in New York, London, and Tokyo—all with the same table structures.

### Heterogeneous Distributed Databases

**Definition:** Sites run *different* DBMS software and/or have *different* schemas.

Think of this as database integration rather than database distribution.

**Challenges:**

| Challenge | Why It's Hard |
|:----------|:--------------|
| **Schema matching** | `Customer.name` in System A might be `client.full_name` in System B |
| **Data type differences** | Date formats, character encodings, numeric precision vary |
| **Query translation** | SQL dialects differ; some systems may not even be SQL-based |
| **Transaction coordination** | Not all systems support the same commit protocols |

**Solution approaches:**
- **Middleware/Mediators:** Translation layers that map between schemas
- **Federated databases:** Each system retains autonomy; a global layer handles integration

---

# 📂 Distributed Data Storage

This section addresses the fundamental question: *Where should data physically live?*

### Distributed Database Design

How should the database and applications on top of it be placed **across the sites**? We assume the relational data model, but the techniques can be applied to others.

### Two Orthogonal Strategies

| Strategy | Description | Key Trade-off |
|:---------|:------------|:--------------|
| **Replication** | Maintain multiple copies of data at different sites | Read performance vs. write complexity |
| **Fragmentation** | Partition a relation into fragments stored at distinct sites | Locality vs. reconstruction cost |

**These can be combined:** A relation is partitioned into several fragments, and the system maintains several identical replicas of each fragment.

---

## Page: Replication

### Definition

A relation or fragment of a relation is **replicated** if it is stored redundantly in two or more sites.

### Replication Spectrum

| Level | Description |
|:------|:------------|
| **No replication** | Each data item exists at exactly one site |
| **Partial replication** | Some data is replicated, some isn't (most common) |
| **Full replication** | A relation is stored at *all* sites |
| **Fully redundant database** | Every site contains a copy of the *entire* database |

### Advantages of Replication

| Advantage | Explanation |
|:----------|:------------|
| **Availability** | Failure of a site containing relation $r$ does not result in unavailability of $r$ if replicas exist |
| **Parallelism** | Queries on $r$ may be processed by several sites in parallel |
| **Reduced data transfer** | Relation $r$ is available locally at each site that has a replica |

### Disadvantages of Replication

| Disadvantage | Explanation |
|:-------------|:------------|
| **Increased update cost** | Each replica of relation $r$ must be updated |
| **Concurrency complexity** | Concurrent updates to distinct replicas may lead to inconsistent data unless special mechanisms are implemented |

**Example problem:** Consider money transfer between replicates on different sites—both might think they have the correct balance.

### Primary Copy Strategy

One solution for handling concurrent updates:

1. Choose one copy as the **primary copy**
2. Apply concurrency control operations on the primary copy only
3. Propagate changes to replicas

**Trade-off:** Simplifies concurrency control but creates a single point of failure for writes.

---

## Page: Fragmentation

### Definition

A relation $r$ is partitioned into fragments $r_1, r_2, ..., r_n$ which contain **sufficient information to reconstruct** the original relation $r$.

### Horizontal Fragmentation

**What:** Each *tuple* (row) of $r$ is assigned to one or more fragments based on a selection predicate.

**How:** Apply selection conditions to assign rows to fragments.

**Example:**
```
Original: account(branch_name, account_number, balance)

Fragment 1: σ(branch_name = "Hillside")(account)
Fragment 2: σ(branch_name = "Valleyview")(account)
```

| branch_name | account_number | balance |
|:------------|:---------------|:--------|
| Hillside | A-305 | 500 |
| Hillside | A-226 | 336 |
| Hillside | A-155 | 62 |

$$account_1 = \sigma_{branch\_name = "Hillside"}(account)$$

**Reconstruction:** $account = account_1 \cup account_2$

### Vertical Fragmentation

**What:** The *schema* for relation $r$ is split into several smaller schemas. Each fragment contains a subset of attributes.

**Example:**
```
Original: employee(branch_name, customer_name, account_number, balance)

Fragment 1: Π(branch_name, customer_name, tuple_id)(employee)
Fragment 2: Π(account_number, balance, tuple_id)(employee)
```

**Reconstruction:** $employee = deposit_1 \bowtie deposit_2$ (join on tuple_id)

### Lossless Join Property & Tuple-ID

**Critical requirement:** All vertical fragments must contain a **common key** to ensure the *lossless join property*.

- A special attribute (e.g., **tuple-id**) may be added to each schema to serve as the key
- This ensures fragments can be rejoined without losing or duplicating data

### Advantages of Fragmentation

| Fragmentation Type | Advantages |
|:-------------------|:-----------|
| **Horizontal** | Allows parallel processing on fragments; tuples located where most frequently accessed |
| **Vertical** | Allows parallel processing; each part of tuple stored where most frequently accessed; tuple-id allows efficient joining |

### Mixed Fragmentation

Vertical and horizontal fragmentation can be **mixed**:
- Fragments may be successively fragmented to an arbitrary depth
- Creates a grid of fragments

---

## Page: Data Transparency

### Definition

**Data transparency** is the degree to which a system user may remain *unaware* of the details of *how* and *where* the data items are stored in a distributed system.

### Types of Transparency

| Type | What's Hidden | User Sees |
|:-----|:--------------|:----------|
| **Fragmentation Transparency** | How data is partitioned into fragments | A single, unified relation |
| **Replication Transparency** | That multiple copies of data exist | A single copy of data |
| **Location Transparency** | The physical site where data is stored | Data "just exists" |

### The Ideal

Full transparency at all levels: Users issue `SELECT * FROM customer` without knowing customers are fragmented across 5 continents and replicated 3 ways.

### Reality

Sometimes transparency is intentionally broken for performance tuning (e.g., query hints to force specific sites).

> **Note:** Similar ideas are used in distributed file systems like HDFS.

---

# 📂 Distributed Query Processing

This section covers how queries are processed when data is distributed across multiple sites. The key challenges are minimizing network transfer costs and exploiting parallelism.

### What You'll Learn

| Topic | Key Question |
|:------|:-------------|
| Cost Model | Why is network cost more important than disk I/O? |
| Query Transformation | How do queries adapt to fragmented data? |
| Reduced Query Trees | How do we avoid computing empty joins? |
| Join Strategies | When should we use centralized vs parallel vs semijoin? |
| Cost Analysis | How do we calculate and compare strategy costs? |

### The Paradigm Shift

| Centralized DB | Distributed DB |
|:---------------|:---------------|
| Optimize for **disk I/O** | Optimize for **network transfer** |
| Disk latency: ~10ms | Network latency: 10-200ms+ |
| Disk bandwidth: 100+ MB/s | WAN bandwidth: variable, often constrained |

### Key Considerations

1. **Data transmission cost** over the network (often the dominant factor)
2. **Potential gain from parallelism**: several sites process parts of the query in parallel
3. **Relative processing speed** at each site

### Core Principle

In distributed query processing, it is possible to construct a relation $r$ from its fragments. The query processor must **replace** relation names with expressions that reconstruct them, then **optimize** to minimize cross-site data movement.

---

## Page: Cost Model in Distributed Systems

### Cost Formula

A simplified distributed cost model:

$$\text{Total Cost} = \sum (c_0 + \text{data\_size} \times c_1)$$

Where:
- **$c_0$** = initial setup cost per message (connection overhead, headers)
- **$c_1$** = transmission cost per data unit (e.g., per 1000 bytes)

### Example Cost Calculation

Given:
- Setup cost $c_0 = 10$
- Transmission cost $c_1 = 1$ per 1000 bytes
- Data size = 50,000 rows × 80 bytes = 4,000,000 bytes

$$\text{Cost} = 10 + \frac{4,000,000}{1000} = 10 + 4000 = 4010$$

---

## Page: Query Processing on Fragments

### Translating Queries on Fragments

When a relation is fragmented, the query processor must:

1. **Replace** the relation name with an expression that constructs the relation from its fragments
2. **Optimize** by eliminating unnecessary fragment accesses

### Query Transformation Example

Consider horizontal fragmentation of the *account* relation:
$$account_1 = \sigma_{branch\_name = "Hillside"}(account)$$
$$account_2 = \sigma_{branch\_name = "Valleyview"}(account)$$

**Query:** $\sigma_{branch\_name = "Hillside"}(account)$

**Step 1:** Replace relation with union of fragments:
$$\sigma_{branch\_name = "Hillside"}(account_1 \cup account_2)$$

**Step 2:** Push selection through union:
$$\sigma_{branch\_name = "Hillside"}(account_1) \cup \sigma_{branch\_name = "Hillside"}(account_2)$$

**Step 3:** Apply fragment definitions:
- $\sigma_{Hillside}(account_1)$ → Just $account_1$ (already filtered)
- $\sigma_{Hillside}(\sigma_{Valleyview}(account))$ → **Empty set!**

**Result:** Only the Hillside site returns its $account_1$. Valleyview site not needed!

---

## Page: Reduced Query Trees

### Motivation

Not all fragment combinations produce results. By analyzing fragment predicates, we can **eliminate empty joins** before execution.

### Example: Join with Horizontal Fragments

**Relations:**
- **E(Eno, Ename, Title)** — horizontally fragmented:
  - $E_1 = \sigma_{Eno \le e3}(E)$
  - $E_2 = \sigma_{e3 < Eno \le e6}(E)$
  - $E_3 = \sigma_{Eno > e6}(E)$

- **G(Eno, Jno, Resp, Dur)** — horizontally fragmented:
  - $G_1 = \sigma_{Eno \le e3}(G)$
  - $G_2 = \sigma_{Eno > e3}(G)$

**Query:** `SELECT * FROM E, G WHERE E.Eno = G.Eno`

### Naïve Approach

1. Get E by union: $E_1 \cup E_2 \cup E_3$
2. Get G by union: $G_1 \cup G_2$
3. Join E and G

Steps 1 and 2 can be parallelized. But **not all $E_i$'s match $G_j$'s!**

### Identifying Empty Joins

| Join | E Fragment Range | G Fragment Range | Result |
|:-----|:-----------------|:-----------------|:-------|
| $E_1 \bowtie G_1$ | $Eno \le e3$ | $Eno \le e3$ | ✓ Valid |
| $E_1 \bowtie G_2$ | $Eno \le e3$ | $Eno > e3$ | ∅ Empty |
| $E_2 \bowtie G_1$ | $e3 < Eno \le e6$ | $Eno \le e3$ | ∅ Empty |
| $E_2 \bowtie G_2$ | $e3 < Eno \le e6$ | $Eno > e3$ | ✓ Valid |
| $E_3 \bowtie G_1$ | $Eno > e6$ | $Eno \le e3$ | ∅ Empty |
| $E_3 \bowtie G_2$ | $Eno > e6$ | $Eno > e3$ | ✓ Valid |

### Reduced Query Tree

$$\text{Result} = (E_1 \bowtie G_1) \cup (E_2 \bowtie G_2) \cup (E_3 \bowtie G_2)$$

**Advantages:**
- **Parallelism:** Three joins can execute simultaneously
- **Efficiency:** No time wasted on empty joins

---

## Page: Distributed Join Strategies

### Factors to Consider

- Amount of data to be shipped between sites
- Cost of transmitting a data block between sites
- Relative processing speed at each site

### Simple Join Strategies

**Scenario:** Compute $account \bowtie depositor \bowtie branch$
- account at $S_1$
- depositor at $S_2$
- branch at $S_3$
- Result needed at $S_I$

| Strategy | Description | Trade-off |
|:---------|:------------|:----------|
| **Centralized** | Ship all relations to one site, join locally | Simple but high transfer cost |
| **Serialized** | Compute joins incrementally, ship intermediate results | Less parallelism |
| **Parallel** | Compute multiple joins concurrently, pipeline results | Best performance, most complex |

### Parallel Distributed Join

**Example:** $r_1 \bowtie r_2 \bowtie r_3 \bowtie r_4$ (each $r_i$ at site $S_i$, result at $S_1$)

1. Ship $r_1$ to $S_2$, compute $(r_1 \bowtie r_2)$ at $S_2$
   **SIMULTANEOUSLY** ship $r_3$ to $S_4$, compute $(r_3 \bowtie r_4)$ at $S_4$

2. $S_2$ sends tuples of $(r_1 \bowtie r_2)$ to $S_1$ **as they are produced**
   $S_4$ sends tuples of $(r_3 \bowtie r_4)$ to $S_1$ **as they are produced**

3. At $S_1$, compute $(r_1 \bowtie r_2) \bowtie (r_3 \bowtie r_4)$ **in parallel** with steps 1-2

**Benefits:**
- **Pipelining:** Start processing before all data arrives
- **Parallelism:** Multiple joins execute simultaneously

---

## Page: Semijoin Strategy

### Motivation

Shipping whole $r_1$ or $r_2$ can be **very expensive** when only a small fraction of rows actually participate in the join!

### Definition

The **semijoin** of $r_i$ with $r_j$:
$$r_i \ltimes r_j = \Pi_{R_i}(r_i \bowtie r_j)$$

This selects only those tuples of $r_i$ that **contribute to** $r_i \bowtie r_j$.

### The Algorithm

**Scenario:** Join $r_1$ (at $S_1$) with $r_2$ (at $S_2$). Result needed at $S_1$.

| Step | Location | Operation | Purpose |
|:-----|:---------|:----------|:--------|
| 1 | $S_1$ | $temp_1 \leftarrow \Pi_{R_1 \cap R_2}(r_1)$ | Extract join keys only |
| 2 | Network | Ship $temp_1$: $S_1 \to S_2$ | Send keys (small!) |
| 3 | $S_2$ | $temp_2 \leftarrow r_2 \bowtie temp_1$ | Keep only matching $r_2$ rows |
| 4 | Network | Ship $temp_2$: $S_2 \to S_1$ | Send reduced $r_2$ |
| 5 | $S_1$ | $result \leftarrow r_1 \bowtie temp_2$ | Final join |

### Why It Works

- **$temp_1$** contains only the join key values—decides which rows match
- **$temp_2 = r_2 \bowtie temp_1 = r_2 \ltimes r_1$** (only $r_2$ tuples that contribute)
- **$r_1 \bowtie temp_2 = r_1 \bowtie r_2$** ✓

### Performance Gain

Total size of $temp_1$ and $temp_2$ is often **much smaller** than $r_1$ or $r_2$.

**When semijoin wins:** Low selectivity (few matches), join keys much smaller than full rows

**When semijoin loses:** Most rows match anyway, extra round-trip overhead exceeds savings

---

## Page: Cost Analysis of Join Strategies

### Example: Naïve vs Semijoin

**Given:**
- $r_1$ with schema R(A, B) at site $S_1$: 10,000 rows
- $r_2$ with schema S(B, C) at site $S_2$: 50,000 rows
- Attribute sizes: A = 116 bytes, B = 4 bytes, C = 76 bytes
- Cost model: $c_0 = 10$, $c_1 = 1$ per 1000 bytes

**Naïve Strategy 1: Join at $S_1$ (ship $r_2$)**
$$\text{Cost} = 10 + \frac{(76 + 4) \times 50,000}{1000} = 10 + 4000 = 4010$$

**Naïve Strategy 2: Join at $S_2$ (ship $r_1$)**
$$\text{Cost} = 10 + \frac{(116 + 4) \times 10,000}{1000} = 10 + 1200 = 1210$$

**Semijoin Strategy** (with: 2,000 distinct B values in $r_1$, 5,000 matching rows in $r_2$):

| Step | Calculation | Cost |
|:-----|:------------|:-----|
| Ship keys | $10 + \frac{2000 \times 4}{1000}$ | 18 |
| Ship matches | $10 + \frac{5000 \times 80}{1000}$ | 410 |
| **Total** | | **428** |

**Winner:** Semijoin (428) beats both naïve strategies!

---

# 📝 Exercises

## Exercise 1: Semijoin Cost Calculation

**Given:**
- $r_1$ with schema R(A, B) at site $S_1$: 10,000 rows
- $r_2$ with schema S(A, C) at site $S_2$: 50,000 rows
- Attribute sizes: A = 10 bytes, B = 20 bytes, C = 30 bytes
- $card(\Pi_A(r_1)) = 1,000$ distinct A values
- $card(\Pi_A(r_2)) = 3,000$ distinct A values
- $card(r_1 \ltimes r_2) = 1,500$ ($r_1$ rows that match)
- $card(r_2 \ltimes r_1) = 3,500$ ($r_2$ rows that match)
- Cost: $c_0 = 20$, $c_1 = 1$ per 500 bytes

### Q1: Cost to get result at Site 1?

| Step | Calculation | Cost |
|:-----|:------------|:-----|
| Ship keys ($r_1 \to S_2$) | $20 + \frac{1000 \times 10}{500}$ | 40 |
| Ship matches ($r_2 \to S_1$) | $20 + \frac{3500 \times 40}{500}$ | 300 |
| **Total** | | **340** |

### Q2: Cost to get result at Site 2?

| Step | Calculation | Cost |
|:-----|:------------|:-----|
| Ship keys ($r_2 \to S_1$) | $20 + \frac{3000 \times 10}{500}$ | 80 |
| Ship matches ($r_1 \to S_2$) | $20 + \frac{1500 \times 30}{500}$ | 110 |
| **Total** | | **190** |

**Insight:** Result at $S_2$ is cheaper because we ship the smaller matching set.

---

## Exercise 2: Three-Site Join

**Given:**
- EMPLOYEE at Site 1: 1,000 tuples × 60 bytes (EID, Name, Salary, DID)
- DEPARTMENT at Site 2: 50 tuples × 30 bytes (DID, DName)
- Query: Site 3 needs (Name, DName) — result row = 40 bytes

| Strategy | Data Transfers | Total Cost |
|:---------|:---------------|:-----------|
| **1: Ship all to S3** | EMP: 60,000 + DEPT: 1,500 | **61,500 bytes** |
| **2: Join at S1** ✅ | DEPT→S1: 1,500 + Result→S3: 40,000 | **41,500 bytes** |
| **3: Join at S2** | EMP→S2: 60,000 + Result→S3: 40,000 | **100,000 bytes** |

**Key insight:** Ship the *smaller* relation (DEPT: 50 rows) for joining.

---

# 📂 Distributed Transactions

This section covers how transactions are managed when they span multiple sites. The key challenge is ensuring **atomicity**—all sites commit or all sites abort.

### What You'll Learn

| Topic | Key Question |
|:------|:-------------|
| System Architecture | What's the difference between TM and TC? |
| Failure Types | Why are network partitions the hardest to handle? |
| Commit Protocols | Why do we need special protocols for distributed commits? |
| Two-Phase Commit | How does 2PC ensure atomicity across sites? |
| Failure Handling | What happens when a participant or coordinator fails? |
| Blocking Problem | Why can 2PC get stuck, and what are the alternatives? |

### The Core Challenge

A transaction may access data at **several sites**. All sites must agree on the outcome:
- Either **everyone commits**
- Or **everyone aborts**

It's **unacceptable** to have a transaction committed at one site and aborted at another (e.g., in a cross-site money transfer, one account is debited but the other is never credited).

### Why It's Hard

| Challenge | Description |
|:----------|:------------|
| Independent failures | Sites can crash at any time, independently |
| Message loss | Network can drop packets |
| Network partition | Network can split into isolated groups |
| Coordinator failure | The decision-maker itself might crash |

---

## Page: System Architecture

### Transaction Processing Components

| Role | Scope | Responsibilities |
|:-----|:------|:-----------------|
| **Transaction Manager (TM)** | Local (per site) | Maintain log, execute recovery, manage locks, process subtransactions |
| **Transaction Coordinator (TC)** | Global (one per transaction) | Start execution, break into subtransactions, distribute to sites, coordinate commit/abort |

> **Key difference from centralized DB:** The Transaction Coordinator role doesn't exist in centralized systems.

### Communication Pattern

- **TC proactively communicates** with TMs at other sites
- **TM only receives messages** from remote TCs

### Transaction Lifecycle

1. Client submits transaction → that site becomes the Coordinator (TC)
2. TC breaks transaction into subtransactions
3. TC distributes subtransactions to appropriate sites
4. Each site's TM executes and reports back
5. TC decides: commit or abort
6. TC broadcasts decision to all participants

---

## Page: Failure Types

| Failure Type | Description | Handling |
|:-------------|:------------|:---------|
| **Site failure** | A machine crashes | Recovery via local log |
| **Message loss** | Network drops packets | TCP/IP retransmission |
| **Link failure** | Physical connection breaks | Route via alternative links |
| **Network partition** | Network splits into isolated groups | The hard problem |

### The Partition Problem

Sites A and B can't communicate. Is B down, or is the network broken?

**Critical insight:** Network partitioning and site failures are generally **indistinguishable**.

---

## Page: Commit Protocols

### The Atomicity Requirement

All sites must agree on the transaction outcome:
- Either **everyone commits**
- Or **everyone aborts**

It's **unacceptable** to have a transaction committed at one site and aborted at another.

### Two-Phase Commit (2PC)

The standard solution, **widely used in practice**.

**Assumptions:**
- **Fail-stop model:** Failed sites simply stop working (no Byzantine failures)
- Protocol initiated after the last step of the transaction

---

## Page: Two-Phase Commit Protocol

### Phase 1: Voting (Prepare Phase)

**Coordinator:**
1. Write `<prepare T>` to log, force to stable storage
2. Send `prepare T` to all participants

**Participant (TM):**
- **Can commit?**
  - YES: Write `<ready T>` to log, force all T's entries to stable storage, send `ready T`
  - NO: Write `<no T>` to log, send `abort T`

### Phase 2: Decision (Commit Phase)

**Coordinator decision:**
- ALL participants sent `ready` → **COMMIT**
- ANY participant sent `abort` OR timeout → **ABORT**

**Coordinator:**
1. Write `<commit T>` or `<abort T>` to log
2. Force to stable storage (**decision is now irrevocable**)
3. Send decision to all participants

**Participant:**
- Execute the decision locally

### Why Two Phases?

- **Phase 1:** Ensures everyone *can* commit before anyone *does* commit
- **Phase 2:** Ensures everyone learns the *same* decision

---

## Page: Failure Handling

### Participant Failure Recovery

When site $S_x$ recovers, examine the log:

| Log State | Meaning | Action |
|:----------|:--------|:-------|
| `<commit T>` | Decision received | **Redo(T)** |
| `<abort T>` | Decision received | **Undo(T)** |
| `<ready T>` only | Voted, no decision | **Ask TC** (in-doubt state) |
| Nothing about T | Failed before voting | **Undo(T)** (TC will abort) |

### Coordinator Failure

| Situation | Action |
|:----------|:-------|
| Active site has `<commit T>` | T must be committed |
| Active site has `<abort T>` | T must be aborted |
| Some site lacks `<ready T>` | Coordinator couldn't have committed → Abort |
| All have only `<ready T>` | **Must wait for coordinator** |

---

## Page: The Blocking Problem

### Scenario

1. TC sends PREPARE
2. Participants vote COMMIT, write `<ready>`
3. TC decides COMMIT, writes `<commit>`
4. **TC crashes before sending decision**

### Result

Participants are **stuck**:
- Voted COMMIT → can't unilaterally abort
- No decision received → can't commit
- **Must hold locks and wait** for TC to recover

This is called **blocking**.

### Why Participants Can't Decide Alone

| Action | Risk |
|:-------|:-----|
| Just commit? | TC might have aborted (another participant voted no) |
| Just abort? | TC might have committed and told other participants |
| Ask other participants? | If all have only `<ready>`, everyone is blocked |

### Solutions Beyond 2PC

| Protocol | Approach | Trade-off |
|:---------|:---------|:----------|
| **3PC** | Add "pre-commit" phase | More messages, still not partition-tolerant |
| **Paxos/Raft** | Consensus algorithms | Complex, higher latency |
| **Saga pattern** | Compensating transactions | Eventual consistency |

---

## Page: Network Partition Handling

### Case 1: All in Same Partition

Coordinator and all participants in one partition → **No effect** on protocol.

### Case 2: Split Across Partitions

**Sites NOT in coordinator's partition:**
- Think coordinator has failed
- Execute coordinator failure protocol
- May have to **wait** for coordinator

**Coordinator's partition:**
- Think other sites have failed
- Follow usual commit protocol

**Key insight:** Partition doesn't cause incorrect behavior, but can cause **blocking**.

---

# 📂 Summary

## Quick Reference: Replication vs Fragmentation

| Aspect | Replication | Fragmentation |
|:-------|:------------|:--------------|
| **What** | Copy data | Split data |
| **Improves** | Read performance, availability | Locality, parallel processing |
| **Complicates** | Writes, consistency | Joins, queries |
| **Reconstruction** | Any copy suffices | Union (horizontal) or Join (vertical) |

## Quick Reference: Semijoin Steps

| Step | Location | Operation |
|:-----|:---------|:----------|
| 1 | $S_1$ | $temp_1 \leftarrow \Pi_{R_1 \cap R_2}(r_1)$ |
| 2 | Network | Ship $temp_1$: $S_1 \to S_2$ |
| 3 | $S_2$ | $temp_2 \leftarrow r_2 \bowtie temp_1$ |
| 4 | Network | Ship $temp_2$: $S_2 \to S_1$ |
| 5 | $S_1$ | $result \leftarrow r_1 \bowtie temp_2$ |

## Quick Reference: 2PC Log States

| Log State | Meaning | Recovery |
|:----------|:--------|:---------|
| Nothing | Never started | Undo |
| `<ready T>` | Voted, awaiting decision | Ask TC |
| `<commit T>` | Decision received | Redo |
| `<abort T>` | Decision received | Undo |

## Key Concepts Checklist

- [ ] Parallel vs. distributed databases (network cost)
- [ ] Homogeneous vs. heterogeneous systems
- [ ] Replication: advantages, disadvantages, primary copy
- [ ] Fragmentation: horizontal, vertical, lossless join
- [ ] Three types of transparency
- [ ] Query transformation for fragments
- [ ] Reduced query trees (empty join elimination)
- [ ] Semijoin algorithm and cost calculation
- [ ] Parallel/pipelined join strategies
- [ ] TM vs. TC roles
- [ ] Four failure types
- [ ] 2PC protocol (both phases)
- [ ] Blocking problem and why it occurs
- [ ] Participant and coordinator recovery

## The One Thing to Remember

> **In distributed systems, network cost dominates.** Every design decision—replication, fragmentation, join strategies—is ultimately about minimizing data movement while maintaining correctness.

---

## References

**Mandatory readings:**
- A. Silberschatz, H. F. Korth, S. Sudarshan: *Database System Concepts* (7th edition), Chapters 20, 21, 22, 23
  - Optional: 21.3, 21.5, 22.6, 22.7, 22.8, 23.4, 23.5, 23.6, 23.7, 23.8