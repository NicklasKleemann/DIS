# Problem Definition

## Problem Definition

- Transactional data
- Items and itemsets
- Association rules
- Support
- Confidence
- Lift

# Problem Definition – Association Rule Mining

## Key Terms

| Term | Definition |
| --- | --- |
| Transactional data | A dataset where each record (transaction) contains a set of items purchased or occurring together. |
| Item | A single element in a transaction (e.g., bread, milk). |
| Itemset | A set of one or more items. |
| Association rule | An implication of the form X → Y meaning that when X occurs, Y tends to occur as well. |
| Support | The proportion of transactions that contain a given itemset. |
| Confidence | The probability that Y occurs given that X has occurred. |
| Lift | A measure of how much more often X and Y occur together than expected if they were independent. |

---

## Transactional Data

Association rule mining works on **transactional databases**.

Each transaction is a set of items, for example:

| Transaction ID | Items |
| --- | --- |
| T1 | {bread, milk, butter} |
| T2 | {bread, diapers, beer} |
| T3 | {milk, diapers, beer, cola} |

Important properties:

- Order does **not** matter
- Items are either present or not present
- Data is typically very sparse

The goal is to find **regularities in item co-occurrence** across transactions.

---

## Items and Itemsets

- An **item** is a single product or event
- An **itemset** is any subset of items

Examples:

- {milk} → 1-itemset
- {bread, milk} → 2-itemset
- {bread, milk, butter} → 3-itemset

The number of possible itemsets grows **exponentially** with the number of items, which is why efficient algorithms like **Apriori** are needed.

---

## Association Rules

An **association rule** has the form:

$X \rightarrow Y$

where:

- X and Y are itemsets
- $X \cap Y = \varnothing$

Meaning:

> If a transaction contains X, it is likely to also contain Y.
> 

Example:

$\{bread, butter\} \rightarrow \{milk\}$

Interpretation:

- Customers who buy bread and butter tend to also buy milk.

Rules do not imply **causality** — only statistical co-occurrence.

---

## Support

Support measures **how frequent an itemset is** in the database.

For an itemset X:

$Total number of transactionssupport(X) = \frac{\text{Number of transactions containing } X}{\text{Total number of transactions}}$

Example:

If {milk, bread} appears in 30 out of 100 transactions:

$support(\{milk, bread\}) = 0.30$

Support is used to:

- Filter rare itemsets
- Define **frequent itemsets** (support ≥ minsup)

---

## Confidence

Confidence measures the **reliability of a rule**.

For a rule $X \rightarrow Y$:

$confidence(X \rightarrow Y) = \frac{support(X \cup Y)}{support(X)}$

Interpretation:

> Among all transactions that contain X, how many also contain Y?
> 

Example:

If:

- support({bread}) = 0.40
- support({bread, milk}) = 0.30

Then:

$confidence(\{bread\} \rightarrow \{milk\}) = \frac{0.30}{0.40} = 0.75$

So 75% of customers who buy bread also buy milk.

---

## Lift

Lift measures how much **better the rule is than random chance**.

$lift(X \rightarrow Y) = \frac{confidence(X \rightarrow Y)}{support(Y)}$

Interpretation:

- Lift > 1 → X and Y occur together more than expected
- Lift = 1 → X and Y are independent
- Lift < 1 → X and Y occur together less than expected

Example:

If:

- confidence(bread → milk) = 0.75
- support(milk) = 0.50

Then:

$lift = \frac{0.75}{0.50} = 1.5$

This means buying bread makes buying milk **1.5× more likely** than random chance.

---

## Summary

Association rule mining aims to discover **strong relationships between items** in transactional data.

It does this by:

- Finding frequent itemsets using **support**
- Evaluating rules using **confidence**
- Measuring usefulness using **lift**

These measures form the foundation for algorithms like **Apriori**.