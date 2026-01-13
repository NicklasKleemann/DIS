# Fragmentation

Fragmentation is a technique used in distributed databases where a relation (table) is divided into smaller parts called fragments, and these fragments are stored at different sites.

Each fragment contains a subset of the original table’s data. When designed correctly, all fragments together contain exactly the same information as the original table.

Fragmentation is used to improve performance, reduce network traffic, and support local data access.

## Horizontal vs Vertical Fragmentation

| Feature | Horizontal Fragmentation | Vertical Fragmentation |
| --- | --- | --- |
| How data is split | By rows (tuples) | By columns (attributes) |
| What each fragment contains | A subset of records with all attributes | A subset of attributes with all records |
| What is kept in each fragment | All columns of the table | Only selected columns plus the primary key |
| How fragments are created | Using selection conditions (e.g., City = Copenhagen) | By grouping attributes based on usage |
| How the original table is reconstructed | By UNION of all fragments | By JOIN on the primary key (or tuple-ID) |
| Typical use case | When different locations use different records | When different applications use different attributes |
| Data locality | Stores only the rows needed at each site | Stores only the attributes needed at each site |
| Storage redundancy | No redundancy (unless replicated) | No redundancy (except primary key in all fragments) |
| Query performance | Faster for queries targeting specific subsets of rows | Faster for queries targeting specific subsets of columns |
| Example | Employees split by department or location | Employee personal info separated from salary data |

### **Definition**

A relation $r$ is partitioned into fragments $r_1,r_2,...,r_nr_1,r_2,...,r_n$ which contain **sufficient information to reconstruct** the original relation $*r*$.

## **Horizontal Fragmentation**

Horizontal fragmentation divides a table by rows.

Each fragment contains a subset of the tuples (records) of the original table, based on some condition.

Example

```
EMPLOYEE(EID, Name, Salary, Dept)

If the company has two branches:
	Fragment 1 (Copenhagen): 
		Employees where Dept = Copenhagen 
	Fragment 2 (Aarhus): 
		Employees where Dept = Aarhus
```

All columns are kept, but only some rows are stored in each fragment.

This is useful when different locations mostly access their own local data.

<aside>
💡 **Formal:** Each *tuple* (row) of $r$ is assigned to one or more fragments based on a selection predicate. **How:** Apply selection conditions to assign rows to fragments.

</aside>

**Another Example:**

```
Original: account(branch_name, account_number, balance)

Fragment 1: σ(branch_name = "Copenhagen")(account)
Fragment 2: σ(branch_name = "Aarhus")(account)

```

| branch_name | account_number | balance |
| --- | --- | --- |
| Copenhagen | A-305 | 500 |
| Copenhagen | A-226 | 336 |
| Copenhagen | A-155 | 62 |

$account_1 = \sigma_{branch\_name = "Copenhagen"}(account)$

**Reconstruction:** $account = account_1 \cup account_2$

## Vertical Fragmentation

Vertical fragmentation divides a table by columns.

Each fragment contains a subset of the attributes (columns), but must include the primary key so that rows can be reconstructed.

Example

```
EMPLOYEE(EID, Name, Salary, Address)  

Fragment 1:  - (EID, Name)  
Fragment 2:  - (EID, Salary, Address)
```

The common attribute EID allows the original table to be reconstructed by joining the fragments.

Vertical fragmentation is useful when different applications use different attributes of the same table.

<aside>
💡 **Formal:** The *schema* for relation $r$ is split into several smaller schemas. Each fragment contains a subset of attributes.

</aside>

**Example:**

```
Original: employee(branch_name, customer_name, account_number, balance)

Fragment 1: Π(branch_name, customer_name, tuple_id)(employee)
Fragment 2: Π(account_number, balance, tuple_id)(employee)

```

**Reconstruction:** $employee = deposit_1 \bowtie deposit_2$ (join on tuple_id)

### **Lossless Join Property & Tuple-ID**

For fragmentation to be correct, it must be possible to reconstruct the original table without losing information. This is called the lossless join property.

This means:

- When fragments are joined back together, the result must be exactly the same as the original table.

For horizontal fragmentation:

- Reconstruct by using UNION of all fragments.

For vertical fragmentation:

- Reconstruct by joining fragments using the primary key.

Tuple-ID is an internal unique identifier assigned to each row.

It is sometimes used instead of the primary key to reconnect vertical fragments.

This guarantees that fragments can always be joined correctly even if the original primary key is not included.

<aside>
💡 **Critical requirement:** All vertical fragments must contain a **common key** to ensure the *lossless join property*.

</aside>

- A special attribute (e.g., **tuple-id**) may be added to each schema to serve as the key
- This ensures fragments can be rejoined without losing or duplicating data

### **Advantages of Fragmentation**

| Fragmentation Type | Advantages |
| --- | --- |
| **Horizontal** | Allows parallel processing on fragments; tuples located where most frequently accessed |
| **Vertical** | Allows parallel processing; each part of tuple stored where most frequently accessed; tuple-id allows efficient joining |

### **Mixed Fragmentation**

Vertical and horizontal fragmentation can be **mixed**:

- Fragments may be successively fragmented to an arbitrary depth
- Creates a grid of fragments

---

## Fragmentation Examples

Horizontal fragmentation example:

STUDENT(SID, Name, City)

Fragment 1:

- Students where City = Copenhagen

Fragment 2:

- Students where City = Aarhus

Vertical fragmentation example:

STUDENT(SID, Name, Age, GPA)

Fragment 1:

- (SID, Name)

Fragment 2:

- (SID, Age, GPA)

Mixed fragmentation example:

A table is first split by rows (horizontal) and then each fragment is split by columns (vertical).

This is often used in large distributed systems.

---

## Advantages of Fragmentation

### Improved Performance

Queries can be processed using only the relevant fragments instead of the entire table. This reduces data transfer and speeds up execution.

---

### Reduced Network Traffic

Data that is only used locally does not need to be sent across the network.

---

### Scalability

Fragments can be stored on different machines, allowing the system to handle more data and users.

---

### Better Data Locality

Users and applications access data stored close to them, which improves response time.

---

### Increased Availability

If one fragment is unavailable, other fragments may still be accessible, allowing partial system operation.