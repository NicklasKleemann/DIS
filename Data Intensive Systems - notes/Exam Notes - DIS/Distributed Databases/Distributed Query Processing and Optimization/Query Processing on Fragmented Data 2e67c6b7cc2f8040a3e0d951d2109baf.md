# Query Processing on Fragmented Data

# Query Processing on Fragmented Data

In a distributed database, relations are often fragmented and stored at different sites.

When a user submits a query, the system must access several fragments and combine them to produce the correct result.

The goal is to process the query efficiently while hiding fragmentation from the user.

---

## Basic Idea

The user writes a query as if the table were not fragmented.

The distributed database system then:

1. Determines which fragments are relevant
2. Sends subqueries to the sites where those fragments are stored
3. Executes operations locally on each fragment
4. Collects and combines the results
5. Returns the final answer to the user

---

## Query Processing with Horizontal Fragmentation

When a table is horizontally fragmented, each site stores different rows of the table.

To process a query:

- The system sends the query to all sites that store relevant fragments
- Each site executes the query on its local fragment
- The partial results are sent back
- The results are combined using UNION

### Example

If STUDENT is split by city:

- Copenhagen students at Site 1
- Aarhus students at Site 2

A query:

```
SELECT*FROM STUDENTWHERE Age>20;

```

is sent to both sites.

Each site filters its own rows.

The results are combined to produce the final answer.

### Formal Example

![image.png](Query%20Processing%20on%20Fragmented%20Data/image.png)

---

## Query Processing with Vertical Fragmentation

When a table is vertically fragmented, each site stores different columns of the table.

To process a query:

- The system identifies which fragments contain the required attributes
- The relevant fragments are retrieved
- The fragments are joined using the primary key (or tuple-ID)
- The final result is constructed

Example

EMPLOYEE is split into:

- (EID, Name) at Site 1
- (EID, Salary) at Site 2

A query:

```
SELECT Name, Salary FROM EMPLOYEE;
```

The system retrieves both fragments and joins them on EID.

---

## Query Processing with Mixed Fragmentation

If data is both horizontally and vertically fragmented:

1. The system first selects the correct horizontal fragments
2. Then it selects the required vertical fragments
3. It joins the vertical fragments
4. It unions the horizontal results

This allows very large databases to be processed efficiently across many sites.

---

## Optimization Goals

To make query processing efficient, the system tries to:

- Access only the fragments needed
- Perform filtering and projection as early as possible
- Minimize data transferred across the network
- Combine results efficiently

---

## Why This Is Important

Fragmented data allows:

- Faster access to local data
- Reduced network traffic
- Better scalability

Query processing mechanisms ensure that even though data is split across many sites, users still see a single logical database.