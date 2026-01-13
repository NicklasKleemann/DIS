# Apriori Principle

## Apriori Principle

- Downward closure (anti-monotonicity)
- Why pruning works
- Reducing search space

## Key Terms

| Term | Definition |
| --- | --- |
| Apriori principle | The fundamental property used in Apriori that all subsets of a frequent itemset must also be frequent. |
| Downward closure | The property that frequency decreases as itemsets grow larger. |
| Anti-monotonicity | Another name for downward closure: if a set is infrequent, all of its supersets must be infrequent. |
| Pruning | Removing candidate itemsets that cannot possibly be frequent. |
| Search space | The set of all possible itemsets that could be tested. |

---

## Downward Closure (Anti-Monotonicity)

The **Apriori principle** is also called **downward closure** or **anti-monotonicity**.

It states:

> If an itemset is frequent, then all of its subsets are also frequent.
> 
> 
> If an itemset is infrequent, then all of its supersets must also be infrequent.
> 

Mathematically:

$support(X) \ge minsup \Rightarrow support(Y) \ge minsup \quad \text{for all } Y \subseteq X$

and

$support(X) < minsup \Rightarrow support(Z) < minsup \quad \text{for all } Z \supseteq X$

---

## Why Pruning Works

Because of anti-monotonicity:

- If a candidate itemset contains **any** infrequent subset
- Then it **cannot** be frequent

So we can safely discard it without checking the database.

Example:

If {bread, milk} is infrequent, then:

- {bread, milk, butter}
- {bread, milk, eggs}
- {bread, milk, beer}

are all guaranteed to be infrequent and never need to be tested.

This saves:

- Database scans
- Support counting
- Memory and computation

---

## Reducing the Search Space

Without the Apriori principle:

- Every possible itemset would have to be tested
- This grows exponentially as 2n2^n2n, where nnn is the number of items

With Apriori:

- Only itemsets whose subsets are frequent are considered
- The number of candidates shrinks dramatically at each level

This makes Apriori feasible for real-world datasets.

---

## Summary

The Apriori principle is the **core idea** behind association rule mining efficiency.

It:

- Explains why pruning is correct
- Eliminates huge parts of the search space
- Makes large-scale pattern discovery possible