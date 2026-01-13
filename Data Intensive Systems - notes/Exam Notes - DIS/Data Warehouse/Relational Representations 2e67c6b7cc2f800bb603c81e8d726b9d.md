# Relational Representations

## Relational Representations

- Fact tables
- Dimension tables
- Surrogate keys
- Star schema
- Snowflake schema
- Redundancy in data warehouses
- Star vs snowflake tradeoffs

# Relational Representations

## Key Terms

| Term | Definition |
| --- | --- |
| Fact table | The central table in a data warehouse that stores business events (facts) and numeric measures. |
| Dimension table | A table that stores descriptive attributes about a business dimension (e.g., product, time, store). |
| Surrogate key | An artificial key (usually an integer) used to uniquely identify dimension records in a data warehouse. |
| Star schema | A schema where the fact table is directly connected to denormalized dimension tables. |
| Snowflake schema | A schema where dimension tables are normalized into multiple related tables. |
| Redundancy | Repeated storage of the same attribute values across rows. |
| Schema tradeoff | The balance between performance, storage, and maintainability when choosing a schema design. |

---

## Fact Tables

A **fact table** stores:

- The **measures** (e.g., sales amount, quantity)
- **Foreign keys** referencing all related dimensions

Example (Sales Fact):

| product_key | store_key | time_key | sales_amount | quantity |
| --- | --- | --- | --- | --- |
| 101 | 22 | 20250501 | 7.75 | 1 |

Key properties:

- Very large
- Append-only
- High granularity (often one row per transaction)

The fact table represents the **business process** being analyzed (sales, shipments, visits, etc.).

---

## Dimension Tables

A **dimension table** provides the **context** for facts.

Example (Product Dimension):

| product_key | product_name | brand | category | size |
| --- | --- | --- | --- | --- |
| 101 | Cola | Coca-Cola | Soft Drink | 0.5L |

Dimensions:

- Contain descriptive attributes
- Are used for filtering, grouping, and labeling facts
- Are relatively small compared to fact tables

---

## Surrogate Keys

A **surrogate key** is:

- A meaningless, system-generated ID (e.g., 101, 102, 103)

Why they are used:

- Natural keys (e.g., product codes) may change
- Multiple historical versions of a dimension must exist (slowly changing dimensions)
- Surrogate keys ensure stable joins and good performance

Surrogate keys allow the warehouse to:

- Track history
- Avoid key conflicts
- Improve query speed

---

## Star Schema

In a **star schema**:

- The fact table is in the center
- All dimension tables connect directly to it

Structure:

```
        Time
         |
Product — Fact —Store
         |
      Customer
```

Characteristics:

- Dimension tables are **denormalized**
- Queries require fewer joins
- Very fast for OLAP workloads
- Simple and intuitive design

---

## Snowflake Schema

In a **snowflake schema**:

- Dimension tables are **normalized**
- Dimensions are split into multiple related tables

Example:

```
Fact → Store → City → Country
```

This removes redundancy but introduces:

- More tables
- More joins
- More complex queries

---

## Redundancy in Data Warehouses

Data warehouses **intentionally allow redundancy** in dimension tables.

Example:

- City name repeated for every store in that city

Why this is acceptable:

- Storage is cheap
- Query performance is more important than space
- It avoids expensive joins

This is very different from OLTP systems, which aim to eliminate redundancy.

---

## Star vs Snowflake Tradeoffs

| Star Schema | Snowflake Schema |
| --- | --- |
| Fewer tables | More tables |
| Faster queries | Slower queries |
| More redundancy | Less redundancy |
| Simple design | More complex |
| Preferred for OLAP | Used when dimensions are huge |

![image.png](Relational%20Representations/image.png)

![image.png](Relational%20Representations/image%201.png)

Rule of thumb from practice:

> Use star schema unless you have a very strong reason not to.
> 

Snowflake is useful when:

- Dimensions are extremely large
- Storage must be minimized

---

## Summary

Relational representations map multidimensional models into SQL tables.

- **Fact tables** store measures
- **Dimension tables** store context
- **Surrogate keys** ensure stability and history
- **Star schemas** maximize performance
- **Snowflake schemas** reduce redundancy

These structures allow OLAP systems to run fast, flexible analytical queries on top of relational databases.