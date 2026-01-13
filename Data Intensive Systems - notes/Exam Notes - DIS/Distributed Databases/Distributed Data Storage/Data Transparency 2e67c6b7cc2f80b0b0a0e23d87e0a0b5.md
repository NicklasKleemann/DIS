# Data Transparency

- Fragmentation Transparency
- Replication Transparency
- Location Transparency

# Data Transparency

Data transparency refers to the ability of a distributed database system to hide the complexity of data distribution from users and applications.

Users should be able to access and manipulate data as if it were stored in a single, centralized database, even though it is actually spread across multiple sites.

The goal of data transparency is to make distribution invisible.

---

## Fragmentation Transparency

Fragmentation transparency means that users do not need to know that a table has been split into fragments.

A relation may be horizontally or vertically fragmented and stored at different sites, but users write queries as if the table were whole.

Example

A user writes:

```
SELECT * FROM EMPLOYEE;
```

The system automatically:

- Finds the relevant fragments
- Retrieves data from multiple sites
- Combines the results
- Returns a complete EMPLOYEE table

The user never sees the fragments.

---

## Replication Transparency

Replication transparency means that users do not know that multiple copies of the same data exist.

The system decides:

- Which copy to read from
- Where updates should be sent

Users simply issue queries and updates normally.

Example

If EMPLOYEE is replicated at three sites, a user does not have to choose which one to query. The system selects the best replica automatically.

---

## Location Transparency

Location transparency means that users do not need to know where data is physically stored.

Users refer to tables by their logical names, not by site names.

Example

A user writes:

```
SELECT * FROM STUDENT;
```

The user does not need to know whether STUDENT is stored in:

- Copenhagen
- Aarhus
- Or multiple locations

The distributed database system finds the data and returns it.

---

## Why Data Transparency Matters

Data transparency:

- Simplifies application development
- Reduces user errors
- Makes distributed databases easier to use
- Allows the system to change data placement without affecting applications

It is a key feature that makes a distributed database behave like a single unified system.