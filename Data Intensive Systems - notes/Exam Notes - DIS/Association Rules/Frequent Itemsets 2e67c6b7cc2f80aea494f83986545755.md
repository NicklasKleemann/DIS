# Frequent Itemsets

## Frequent Itemsets

- What is a frequent itemset
- Support threshold (minsup)
- Downward closure property
- Candidate itemsets
- Pruning infrequent itemsets

# Frequent Itemsets

## Key Terms

| Term | Definition |
| --- | --- |
| Itemset | A set of one or more items appearing together in a transaction. |
| Support | The fraction of transactions that contain a given itemset. |
| Frequent itemset | An itemset whose support is greater than or equal to a user-defined minimum support threshold. |
| minsup | The minimum support threshold used to decide whether an itemset is frequent. |
| Downward closure property (Apriori principle) | If an itemset is frequent, then all of its subsets must also be frequent. |
| Candidate itemset | A potential frequent itemset that is generated and then tested against the database. |
| Pruning | The process of eliminating itemsets that cannot possibly be frequent. |

---

## What is a Frequent Itemset

An **itemset** is any set of items, such as:

- {milk}
- {bread, butter}
- {milk, bread, eggs}

A **frequent itemset** is an itemset that appears **often enough** in the transactional database.

Formally:

$X \text{ is frequent if } support(X) \ge minsup$

Only frequent itemsets are used to generate **association rules**, because rare itemsets are not statistically reliable.

---

## Support Threshold (minsup)

The **minimum support threshold (minsup)** is chosen by the user.

It defines:

> The smallest fraction of transactions an itemset must appear in to be considered frequent.
> 

Example:

If minsup = 0.3 and the database has 100 transactions,

then an itemset must appear in at least 30 transactions to be frequent.

Minsup controls:

- How many patterns are found
- How much noise is allowed

Lower minsup → more itemsets

Higher minsup → fewer but more reliable itemsets

---

## Downward Closure Property (Apriori Principle)

The **downward closure property** states:

> If an itemset is frequent, then all of its subsets must also be frequent.
> 

Example:

If {milk, bread, butter} is frequent, then:

- {milk, bread}
- {milk, butter}
- {bread, butter}
- {milk}
- {bread}
- {butter}
    
    must all also be frequent.
    

Conversely:

> If any subset of an itemset is infrequent, then the itemset itself cannot be frequent.
> 

This property is the key reason the Apriori algorithm is efficient.

---

## Candidate Itemsets

A **candidate itemset** is a set of items that is:

- Potentially frequent
- Generated from smaller frequent itemsets

Candidates are created by:

- Joining frequent (k−1)-itemsets to form k-itemsets

Example:

If {milk, bread} and {milk, butter} are frequent,

then {milk, bread, butter} becomes a candidate 3-itemset.

Candidates are not yet known to be frequent — their support must be counted.

---

## Pruning Infrequent Itemsets

After generating candidate itemsets:

- Their support is computed by scanning the database
- Any candidate with support < minsup is removed

This is called **pruning**.

Using the downward closure property:

- If a candidate contains an infrequent subset, it is removed **before** counting support
- This avoids unnecessary database scans and computations

Pruning drastically reduces:

- The number of itemsets tested
- The computational cost

---

## Summary

Frequent itemsets are the **foundation of association rule mining**.

They are:

- Itemsets whose support is at least minsup
- Found efficiently using the downward closure property
- Generated and filtered through candidate generation and pruning

Only frequent itemsets are used to build meaningful association rules.