# Distributed Databases

# Exercise 1: Semijoin Strategy

> Consider r₁ with schema R(A, B) at site S₁ and r₂ with schema S(A, C) at site S₂. If we use the semijoin strategy to obtain r₁ ⋈ r₂, what is the total cost to obtain the result at S₁? What is the total cost to obtain the result at S₂?
> 

### Given Statistics

| Site S₁ (R) | Site S₂ (S) |
| --- | --- |
| card(R) = 10,000 | card(S) = 50,000 |
| card(∏ₐ(r₁)) = 1,000 | card(∏ₐ(r₂)) = 3,000 |
| card(∏ᵦ(r₁)) = 2,000 | card(∏꜀(r₂)) = 5,000 |
| card(r₁ ⋉ r₂) = 1,500 | card(r₂ ⋉ r₁) = 3,500 |
- **Attribute sizes:** A = 10 bytes, B = 20 bytes, C = 30 bytes
- **Costs:** c₀ = 20 (setup), c₁ = 1 per 500 bytes

$$
Cost = c_0 + c_1 × (\text{data size in bytes} / 500)
$$

---

## Result at $S_1$

**Semijoin Strategy:**

```python
1. S₁ → S₂: Send ∏ₐ(r₁) to S₂
2. S₂: Compute r₂ ⋉ r₁ (tuples in r₂ matching r₁)
3. S₂ → S₁: Send r₂ ⋉ r₁ to S₁
4. S₁: Compute final join r₁ ⋈ (r₂ ⋉ r₁)
```

**Cost Calculation**

| Step | Data | Size (bytes) |
| --- | --- | --- |
| Step 1 | ∏ₐ(r₁) | 1,000 × 10 = 10,000 |
| Step 3 | r₂ ⋉ r₁ | 3,500 × (10 + 30) = 140,000 |
| **Total data** |  | **150,000 bytes** |

```python
Cost = 2 × c₀ + c₁ × (150,000 / 500)
     = 2 × 20 + 1 × 300
     = 40 + 300
     = 340
```

---

## Result at $S_2$

**Semijoin Strategy:**

```python
1. S₁ → S₂: Send ∏ₐ(r₁) to S₂
2. S₂: Compute r₂ ⋉ r₁ (tuples in r₂ matching r₁)
3. S₂ → S₁: Send r₂ ⋉ r₁ to S₁
4. S₁: Compute final join r₁ ⋈ (r₂ ⋉ r₁)
```

**Cost Calculation:**

| Step | Data | Size (bytes) |
| --- | --- | --- |
| Step 1 | ∏ₐ(r₂) | 3,000 × 10 = 30,000 |
| Step 3 | r₁ ⋉ r₂ | 1,500 × (10 + 20) = 45,000 |
| **Total data** |  | **75,000 bytes** |

```python
Cost = 2 × c₀ + c₁ × (75,000 / 500)
     = 2 × 20 + 1 × 150
     = 40 + 150
     = 190
```

## Answer

| Destination | Total Data Transfer | Total Cost |
| --- | --- | --- |
| Result at S₁ | 150,000 bytes | **340** |
| Result at S₂ | 75,000 bytes | **190** |

**Conclusion:** Getting result at S₂ is cheaper because r₁ ⋉ r₂ is smaller than r₂ ⋉ r₁.

---

# Exercise 2: Distributed Join Strategies

> Site 1 has EMPLOYEE(EID, Name, Salary, DID), Site 2 has DEPARTMENT(DID, DName). Site 3 needs to find the name of employees and their department names. Figure out at least 3 strategies for this distributed join query and calculate the total amount of data transfer for each strategy.
> 

### Given Statistics

| Site 1: EMPLOYEE | Site 2: DEPARTMENT |
| --- | --- |
| EID: 10 bytes | DID: 10 bytes |
| Name: 20 bytes | DName: 20 bytes |
| Salary: 20 bytes |  |
| DID: 10 bytes |  |
| **Total: 1000 tuples** | **Total: 50 tuples** |

**Query:** Find (Name, DName) for all employees with their departments.

**Tuple sizes:**

- EMPLOYEE tuple: 10 + 20 + 20 + 10 = 60 bytes
- DEPARTMENT tuple: 10 + 20 = 30 bytes
- Result tuple (Name, DName): 20 + 20 = 40 bytes
- Projected EMPLOYEE (Name, DID): 20 + 10 = 30 bytes

---

## Strategy 1: Ship EMPLOYEE to Site 2, Join, Send to Site 3

```python
1. Site 1 → Site 2: Send EMPLOYEE (or projected ∏_{Name,DID}(EMPLOYEE))
2. Site 2: Perform join
3. Site 2 → Site 3: Send result
```

**Data Transfer:**

| Step | Data | Size |
| --- | --- | --- |
| Step 1 | ∏_{Name,DID}(EMPLOYEE) | 1000 × 30 = 30,000 bytes |
| Step 3 | Result (Name, DName) | 1000 × 40 = 40,000 bytes |
| **Total** |  | **70,000 bytes** |

---

## Strategy 2: Ship DEPARTMENT to Site 1, Join, Send to Site 3

```python
1. Site 2 → Site 1: Send DEPARTMENT
2. Site 1: Perform join
3. Site 1 → Site 3: Send result
```

**Data Transfer:**

| Step | Data | Size |
| --- | --- | --- |
| Step 1 | DEPARTMENT | 50 × 30 = 1,500 bytes |
| Step 3 | Result (Name, DName) | 1000 × 40 = 40,000 bytes |
| **Total** |  | **41,500 bytes** |

---

## Strategy 3: Ship Both to Site 3, Join Locally

```python
1. Site 1 → Site 3: Send ∏_{Name,DID}(EMPLOYEE)
2. Site 2 → Site 3: Send DEPARTMENT
3. Site 3: Perform join locally
```

**Data Transfer:**

| Step | Data | Size |
| --- | --- | --- |
| Step 1 | ∏_{Name,DID}(EMPLOYEE) | 1000 × 30 = 30,000 bytes |
| Step 2 | DEPARTMENT | 50 × 30 = 1,500 bytes |
| **Total** |  | **31,500 bytes** |

---

## Strategy 4: Semijoin Strategy

```python
1. Site 1 → Site 2: Send ∏_{DID}(EMPLOYEE) (distinct DIDs)
2. Site 2: Compute DEPARTMENT ⋉ EMPLOYEE
3. Site 2 → Site 1: Send matching departments
4. Site 1: Compute join, project (Name, DName)
5. Site 1 → Site 3: Send result
```

**Assumption:** All 50 departments have employees (or fewer distinct DIDs in EMPLOYEE).

**Data Transfer:**

| Step | Data | Size |
| --- | --- | --- |
| Step 1 | ∏_{DID}(EMPLOYEE) | ≤ 50 × 10 = 500 bytes |
| Step 3 | DEPARTMENT ⋉ EMPLOYEE | ≤ 50 × 30 = 1,500 bytes |
| Step 5 | Result | 1000 × 40 = 40,000 bytes |
| **Total** |  | **≤ 42,000 bytes** |

## Answer

| Strategy | Description | Data Transfer |
| --- | --- | --- |
| **1** | EMPLOYEE → Site 2 → Site 3 | 70,000 bytes |
| **2** | DEPARTMENT → Site 1 → Site 3 | 41,500 bytes |
| **3** | Both → Site 3 (join there) | **31,500 bytes** (Best) |
| **4** | Semijoin approach | ≤ 42,000 bytes |

**Conclusion:** Strategy 3 is most efficient because DEPARTMENT is small, and joining at the destination avoids sending intermediate results twice.