# Query Transformation and Reduction

# Query Transformation and Reduction

Query transformation and reduction are techniques used in distributed databases to rewrite and simplify queries so that they can be executed more efficiently on fragmented and distributed data.

The goal is to reduce:

- The amount of data processed
- The amount of data sent over the network
- The overall query execution cost

Before a query is executed, it is transformed into an equivalent but cheaper form.

---

## Query Transformation

Query transformation means rewriting a query into an equivalent form that is easier or cheaper to execute.

The result of the query does not change, only the way it is executed.

Typical transformations include:

- Reordering operations (selection, projection, joins)
- Pushing selections closer to the data
- Pushing projections to remove unnecessary attributes

Example

Original query:

```
SELECT*FROM EMPLOYEEWHERE Salary>50000;

```

Instead of first retrieving all EMPLOYEE records and then filtering, the system applies the condition at each site before sending data.

---

## Query Reduction

Query reduction means eliminating unnecessary fragments or operations from a query.

This is possible because fragmentation rules describe which data is stored in which fragments.

Example

If EMPLOYEE is horizontally fragmented by department:

- Fragment 1: Dept = IT
- Fragment 2: Dept = HR

A query:

```
SELECT * FROM EMPLOYEE WHERE Dept='IT';
```

Only Fragment 1 needs to be accessed. Fragment 2 can be ignored.

This reduces:

- Disk access
- Network traffic
- Processing time

---

## Fragment Pruning

Fragment pruning is a key part of query reduction.

The system uses the fragmentation conditions to decide which fragments are relevant for a query.

Only those fragments are included in the query plan.

---

## Vertical Fragment Reduction

If a query only needs certain attributes, only the vertical fragments containing those attributes are accessed.

Example

If a query only needs Name and Salary, fragments that store Address or Phone are not accessed.

---

## Why Transformation and Reduction Matter

Without these techniques, a distributed system might:

- Access all fragments
- Transfer too much data
- Perform unnecessary joins

By transforming and reducing queries, the system:

- Works faster
- Uses less bandwidth
- Scales better

---

## Final Goal

The main purpose of query transformation and reduction is to produce a query plan that:

- Touches as little data as possible
- Moves as little data as possible
- Produces the correct result with minimal cost