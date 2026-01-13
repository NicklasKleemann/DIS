# Distributed Join Processing

# Distributed Join Processing

In a distributed database, relations involved in a join operation may be stored at different sites.

Distributed join processing refers to the techniques used to compute joins when the required tables or fragments are located on different machines.

Because moving data across the network is expensive, the main goal is to minimize data transfer while still producing the correct join result.

![image.png](Distributed%20Join%20Processing/image.png)

---

## Why Distributed Joins Are Expensive

A join usually requires combining many rows from two or more tables.

If these tables are at different sites, large amounts of data may need to be transferred over the network.

Since network communication is much slower than local computation, poor join strategies can make distributed queries extremely slow.

---

## Basic Join Strategies

### Ship Whole Table

One table is sent to the site of the other table, and the join is performed there.

Example:

- Table R at Site 1
- Table S at Site 2

Options:

- Send R to Site 2 and compute R ⋈ S
- Send S to Site 1 and compute R ⋈ S

The system chooses to send the smaller table to reduce data transfer.

---

### Join at a Third Site

Both tables are sent to a third site where the join is computed.

This is rarely used because it usually transfers the most data.

---

## Semijoin Strategy

The semijoin is an optimization technique used to reduce network traffic.

Instead of sending an entire table, only the join attributes are sent first.

Steps:

1. Send the join attribute of the first table to the second site
2. The second site finds matching values
3. Only the matching rows are sent back
4. The final join is performed

This avoids sending rows that will not participate in the join.

---

## When Semijoins Are Useful

Semijoins are effective when:

- Only a small subset of rows actually match
- Join attributes have many distinct values
- Tables are large

They significantly reduce the amount of data sent over the network.

---

## Cost-Based Choice

The distributed database system uses a cost model to decide:

- Which table to ship
- Whether to use a semijoin
- Where to perform the join

The optimizer chooses the strategy with the lowest estimated communication cost.

---

## Final Goal

The purpose of distributed join processing is to:

- Minimize network traffic
- Reduce response time
- Execute joins efficiently across multiple sites

Efficient join strategies are essential for making distributed databases practical at scale.