# Fundamental Multidimensional Modelling

## Fundamental Multidimensional Modelling

- Facts and measures
- Dimensions
- Dimension hierarchies and levels
- Multidimensional cubes
- Cells, sparsity, and density
- Granularity
- Measures and aggregation
- Dimension attributes

# Fundamental Multidimensional Modelling

## Key Terms

| Term | Definition |
| --- | --- |
| Fact | A business event to be analyzed (e.g., a sale). |
| Measure | A numerical value describing a fact (e.g., sales price, quantity sold). |
| Dimension | A context used to describe facts (e.g., Product, Store, Time). |
| Hierarchy | A structure that organizes dimension levels from detailed to summarized. |
| Granularity | The level of detail at which facts are stored. |
| Cube | A multidimensional structure organizing facts by dimensions. |
| Cell | One entry in a cube corresponding to a specific combination of dimension values. |
| Density | How many cells in a cube contain data. |
| Sparsity | How many cells in a cube are empty. |

![image.png](Fundamental%20Multidimensional%20Modelling/image.png)

---

## Facts and Measures

A **fact** represents the subject of analysis — something that happened in the business.

Examples:

- A sale
- A shipment
- A transaction

A **measure** describes the fact numerically.

Examples:

- Sales price
- Quantity sold
- Revenue

From the slides:

> Each sales record is a fact, and its sales value is a measure. 10. Data Warehouse
> 

Facts are identified by their **dimension values**.

[https://www.notion.so](https://www.notion.so)

---

## Dimensions

A **dimension** gives context to facts.

Typical dimensions:

- Product
- Store
- Time

Each fact is associated with exactly one value from each dimension.

Example:

| Product | Store | Time | Sales |
| --- | --- | --- | --- |
| Beer | Aalborg | 25-May-2015 | 7.75 |

Dimensions group related attributes to make analysis easier. 
10. Data Warehouse

---

## Dimension Hierarchies and Levels

Each dimension is organized into **hierarchies**.

Example (Time):

```
Day → Month → Quarter → Year → T (top)
```

Example (Location):

```
Store → City → Region → Country → T
```

Hierarchies allow:

- Aggregation
- Roll-up
- Drill-down

They make OLAP queries efficient and intuitive. 
10. Data Warehouse

---

## Multidimensional Cubes

A **data cube** is a logical structure where:

- Each dimension is an axis
- Measures are stored in the cells

For example:

- 3 dimensions (Product, Store, Time) form a 3D cube
- Each cell contains a measure (e.g., sales)

This is the basis of **OLAP analysis**.

![image.png](Fundamental%20Multidimensional%20Modelling/image%201.png)

---

## Cells, Sparsity, and Density

A **cell** corresponds to:

(Product,Store,Time)→Measure(Product, Store, Time) → Measure

(Product,Store,Time)→Measure

Not all combinations exist:

- Some products are not sold in some stores
- Some dates have no transactions

This leads to:

- **Sparse cubes** → many empty cells
- **Dense cubes** → many filled cells

Sparsity affects:

- Storage
- Performance
- Query optimization

---

## Granularity

Granularity is the **level of detail** of facts.

Example:

- Transaction level → one row per sale
- Aggregated level → total sales per store per day

From the slides:

> Granularity is determined by the combination of the bottom levels of all dimensions. 10. Data Warehouse
> 

Lower granularity = more detail

Higher granularity = more summarized

---

## Measures and Aggregation

A measure has:

1. A **numeric value**
2. An **aggregation function** (e.g., SUM)

Example:

- Sales price aggregated by SUM
- Quantity aggregated by SUM
- Inventory might use AVG

Measures must be:

> Meaningful at all aggregation levels. 10. Data Warehouse
> 

---

## Dimension Attributes

Dimensions contain many attributes.

Example (Time):

- Day
- Week
- Month
- Year
- Holiday
- Season

From the slides:

> Good dimensions may have 50–100 or more attributes. 10. Data Warehouse
> 

These attributes allow flexible filtering and analysis.

![image.png](Fundamental%20Multidimensional%20Modelling/image%202.png)

---

## Summary

Multidimensional modeling:

- Organizes business data into facts and dimensions
- Supports aggregation via hierarchies
- Enables fast, intuitive OLAP analysis
- Is the conceptual foundation of data warehouses