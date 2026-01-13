# Cost Model in Distributed Queries

A cost model is used to estimate how expensive it is to execute a query in a distributed database system.

### **Cost Formula**

A simplified distributed cost model:

$\text{Total Cost} = \sum (c_0 + \text{data\_size} \times c_1)$

Where:

- **$c_0$**= initial setup cost per message (connection overhead, headers)
- **$c_1$** = transmission cost per data unit (e.g., per 1000 bytes)

### **Example Cost Calculation**

Given:

- Setup cost $c_0 = 10$
- Transmission cost $c_1 = 1$ per 1000 bytes
- Data size = 50,000 rows × 80 bytes = 4,000,000 bytes

$\text{Cost} = 10 + \frac{4,000,000}{1000} = 10 + 4000 = 4010$

In a distributed system, data is stored at multiple sites, and queries may need to move data across the network. The cost model helps the query optimizer decide where and how to execute each part of a query so that the total cost is as low as possible.

The main goal is to minimize:

- Data transfer over the network
- Query execution time
- Use of system resources

---

## What Makes Distributed Queries Expensive?

In centralized databases, most of the cost comes from disk I/O and CPU.

In distributed databases, the dominant cost is usually **network communication**.

Sending data between sites is much slower and more expensive than processing data locally.

---

## Main Cost Components

### Communication Cost

This is the cost of sending data between sites.

It is usually modeled as:

- A fixed startup cost for opening a connection
- A cost proportional to the amount of data sent

More data sent over the network means higher cost.

---

### Local Processing Cost

This includes:

- Reading data from disk
- Performing joins, selections, and projections
- Writing results

This cost is usually much smaller than communication cost but still matters when large tables are processed.

---

### Coordination Cost

This includes:

- Synchronizing between sites
- Managing distributed transactions
- Waiting for results from remote sites

This increases when many sites are involved.

---

## Why Data Transfer Matters Most

If a query requires moving large tables across the network, it becomes very slow.

For this reason, distributed query optimization tries to:

- Move small tables instead of large ones
- Perform filtering as early as possible
- Send only needed attributes and rows

---

## Example

Suppose:

- Table A is at Site 1
- Table B is at Site 2
- We want to compute A ⋈ B

Two options:

1. Send A to Site 2 and join there
2. Send B to Site 1 and join there

The cost model compares:

- Size of A
- Size of B
- Network cost

The system chooses the cheaper option.

---

## Use of Semijoins

To reduce data transfer, systems may use **semijoins**.

Instead of sending an entire table, the system:

1. Sends only the join attributes
2. Uses them to filter the other table
3. Sends back only the matching rows

This can greatly reduce the amount of data sent over the network.

---

## Purpose of the Cost Model

The cost model allows the distributed query optimizer to:

- Compare different execution strategies
- Choose the one with the lowest estimated cost
- Improve performance and reduce network traffic

Without a cost model, the system would make poor decisions and distributed queries would be very slow.