# Storage model

# Storage Models in Data-Intensive Systems

This note summarizes all storage models covered in the course *Data-Intensive Systems (DIS)*.

---

# 1. Relational Database Storage

Relational databases store data in **tables (relations)** with **rows and columns** and a fixed **schema**. Data must follow this schema in order to be stored. 

## Two Physical Storage Models

### Row-oriented storage

Data is stored row by row.

Example table:

| ID | Name | Email |
| --- | --- | --- |
| 1 | Anna | a@mail |
| 2 | Bob | b@mail |

Stored physically as:

```
(1, Anna,a@mail)
(2, Bob, b@mail)
```

This layout stores all values of a record together.

---

### Column-oriented storage

Data is stored column by column.

The same table is stored as:

```
IDcolumn:1,2
Namecolumn:   Anna, Bob
Emailcolumn:  a@mail, b@mail
```

Only the columns that are needed for a query are read from disk. 

---

## Advantages and disadvantages

| Storage | Advantages | Disadvantages |
| --- | --- | --- |
| Row-oriented | Fast inserts, updates, and SELECT * queries | Reads unnecessary columns |
| Column-oriented | Very fast for analytics (SUM, AVG, COUNT) | Slow when updating a single record |

---

## When to use

Row-oriented storage is best for:

- Transaction systems
- Online applications
- Banking, user accounts, orders

Column-oriented storage is best for:

- Data warehouses
- Reports and analytics
- Large scans over few columns

---

## Example

A bank system retrieving a customer by ID uses row storage because all customer data is in one row.

A sales analysis computing total revenue uses column storage because only the revenue column needs to be read.

---

# 2. Key-Value Storage

Data is stored as pairs:

```
Key → Value
```

Example:

```
"user123" → {"name":"Mikkel","age":23 }
```

Each key is unique. The value can be any type of data: text, number, JSON, image, etc. 

---

## Advantages

- Very fast lookup by key
- Simple data model
- Easy to scale across many servers

---

## Disadvantages

- No complex queries
- No joins
- No foreign keys
- All relationships must be handled in application code

---

## When to use

Key-value stores are ideal for:

- Session storage
- Caching
- User profiles
- Shopping carts

They are especially good for high-speed reads and writes.

---

## Example

A website stores login sessions as:

```
sessionID → userID
```

This allows very fast authentication checks.

---

# 3. Document Storage

Data is stored as **documents** in formats such as JSON, BSON, XML or YAML.

Example document:

```json
{
"name":"Mikkel",
"age":23,
"courses":["DIS","WIB"]
}
```

Documents are grouped into **collections**. Documents in the same collection do not have to follow the same structure. 

---

## Advantages

- Flexible schema
- Natural fit for JSON-based applications
- Easy to store complex nested data
- Scales well

---

## Disadvantages

- No joins like in SQL
- Data duplication is common
- Weaker consistency guarantees

---

## When to use

Document stores are good for:

- Web applications
- Content management systems
- APIs returning JSON
- User profiles

---

## Example

A blog stores each article as one document containing:

```
title, text, tags, comments, author
```

All data for one article is stored together.

---

# 4. Graph Storage

Graph databases store data as:

- Nodes (entities)
- Edges (relationships)
- Properties (attributes)

Example:

```
(Alice)--FRIEND--> (Bob)
```

Relationships are first-class objects and are stored directly. 

---

## Advantages

- Very fast for relationship queries
- Natural representation of networks
- Very flexible data model

---

## Disadvantages

- Hard to scale across many servers
- Fewer standard query languages
- More complex than tables

---

## When to use

Graph databases are best for:

- Social networks
- Recommendation systems
- Fraud detection
- Network analysis

---

## Example

A social network stores:

```
User —FOLLOWS→User
User —LIKES→ Post

```

Finding friends of friends is very fast.

---

# 5. Triple-Store (RDF Storage)

Data is stored as triples:

```
(Subject, Predicate,Object)

```

Example:

```
(Mikkel, studies, DIS)
(DISt, type, Course)

```

This is the basis of RDF and the Semantic Web. 

---

## Advantages

- Very flexible
- Designed for linked data
- Powerful graph queries with SPARQL

---

## Disadvantages

- More complex
- Slower than property graphs
- Harder to design

---

## When to use

Triple-stores are used for:

- Knowledge graphs
- Linked open data
- Semantic web applications

---

## Example

Wikipedia-like data:

```
(Book1, writtenBy, Author1)
(Author1, bornIn, Denmark)

```

This allows rich semantic queries.

---

# Summary

| Model | Best used for |
| --- | --- |
| Row-oriented relational | Transactions, CRUD |
| Column-oriented relational | Analytics, reporting |
| Key-value | Sessions, caching |
| Document | Web apps, JSON data |
| Graph | Relationships and networks |
| Triple-store | Knowledge graphs and semantics |

---

If you want, I can also provide a **short exam-ready version** or a **comparison table for revision**.