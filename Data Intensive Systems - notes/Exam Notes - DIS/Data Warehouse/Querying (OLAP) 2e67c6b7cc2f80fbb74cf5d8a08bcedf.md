# Querying (OLAP)

## Querying (OLAP)

- Navigation queries
- Aggregation queries
- Slice and dice
- Roll-up
- Drill-down
- Drill-out
- Drill-across

# Querying (OLAP)

## Key Terms

| Term | Definition |
| --- | --- |
| OLAP | Online Analytical Processing – systems designed for fast, interactive analysis of multidimensional data. |
| Navigation query | A query that moves through dimensions or hierarchies to change the view of data. |
| Aggregation | Summarizing detailed data into higher-level totals. |
| Slice | Selecting one value of a dimension to create a sub-cube. |
| Dice | Selecting a subset of values across multiple dimensions. |
| Roll-up | Aggregating data to a higher level in a dimension hierarchy. |
| Drill-down | Moving from aggregated data to more detailed data. |
| Drill-out | Removing a dimension from the analysis. |
| Drill-across | Comparing data across different fact tables. |

---

## Navigation Queries

Navigation queries allow users to:

- Move through the data cube
- Change which dimensions and levels are being viewed

They do not change the underlying data — only how it is **viewed and aggregated**.

OLAP tools are designed so these queries can be performed **interactively**.

---

## Aggregation Queries

Aggregation is the core of OLAP.

It computes:

- SUM
- COUNT
- AVG
- MIN
- MAX

over many facts.

Example:

- Total sales per month
- Total sales per product category

Aggregation turns detailed transaction data into **high-level business insights**.

---

## Slice and Dice

### Slice

A **slice** selects one fixed value of a dimension.

Example:

- All sales in **2024**

This reduces the cube by one dimension.

---

### Dice

A **dice** selects multiple values from multiple dimensions.

Example:

- Sales for **Product = Beer or Wine**
- In **Stores = Copenhagen or Aarhus**
- In **2024**

This creates a smaller **sub-cube**.

---

## Roll-Up

Roll-up moves **up** a hierarchy to get more aggregated data.

Example:

```
Day → Month → Year
```

Rolling up from **day to month** sums daily sales into monthly totals.

Used when:

- You want a higher-level overview

---

## Drill-Down

Drill-down moves **down** a hierarchy.

Example:

```
Year → Month → Day
```

It reveals more detailed data.

Used when:

- You see something interesting at a high level
- You want to understand what caused it

---

## Drill-Out

Drill-out removes a dimension.

Example:

- From **Sales by Product and Store**
- To **Sales by Product (across all stores)**

This increases aggregation by dropping a dimension.

---

## Drill-Across

Drill-across compares:

- Different fact tables
- Using the same dimensions

Example:

- Compare **Sales** and **Inventory** by Product and Time

This enables:

- Cross-process analysis

---

## Summary

OLAP querying allows users to:

- Explore data interactively
- Aggregate, filter, and navigate through dimensions
- Analyze business performance from many perspectives

It is what turns a data warehouse into a powerful **decision-support system**.