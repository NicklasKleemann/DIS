# Deriving Association Rules from Frequent Itemsets

## Deriving Association Rules from Frequent Itemsets

- Rule generation from itemsets
- Computing confidence
- Computing lift
- Filtering strong rules

# Deriving Association Rules from Frequent Itemsets

## Key Terms

| Term | Definition |
| --- | --- |
| Frequent itemset | An itemset whose support is at least the minimum support threshold. |
| Association rule | An implication of the form $X \rightarrow Y$, where X and Y are disjoint itemsets. |
| Antecedent (X) | The left-hand side of a rule. |
| Consequent (Y) | The right-hand side of a rule. |
| Confidence | The probability that Y occurs given that X has occurred. |
| Lift | A measure of how much more often X and Y occur together than expected under independence. |
| Strong rule | An association rule that satisfies both minimum support and minimum confidence. |

---

## Rule Generation from Itemsets

Once all frequent itemsets are found, association rules are generated.

For every frequent itemset L:

- All non-empty subsets $X \subset L$ are considered
- A rule is formed:

$X \rightarrow L \setminus X$

Example:

If $L = \{milk, bread, butter\}$, possible rules include:

- $\{milk, bread\} \rightarrow \{butter\}$
- $\{milk\} \rightarrow \{bread, butter\}$
- $\{butter\} \rightarrow \{milk, bread\}$

---

## Computing Confidence

For a rule $X \rightarrow Y$, confidence is:

$confidence(X \rightarrow Y) = \frac{support(X \cup Y)}{support(X)}$

It measures:

> Among all transactions that contain X, how many also contain Y.
> 

High confidence means the rule is reliable.

---

## Computing Lift

Lift measures how useful the rule is compared to random chance:

$lift(X \rightarrow Y) = \frac{confidence(X \rightarrow Y)}{support(Y)}$

Interpretation:

- Lift > 1 → positive correlation
- Lift = 1 → independence
- Lift < 1 → negative correlation

Lift helps avoid rules that are confident but not interesting.

---

## Filtering Strong Rules

A rule is kept if:

$support(X \cup Y) \ge minsup$

$confidence(X \rightarrow Y) \ge minconf$

Rules that fail these conditions are removed.

Often, lift is also used to rank or further filter the rules.

---

## Summary

Frequent itemsets provide the raw material for rule mining.

Rules are generated, evaluated using confidence and lift, and only strong, meaningful rules are retained.