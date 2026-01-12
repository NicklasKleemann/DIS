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
| **Semijoin** | A join optimization that ships only the join keys first, then fetches only the matching rows. Dramatically reduces network traffic. |
| **Transaction Coordinator (TC)** | The site that initiates a distributed transaction and orchestrates the commit/abort decision across all participants. |
| **Two-Phase Commit (2PC)** | A protocol ensuring atomicity across sites: first get everyone to *promise* they can commit (Phase 1), then tell everyone the final decision (Phase 2). |

---

# 📂 Introduction

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

## Page: Distributed Database Systems Overview

A DDBS consists of autonomous sites connected by a network. Key characteristics:

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

## Page: Heterogeneous and Homogeneous Systems

### Homogeneous Distributed Databases

**Definition:** All sites run the *same* DBMS software with *identical* schemas.

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

The fundamental question: *Where should data physically live?*

Two orthogonal strategies: **Replication** (make copies) and **Fragmentation** (split it up). You can combine them.

---

## Page: Replication

**Definition:** Maintaining identical copies of data at multiple sites.

### Replication Spectrum

```
No Replication ←——————————————————→ Full Replication
(each item at 1 site)              (every item at every site)
```

- **No replication:** Each data item exists at exactly one site
- **Partial replication:** Some data is replicated, some isn't (most common)
- **Full replication:** Every site has a complete copy of everything

### Trade-offs

| ✅ Advantages | ❌ Disadvantages |
|:-------------|:-----------------|
| **Availability:** Site failure doesn't lose data | **Update overhead:** Every write must propagate to all copies |
| **Read performance:** Queries served locally | **Consistency complexity:** Keeping copies synchronized is hard |
| **Fault tolerance:** Natural backup | **Storage cost:** N copies = N× storage |
| **Load distribution:** Spread read load across sites | **Conflict resolution:** Concurrent updates to different copies |

### When to Replicate

✅ **Good candidates:**
- Read-heavy data (e.g., product catalogs)
- Critical data that must survive failures
- Data frequently accessed from multiple locations

❌ **Poor candidates:**
- Frequently updated data
- Large datasets with storage constraints
- Data with strict real-time consistency requirements

---

## Page: Fragmentation

**Definition:** Dividing a relation into smaller pieces (*fragments*) stored at different sites.

**Golden Rule:** You must be able to reconstruct the original relation from its fragments (no data loss, no spurious data).

### Horizontal Fragmentation

**What:** Partition by *rows*. Each fragment contains a subset of tuples.

**How:** Apply selection predicates to assign rows to fragments.

```
Original: account(account_id, branch, balance)

Fragment 1 (NYC site):    σ(branch = 'NYC')(account)
Fragment 2 (London site): σ(branch = 'London')(account)
Fragment 3 (Tokyo site):  σ(branch = 'Tokyo')(account)
```

**Reconstruction:** `account = Fragment1 ∪ Fragment2 ∪ Fragment3`

**Benefits:**
- Data lives where it's most frequently accessed
- Queries with matching predicates only touch relevant fragments
- Load balancing based on data characteristics

### Vertical Fragmentation

**What:** Partition by *columns*. Each fragment contains a subset of attributes.

**Critical requirement:** All fragments must include the primary key (or a tuple-id) to enable lossless reconstruction via joins.

```
Original: employee(emp_id, name, address, salary, department)

Fragment 1 (HR site):      Π(emp_id, name, address)(employee)
Fragment 2 (Payroll site): Π(emp_id, salary)(employee)
Fragment 3 (Ops site):     Π(emp_id, department)(employee)
```

**Reconstruction:** `employee = Fragment1 ⋈ Fragment2 ⋈ Fragment3`

**Benefits:**
- Queries access only needed columns (no wasted bandwidth)
- Sensitive data (salaries) isolated at specific sites
- Smaller fragments = faster local scans

### Mixed (Hybrid) Fragmentation

Combine both: first fragment horizontally, then vertically (or vice versa). Creates a grid of fragments.

---

## Page: Data Transparency

**Goal:** Shield users from distribution complexity. Users write queries as if data were in one place.

| Transparency Level | What's Hidden | User Must Know |
|:-------------------|:--------------|:---------------|
| **Fragmentation transparency** | How data is partitioned | Nothing about fragments |
| **Replication transparency** | That copies exist | Nothing about replicas |
| **Location transparency** | Physical site locations | Nothing about geography |

**The ideal:** Full transparency at all levels. Users issue `SELECT * FROM customer` without knowing customers are fragmented across 5 continents and replicated 3 ways.

**Reality:** Sometimes transparency is intentionally broken for performance tuning (e.g., hints to query optimizer).

---

# 📂 Distributed Query Processing

## Page: Cost Model in Distributed Systems

### The Paradigm Shift

| Centralized DB | Distributed DB |
|:---------------|:---------------|
| Optimize for **disk I/O** | Optimize for **network transfer** |
| Disk latency: ~10ms | Network latency: 10-200ms+ |
| Disk bandwidth: 100+ MB/s | WAN bandwidth: variable, often constrained |

**Key insight:** A query plan that's optimal locally may be terrible in a distributed setting. We care about:

1. **Total bytes transferred** across the network
2. **Number of messages** (each has overhead)
3. **Message size** (small messages waste overhead; huge messages may timeout)

### Cost Formula

A simplified distributed cost model:

```
Total Cost = Σ (Message_Setup + Bytes_Transferred × Cost_Per_Byte)
```

Components:
- **Message setup:** Fixed cost per transmission (connection overhead, headers)
- **Transfer cost:** Proportional to data size

---

## Page: Query Processing on Fragments

When a relation is fragmented, query processing must:

1. **Locate relevant fragments** using fragment schemas
2. **Rewrite the query** to reference fragments instead of the base relation
3. **Optimize** to minimize cross-site data movement

### Reduced Query Trees

The query optimizer transforms queries involving fragmented relations:

```
Query: SELECT * FROM account WHERE balance > 10000

If account is horizontally fragmented by branch:
  - Original: σ(balance > 10000)(account)
  - Rewritten: σ(balance > 10000)(F1 ∪ F2 ∪ F3)
  - Optimized: σ(balance > 10000)(F1) ∪ σ(balance > 10000)(F2) ∪ σ(balance > 10000)(F3)
```

### Fragment Elimination

**Key optimization:** Skip fragments that can't possibly contribute results.

**Example:**
- Fragment 1: `emp_id ≤ 1000`
- Fragment 2: `1000 < emp_id ≤ 2000`
- Fragment 3: `emp_id > 2000`
- Query: `SELECT * FROM employee WHERE emp_id > 2500`

Only Fragment 3 needs to be accessed! Fragments 1 and 2 are *guaranteed* to have no matching rows.

---

## Page: Distributed Join Strategies

The **join** is where distributed query processing gets expensive. Joining two tables at different sites requires moving data.

### Strategy 1: Naive Ship-Whole

**Approach:** Ship one entire table to the other site, join locally.

```
R at Site 1, S at Site 2
Option A: Ship S → Site 1, join at Site 1
Option B: Ship R → Site 2, join at Site 2
```

**Cost:** Transfer size of the smaller table.

**Problem:** Even if only 1% of rows match, you ship 100% of the data.

---

## Page: Semijoin Strategy

### The Core Idea

**Observation:** Why ship entire tables when only a fraction will match?

**Semijoin Definition:** 
$$r_1 \ltimes r_2 = \Pi_{R_1}(r_1 \bowtie r_2)$$

This returns only the tuples from $r_1$ that have a matching tuple in $r_2$.

### The Semijoin Algorithm

**Scenario:** Join R (at Site 1) with S (at Site 2). Result needed at Site 1.

```
Step 1: Project join keys from R
        temp1 = Π_joinkey(R)              [at Site 1]

Step 2: Ship keys to Site 2
        Send temp1: Site 1 → Site 2       [NETWORK]

Step 3: Reduce S using the keys
        temp2 = S ⋈ temp1                 [at Site 2]
        (This keeps only S rows that will match)

Step 4: Ship reduced S back
        Send temp2: Site 2 → Site 1       [NETWORK]

Step 5: Perform final join
        Result = R ⋈ temp2                [at Site 1]
```

### Why This Works

- **Step 2 ships:** Only distinct join keys (usually much smaller than full rows)
- **Step 4 ships:** Only the rows of S that will actually participate in the join

**When semijoin wins:** When selectivity is low (few matches) and join keys are much smaller than full rows.

**When semijoin loses:** When most rows match anyway, the extra round-trip wastes time.

---

## Page: Cost Analysis of Join Strategies

### Cost Model Parameters

For these examples, we use:
- **Setup cost:** Fixed overhead per message (e.g., 10 or 20 units)
- **Transfer cost:** Cost per byte or per 1000 bytes

### Example: Comparing Strategies

**Scenario:**
- R at Site 1: 10,000 rows × 120 bytes = 1,200,000 bytes
- S at Site 2: 50,000 rows × 80 bytes = 4,000,000 bytes
- Join selectivity: 10% of S matches (5,000 rows)
- Distinct join keys in R: 2,000 keys × 4 bytes each
- Cost model: Setup = 10, Transfer = 1 per 1000 bytes

**Strategy 1: Ship S to Site 1 (Naive)**
```
Cost = Setup + (Bytes / 1000)
     = 10 + (4,000,000 / 1000)
     = 10 + 4,000
     = 4,010
```

**Strategy 2: Semijoin**
```
Step 1-2 (Ship keys R → S):
    Bytes = 2,000 keys × 4 bytes = 8,000 bytes
    Cost₁ = 10 + (8,000 / 1000) = 18

Step 3-4 (Ship matching S → R):
    Bytes = 5,000 rows × 80 bytes = 400,000 bytes
    Cost₂ = 10 + (400,000 / 1000) = 410

Total = 18 + 410 = 428
```

**Result:** Semijoin is ~10× cheaper in this scenario.

---

### Exercise 1: Semijoin Cost Calculation

**Given:**
- r₁ at Site 1: 10,000 rows, attribute A (10 bytes), attribute B (20 bytes)
- r₂ at Site 2: 50,000 rows, attribute A (10 bytes), attribute C (30 bytes)  
- Join on attribute A
- 1,000 distinct A values in r₁; 3,000 distinct A values in r₂
- 1,500 rows of r₁ match; 3,500 rows of r₂ match
- Cost: Setup = 20, Transfer = 1 per 500 bytes

**Q1: Semijoin cost to get result at Site 1?**

```
Ship keys from r₁ to Site 2:
    1,000 distinct A × 10 bytes = 10,000 bytes
    Cost₁ = 20 + (10,000 / 500) = 20 + 20 = 40

Ship matching r₂ rows to Site 1:
    3,500 rows × (10 + 30) bytes = 140,000 bytes
    Cost₂ = 20 + (140,000 / 500) = 20 + 280 = 300

Total = 40 + 300 = 340
```

**Q2: Semijoin cost to get result at Site 2?**

```
Ship keys from r₂ to Site 1:
    3,000 distinct A × 10 bytes = 30,000 bytes
    Cost₁ = 20 + (30,000 / 500) = 20 + 60 = 80

Ship matching r₁ rows to Site 2:
    1,500 rows × (10 + 20) bytes = 45,000 bytes
    Cost₂ = 20 + (45,000 / 500) = 20 + 90 = 110

Total = 80 + 110 = 190
```

**Insight:** Getting the result at Site 2 is cheaper because we ship the smaller matching set.

---

### Exercise 2: Three-Site Join

**Given:**
- Emp at Site 1: 1,000 rows × 60 bytes (emp_id, name, dept_id)
- Dept at Site 2: 50 rows × 30 bytes (dept_id, dept_name)
- Result needed at Site 3: (name, dept_name) = 40 bytes/row
- All 1,000 employees have valid departments (full match)

**Strategy 1: Ship everything to Site 3**
```
Emp: Site 1 → Site 3 = 1,000 × 60 = 60,000 bytes
Dept: Site 2 → Site 3 = 50 × 30 = 1,500 bytes
Total = 61,500 bytes
```

**Strategy 2: Join at Site 1, ship result to Site 3** ✅ Best
```
Dept: Site 2 → Site 1 = 50 × 30 = 1,500 bytes
Result: Site 1 → Site 3 = 1,000 × 40 = 40,000 bytes
Total = 41,500 bytes
```

**Strategy 3: Join at Site 2, ship result to Site 3**
```
Emp: Site 1 → Site 2 = 1,000 × 60 = 60,000 bytes
Result: Site 2 → Site 3 = 1,000 × 40 = 40,000 bytes
Total = 100,000 bytes
```

**Key insight:** Ship the smaller table to a site, do the join, *then* ship the result. Moving Dept (50 rows) is much cheaper than moving Emp (1,000 rows).

---

# 📂 Distributed Transactions

## Page: System Architecture

### Transaction Processing Components

In a distributed system, transaction management is split across two roles:

| Role | Scope | Responsibilities |
|:-----|:------|:-----------------|
| **Transaction Manager (TM)** | Local (per site) | Maintain local log, execute recovery, manage local locks, process subtransactions |
| **Transaction Coordinator (TC)** | Global (one per transaction) | Decompose transaction into subtransactions, distribute to sites, collect votes, decide commit/abort |

### How a Distributed Transaction Works

```
1. Client submits transaction to a site → that site becomes the Coordinator (TC)
2. TC analyzes the transaction and identifies which sites need to participate
3. TC sends subtransactions to relevant sites
4. Each site's TM executes its subtransaction and reports back
5. TC decides: commit (if all succeed) or abort (if any fails)
6. TC broadcasts the decision to all participants
```

---

## Page: Failure Types

Distributed systems introduce failure modes that don't exist in centralized systems.

| Failure Type | Description | Handling |
|:-------------|:------------|:---------|
| **Site failure** | A machine crashes | Recovery via local log; other sites may timeout waiting |
| **Message loss** | Network drops packets | TCP retransmission; timeouts detect permanent loss |
| **Network partition** | Network splits into isolated groups | The hard problem—sites can't distinguish partition from failure |

### The Partition Problem

**Scenario:** Sites A and B can't communicate. Is B down, or is the network broken?

**Why it matters:** 
- If B is down, A might proceed with the transaction
- If it's a partition, B might also proceed—leading to inconsistent state

This is the core challenge that makes distributed transactions hard.

---

## Page: Commit Protocols

### The Problem

**Requirement:** All sites must agree on the transaction outcome. Either *everyone* commits, or *everyone* aborts.

**Why it's hard:** 
- Sites can fail independently
- Messages can be lost
- Any site might crash *during* the commit process

We need a **commit protocol**—a formal procedure to reach consensus.

---

## Page: Two-Phase Commit (2PC)

The standard solution for distributed atomic commits.

### Phase 1: Voting (The "Prepare" Phase)

```
TC → All Participants: "PREPARE T"

Each Participant:
  - Can I commit? (check locks, constraints, resources)
  - If YES:
      Write <ready T> to log (FORCE to disk!)
      Send "VOTE-COMMIT" to TC
  - If NO:
      Write <abort T> to log
      Send "VOTE-ABORT" to TC
```

**Critical point:** Once a participant votes COMMIT, it *promises* it can commit later. The `<ready>` log record makes this promise durable.

### Phase 2: Decision (The "Commit" Phase)

```
TC collects all votes:
  - If ALL votes are COMMIT → Decision = COMMIT
  - If ANY vote is ABORT (or timeout) → Decision = ABORT

TC:
  Write <commit T> or <abort T> to log (FORCE to disk!)
  Send decision to all participants

Each Participant:
  Write <commit T> or <abort T> to log
  Execute the decision
  Send ACK to TC

TC:
  After all ACKs received, write <complete T>
```

### Why Two Phases?

**Phase 1** ensures everyone *can* commit before anyone *does* commit.

**Phase 2** ensures everyone learns the same decision.

### The 2PC State Machine

```
         Participant                         Coordinator
         
         INITIAL                             INITIAL
            |                                   |
    receive PREPARE                        send PREPARE
            |                                   |
         WAITING ←---- times out ---→        WAITING
            |                                   |
    send VOTE-COMMIT                    collect all votes
    or VOTE-ABORT                              |
            |                           decide & send
         PREPARED ←——————————————————→    COMMITTED
      (or ABORTED)                       (or ABORTED)
            |                                   |
    receive decision                     collect ACKs
            |                                   |
        COMMITTED                          COMPLETE
      (or ABORTED)
```

---

## Page: Failure Handling

### Participant Failure Recovery

On restart, a participant checks its log:

| Log State | Action |
|:----------|:-------|
| `<commit T>` found | Redo the transaction |
| `<abort T>` found | Undo the transaction |
| `<ready T>` found, no decision | **In-doubt state**—must ask TC |
| Nothing about T | Transaction never started; abort is safe |

### Coordinator Failure Recovery

On restart, the coordinator checks its log:

| Log State | Action |
|:----------|:-------|
| `<commit T>` found | Resend COMMIT to all participants |
| `<abort T>` found | Resend ABORT to all participants |
| `<complete T>` found | Transaction finished; nothing to do |
| Only `<prepare T>` | Decision was never made; abort |

---

## Page: The Blocking Problem

### The Fatal Flaw of 2PC

**Scenario:**
1. TC sends PREPARE
2. Participants vote COMMIT, write `<ready>`, enter PREPARED state
3. TC receives votes, decides COMMIT, writes `<commit>` to log
4. TC crashes *before* sending the decision

**Result:** Participants are stuck:
- They voted COMMIT, so they can't unilaterally abort
- They never received the decision, so they can't commit
- They must **hold all locks** and **wait** for TC to recover

This is called **blocking**—participants are blocked, holding resources, unable to proceed.

### Why Can't Participants Decide?

**Why not just commit?** What if TC actually decided to abort? (e.g., one participant voted abort)

**Why not just abort?** What if TC decided to commit and already told some participants? Inconsistent state!

**Why not ask other participants?** 
- If any participant knows the decision, you're saved
- But if all participants are in PREPARED state... everyone is blocked

### Solutions (Beyond 2PC)

| Protocol | Approach | Trade-off |
|:---------|:---------|:----------|
| **3PC (Three-Phase Commit)** | Add a "pre-commit" phase for extra coordination | More messages, still not partition-tolerant |
| **Paxos/Raft** | Consensus algorithms that handle arbitrary failures | Complex, higher latency |
| **Saga pattern** | Compensating transactions instead of locking | Eventual consistency, application-level complexity |

---

# 📂 Summary

## Key Concepts Checklist

### Distribution Fundamentals
- [ ] Understand parallel vs. distributed databases (network cost is the key difference)
- [ ] Distinguish homogeneous vs. heterogeneous systems
- [ ] Know when to use replication vs. fragmentation (or both)
- [ ] Understand the three types of transparency

### Query Processing
- [ ] Recognize that network cost dominates in distributed settings
- [ ] Understand how queries are rewritten for fragmented data
- [ ] Know when semijoin is beneficial (low selectivity, small keys)
- [ ] Be able to calculate costs for naive vs. semijoin strategies
- [ ] Understand fragment elimination optimization

### Distributed Transactions
- [ ] Know the roles of Transaction Manager vs. Coordinator
- [ ] Understand the three failure types (site, message, partition)
- [ ] Be able to trace through 2PC protocol step by step
- [ ] Understand the meaning of the `<ready>` log record (promise to commit)
- [ ] Explain why 2PC can block and under what circumstances

## Quick Reference: Cost Calculation

```
Cost = Setup + (Bytes / CostDenominator)

For semijoin:
  Cost_total = Cost_ship_keys + Cost_ship_matches
  
  Cost_ship_keys = Setup + (distinct_keys × key_size / denominator)
  Cost_ship_matches = Setup + (matching_rows × row_size / denominator)
```

## Quick Reference: 2PC Log States

| Participant Log | Meaning | Recovery Action |
|:----------------|:--------|:----------------|
| Nothing | Never started | Safe to abort |
| `<ready T>` only | Voted commit, awaiting decision | Ask coordinator |
| `<commit T>` | Decision received | Redo |
| `<abort T>` | Decision received | Undo |

## The One Thing to Remember

> **Distributed systems trade simplicity for resilience.** Every optimization (replication, fragmentation, caching) adds complexity. The art is knowing which trade-offs fit your requirements.