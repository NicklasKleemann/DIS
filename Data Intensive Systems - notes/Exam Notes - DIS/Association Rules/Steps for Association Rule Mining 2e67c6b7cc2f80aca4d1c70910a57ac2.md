# Steps for Association Rule Mining

## Steps for Association Rule Mining

- Generating frequent itemsets
- Generating association rules
- Applying support and confidence thresholds

# Steps for Association Rule Mining

## Key Terms

| Term | Definition |
| --- | --- |
| Frequent itemset | An itemset whose support is greater than or equal to the minimum support threshold. |
| Association rule | An implication of the form X→YX \rightarrow YX→Y showing co-occurrence of itemsets. |
| Support threshold (minsup) | The minimum frequency required for an itemset to be considered frequent. |
| Confidence threshold (minconf) | The minimum confidence required for an association rule to be considered strong. |
| Rule generation | The process of creating association rules from frequent itemsets. |

---

## Overview

Association rule mining is a **two-stage process**:

1. Find all **frequent itemsets**
2. From these itemsets, generate **strong association rules**

The slides emphasize that:

> Mining frequent itemsets is the most expensive and important part of the process.
> 

---

## Step 1 – Generating Frequent Itemsets

This step identifies all itemsets that satisfy:

support(X)≥minsupsupport(X) \ge minsup

support(X)≥minsup

The algorithm:

- Starts with single items (1-itemsets)
- Iteratively builds larger itemsets
- Uses the **Apriori principle** to prune candidates

Only frequent itemsets survive.

Example:

If minsup = 30%,

only itemsets appearing in at least 30% of transactions are kept.

This step greatly reduces the search space.

---

## Step 2 – Generating Association Rules

From each frequent itemset LLL, all possible rules of the form:

$X \rightarrow L \setminus X$

are generated, where $X \subset L$

Example:

From frequent itemset {milk, bread, butter}, we can generate:

- {milk, bread} → {butter}
- {milk, butter} → {bread}
- {bread, butter} → {milk}

Each rule is evaluated using **confidence**.

---

## Step 3 – Applying Support and Confidence Thresholds

A rule is considered **strong** if it satisfies both:

$support(X \cup Y) \ge minsup$

$confidence(X \rightarrow Y) \ge minconf$

Rules that do not meet these thresholds are discarded.

This ensures that:

- Rules are statistically meaningful
- They are not based on rare events

---

## Summary

Association rule mining proceeds as:

1. Discover frequent itemsets using support
2. Generate candidate rules
3. Filter rules using confidence

This two-phase approach makes it possible to find meaningful patterns efficiently in large transactional databases.