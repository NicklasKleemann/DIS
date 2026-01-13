# Reflection on the Apriori Algorithm

## Reflection on the Apriori Algorithm

- Strengths of Apriori
- Weaknesses of Apriori
- Computational cost
- Number of database scans
- Scalability limitations

# Reflection on the Apriori Algorithm

## Key Terms

| Term | Definition |
| --- | --- |
| Apriori algorithm | A classic algorithm for mining frequent itemsets using the downward closure property. |
| Downward closure | The property that all subsets of a frequent itemset must be frequent. |
| Candidate explosion | Rapid growth in the number of candidate itemsets as itemset size increases. |
| Database scan | One full pass over the transactional dataset. |
| Scalability | The ability of an algorithm to handle increasing data size efficiently. |

---

## Strengths of Apriori

Apriori is powerful because it:

- Uses a **solid theoretical principle** (downward closure)
- Guarantees finding **all frequent itemsets**
- Prunes huge parts of the search space early
- Is easy to understand and implement

It was the first practical solution for large-scale association rule mining.

---

## Weaknesses of Apriori

Despite pruning, Apriori suffers from:

- **Candidate explosion** when many items are frequent
- High memory usage
- Large computational overhead

If minsup is low, the number of candidates becomes enormous.

---

## Computational Cost

Apriori must:

- Generate candidate itemsets
- Count their support
- Repeat this for each level

Support counting is expensive because:

- It requires scanning all transactions
- It must check many candidates per transaction

Thus, runtime increases quickly with:

- More items
- Larger datasets
- Lower minsup

---

## Number of Database Scans

Apriori performs:

- One full scan per level k

If the largest frequent itemset has size 10:

- At least 10 full database scans are required

For large datasets stored on disk, this is very slow.

---

## Scalability Limitations

Apriori does not scale well when:

- Data is huge
- Many items are frequent
- Patterns are long

Modern algorithms (e.g., FP-Growth) were developed to avoid:

- Candidate generation
- Repeated database scans

---

## Summary

Apriori is:

- The foundation of association rule mining
- Conceptually elegant
- But computationally expensive

Its main limitations are:

- Too many candidates
- Too many database scans
- Poor scalability for very large datasets