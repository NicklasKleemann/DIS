# Reduced Query Trees

# Reduced Query Trees

A reduced query tree is an optimized version of a query tree used in distributed databases after applying query transformation and query reduction.

A query tree is a tree representation of a SQL query where:

- Leaves represent relations (tables or fragments)
- Internal nodes represent operations such as selection, projection, and join

A reduced query tree contains only the operations and fragments that are necessary to answer the query.

---

## Why Reduced Query Trees Are Used

In distributed databases, data is fragmented and stored at different sites.

If all fragments and all attributes are used blindly, the query becomes very expensive.

Reduced query trees remove:

- Unnecessary fragments
- Unnecessary attributes
- Unnecessary operations

This makes query execution faster and cheaper.

---

## How a Reduced Query Tree Is Created

The process is:

1. Start with the original query tree based on the SQL query
2. Apply query transformation rules
    - Push selections down
    - Push projections down
3. Apply query reduction
    - Remove irrelevant fragments
    - Remove unnecessary attributes
4. The result is the reduced query tree

This tree represents the most efficient way to compute the query before execution.

---

## Example (Conceptual)

Original query:

```
SELECT Name
FROM EMPLOYEE
WHERE Dept ='IT';
```

If EMPLOYEE is horizontally fragmented by department:

- Fragment 1: Dept = IT
- Fragment 2: Dept = HR

The reduced query tree:

- Keeps only Fragment 1
- Discards Fragment 2
- Keeps only the Name column

Only the required data is accessed.

![image.png](Reduced%20Query%20Trees/image.png)

---

## What Is Removed in a Reduced Query Tree

A reduced query tree removes:

- Fragments that cannot contribute to the result
- Attributes that are not used in the final output
- Redundant selections or projections

This leads to:

- Smaller intermediate results
- Less network communication
- Faster query execution

---

## Role in Distributed Query Processing

Reduced query trees are a key step before:

- Deciding where each operation will run
- Estimating costs
- Generating the final distributed execution plan

They ensure that the optimizer works with the smallest possible problem.

---

## Final Purpose

The purpose of reduced query trees is to ensure that distributed queries:

- Use only the required fragments
- Transfer only necessary data
- Are executed with minimal cost

They are the foundation for efficient distributed query optimization.