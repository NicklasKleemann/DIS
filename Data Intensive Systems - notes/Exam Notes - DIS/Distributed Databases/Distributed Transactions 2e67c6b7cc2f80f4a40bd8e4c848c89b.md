# Distributed Transactions

This section covers how transactions are managed when they span multiple sites. The key challenge is ensuring **atomicity**—all sites commit or all sites abort.

### **The Core Challenge**

A transaction may access data at **several sites**. All sites must agree on the outcome:

- Either **everyone commits**
- Or **everyone aborts**

It's **unacceptable** to have a transaction committed at one site and aborted at another (e.g., in a cross-site money transfer, one account is debited but the other is never credited).

### **Why It's Hard**

| Challenge | Description |
| --- | --- |
| Independent failures | Sites can crash at any time, independently |
| Message loss | Network can drop packets |
| Network partition | Network can split into isolated groups |
| Coordinator failure | The decision-maker itself might crash |

---

## **Page: System Architecture**

### **Transaction Processing Components**

| Role | Scope | Responsibilities |
| --- | --- | --- |
| **Transaction Manager (TM)** | Local (per site) | Maintain log, execute recovery, manage locks, process subtransactions |
| **Transaction Coordinator (TC)** | Global (one per transaction) | Start execution, break into subtransactions, distribute to sites, coordinate commit/abort |

> Key difference from centralized DB: The Transaction Coordinator role doesn't exist in centralized systems.
> 

### **Communication Pattern**

- **TC proactively communicates** with TMs at other sites
- **TM only receives messages** from remote TCs

### **Transaction Lifecycle**

1. Client submits transaction → that site becomes the Coordinator (TC)
2. TC breaks transaction into subtransactions
3. TC distributes subtransactions to appropriate sites
4. Each site's TM executes and reports back
5. TC decides: commit or abort
6. TC broadcasts decision to all participants

---

## **Page: Failure Types**

| Failure Type | Description | Handling |
| --- | --- | --- |
| **Site failure** | A machine crashes | Recovery via local log |
| **Message loss** | Network drops packets | TCP/IP retransmission |
| **Link failure** | Physical connection breaks | Route via alternative links |
| **Network partition** | Network splits into isolated groups | The hard problem |

### **The Partition Problem**

Sites A and B can't communicate. Is B down, or is the network broken?

**Critical insight:** Network partitioning and site failures are generally **indistinguishable**.

---

## **Page: Commit Protocols**

### **The Atomicity Requirement**

All sites must agree on the transaction outcome:

- Either **everyone commits**
- Or **everyone aborts**

It's **unacceptable** to have a transaction committed at one site and aborted at another.

### **Two-Phase Commit (2PC)**

The standard solution, **widely used in practice**.

**Assumptions:**

- **Fail-stop model:** Failed sites simply stop working (no Byzantine failures)
- Protocol initiated after the last step of the transaction

---

## **Page: Two-Phase Commit Protocol**

### **Phase 1: Voting (Prepare Phase)**

**Coordinator:**

1. Write `<prepare T>` to log, force to stable storage
2. Send `prepare T` to all participants

**Participant (TM):**

- **Can commit?**
    - YES: Write `<ready T>` to log, force all T's entries to stable storage, send `ready T`
    - NO: Write `<no T>` to log, send `abort T`

### **Phase 2: Decision (Commit Phase)**

**Coordinator decision:**

- ALL participants sent `ready` → **COMMIT**
- ANY participant sent `abort` OR timeout → **ABORT**

**Coordinator:**

1. Write `<commit T>` or `<abort T>` to log
2. Force to stable storage (**decision is now irrevocable**)
3. Send decision to all participants

**Participant:**

- Execute the decision locally

### **Why Two Phases?**

- **Phase 1:** Ensures everyone *can* commit before anyone *does* commit
- **Phase 2:** Ensures everyone learns the *same* decision

---

## **Page: Failure Handling**

### **Participant Failure Recovery**

When site Sx*Sx* recovers, examine the log:

| Log State | Meaning | Action |
| --- | --- | --- |
| `<commit T>` | Decision received | **Redo(T)** |
| `<abort T>` | Decision received | **Undo(T)** |
| `<ready T>` only | Voted, no decision | **Ask TC** (in-doubt state) |
| Nothing about T | Failed before voting | **Undo(T)** (TC will abort) |

### **Coordinator Failure**

| Situation | Action |
| --- | --- |
| Active site has `<commit T>` | T must be committed |
| Active site has `<abort T>` | T must be aborted |
| Some site lacks `<ready T>` | Coordinator couldn't have committed → Abort |
| All have only `<ready T>` | **Must wait for coordinator** |

---

## **Page: The Blocking Problem**

### **Scenario**

1. TC sends PREPARE
2. Participants vote COMMIT, write `<ready>`
3. TC decides COMMIT, writes `<commit>`
4. **TC crashes before sending decision**

### **Result**

Participants are **stuck**:

- Voted COMMIT → can't unilaterally abort
- No decision received → can't commit
- **Must hold locks and wait** for TC to recover

This is called **blocking**.

### **Why Participants Can't Decide Alone**

| Action | Risk |
| --- | --- |
| Just commit? | TC might have aborted (another participant voted no) |
| Just abort? | TC might have committed and told other participants |
| Ask other participants? | If all have only `<ready>`, everyone is blocked |

### **Solutions Beyond 2PC**

| Protocol | Approach | Trade-off |
| --- | --- | --- |
| **3PC** | Add "pre-commit" phase | More messages, still not partition-tolerant |
| **Paxos/Raft** | Consensus algorithms | Complex, higher latency |
| **Saga pattern** | Compensating transactions | Eventual consistency |

---

## **Page: Network Partition Handling**

### **Case 1: All in Same Partition**

Coordinator and all participants in one partition → **No effect** on protocol.

### **Case 2: Split Across Partitions**

**Sites NOT in coordinator's partition:**

- Think coordinator has failed
- Execute coordinator failure protocol
- May have to **wait** for coordinator

**Coordinator's partition:**

- Think other sites have failed
- Follow usual commit protocol

**Key insight:** Partition doesn't cause incorrect behavior, but can cause **blocking**.