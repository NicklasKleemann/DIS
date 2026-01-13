# Changing Dimensions

## Changing Dimensions

- Slowly Changing Dimensions (SCD)
- Why dimension values change
- Problems with naive updates
- Solution 1 – overwrite
- Solution 2 – versioning
- Timestamped SCD
- Solution 3 – two values
- Rapidly changing dimensions
- Solution 4 – dimension splitting (minidimensions)

## Key Terms

| Term | Definition |
| --- | --- |
| Slowly Changing Dimension (SCD) | A dimension whose attribute values change over time. |
| Surrogate key | A warehouse-generated key used to identify dimension records and preserve history. |
| Natural key | A real-world identifier such as product code or customer ID. |
| Versioning | Storing multiple historical versions of a dimension record. |
| Timestamped SCD | A dimension that stores validity periods for each version. |
| Minidimension | A small dimension created from frequently changing attributes. |

---

## Slowly Changing Dimensions (SCD)

In a data warehouse:

- Dimension values do not stay constant
- Customers move
- Products change categories
- Stores change regions

These are called **slowly changing dimensions**.

The challenge:

> How do we update dimension data without destroying historical facts?
> 

---

## Why Dimension Values Change

Examples:

- A customer moves to a new city
- A product changes brand or category
- A store changes its sales region

Fact tables already reference old dimension values.

If we overwrite dimension rows, we lose history.

---

## Problems with Naive Updates

If we simply update a dimension row:

- All past facts now appear as if they occurred under the new values
- This produces **wrong historical reports**

Example:

- A customer moves from Aalborg to Copenhagen
- Old purchases suddenly appear as if they happened in Copenhagen

This violates the purpose of a data warehouse.

---

## Solution 1 – Overwrite (Type 1)

Old values are replaced with new ones.

- No history is kept
- Simple
- Wrong for historical analysis

Used when:

- Old values are not relevant
- Corrections of errors

---

## Solution 2 – Versioning (Type 2)

Each change creates a **new row** with a new surrogate key.

Example:

| CustomerKey | City | From | To |
| --- | --- | --- | --- |
| 101 | Aalborg | 2022 | 2024 |
| 245 | Copenhagen | 2024 | ∞ |

Fact tables link to the correct version.

This preserves full history.

---

## Timestamped SCD

Type 2 is often implemented with:

- Start date
- End date

This allows:

- Time-based queries
- “What did we know at that time?”

---

## Solution 3 – Two Values (Type 3)

Store:

- Current value
- Previous value

Example:

- City
- PreviousCity

Keeps limited history but:

- Only one change is stored
- Older history is lost

---

## Rapidly Changing Dimensions

Some attributes change too frequently:

- Customer income
- Loyalty score
- Risk level

Type 2 would explode the table size.

---

## Solution 4 – Dimension Splitting (Minidimensions)

Split fast-changing attributes into a **separate small dimension**.

Main dimension:

- Stable attributes

Mini-dimension:

- Volatile attributes

Fact table links to both.

This:

- Preserves history
- Avoids huge dimension growth

---

## Summary

Handling changing dimensions is essential for:

- Correct historical reporting
- Trustworthy BI

SCD techniques balance:

- Storage
- History
- Performance

Choosing the right SCD type is a key data warehouse design decision.