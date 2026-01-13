# Semijoin Strategy

- Motivation
- Algorithm
- Formal Definition

# Semijoin Strategy

The semijoin strategy is a technique used in distributed databases to reduce the amount of data transferred over the network when performing join operations.

Instead of sending entire tables between sites, only the data that is actually needed for the join is transferred.

![image.png](Semijoin%20Strategy/image.png)

---

## Motivation

In distributed databases, relations involved in a join may be stored at different sites.

Sending an entire table across the network is expensive, especially when:

- Tables are large
- Only a small portion of rows actually match

The main motivation of the semijoin strategy is to:

- Reduce network traffic
- Avoid transferring irrelevant tuples
- Improve join performance

By filtering data before it is sent, the system avoids wasting bandwidth on rows that will not contribute to the final result.

---

## Algorithm

Suppose we want to compute the join:

R ⋈ S

where:

- R is stored at Site 1
- S is stored at Site 2
- The join is on attribute A

The semijoin algorithm works as follows:

1. Project the join attribute from R
    - Send πA(R) from Site 1 to Site 2
2. At Site 2, compute a semijoin
    - Keep only tuples of S whose A value appears in πA(R)
3. Send the reduced S back to Site 1
4. At Site 1, compute the final join
    - R ⋈ (reduced S)

Only the tuples that can participate in the join are transferred.

---

## Formal Definition

Let R(A, X) and S(A, Y) be two relations that share attribute A.

The semijoin of R with S is defined as:

R ⋉ S = { r ∈ R | ∃ s ∈ S such that r.A = s.A }

This means:

- R ⋉ S contains all tuples from R that have at least one matching tuple in S based on attribute A

Similarly:

- S ⋉ R keeps only those tuples of S that match some tuple in R

The semijoin does not produce the full join result.

It only filters a relation so that only join-relevant tuples remain.

---

If you want, I can also give you a **numerical example** showing how many bytes are saved using a semijoin.

Also provide the psudo code for the algoritme

Here is the **Notion-ready pseudocode** for the **Semijoin algorithm**.

---

## Semijoin Algorithm (Pseudocode)

We want to compute the join

R ⋈ S

where:

- R is stored at Site 1
- S is stored at Site 2
- The join attribute is A

---

### Step 1 – Project Join Attribute from R (Site 1)

```
JR ← PROJECTAFROMR
SEND JRTO Site2

```

This sends only the join column (A values) of R to Site 2.

---

### Step 2 – Reduce S Using JR (Site 2)

```
SR ← EMPTYSET

FOReach tuple sIN SDO
IF s.Aisin JRTHEN
ADD sTO SR
ENDIF
ENDFOR

SEND SRTO Site1

```

This keeps only the tuples of S that can participate in the join.

---

### Step 3 – Compute Final Join (Site 1)

```
RESULT ←EMPTYSET

FOReach tuple rIN R DO
FOReach tuple sIN SR DO
        IF r.A= s.ATHEN
ADD (r ⨝ s)TORESULT
END IF
ENDFOR
ENDFOR

RETURNRESULT

```

Only the reduced version of S is used, so much less data is processed and transferred.

---

## What This Achieves

The algorithm ensures that:

- Only necessary tuples of S are sent across the network
- The final join is correct
- Network traffic is minimized

This is why semijoins are very effective in distributed databases.

Make the complete notes for this now

# Semijoin Strategy

- Motivation
- Algorithm
- Formal Definition

Here are the **complete, clean Notion notes** for the **Semijoin Strategy**, including motivation, algorithm, and formal definition.

---