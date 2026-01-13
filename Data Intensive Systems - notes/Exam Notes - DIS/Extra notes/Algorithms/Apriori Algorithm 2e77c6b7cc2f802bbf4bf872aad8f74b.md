# Apriori Algorithm

## Apriori Algorithm

### Term definition table

| Term | Definition |
| --- | --- |
| Apriori Algorithm | A classic algorithm for **mining frequent itemsets** and **association rules** from transaction data. |
| Transaction | A set of items purchased or occurring together. |
| Itemset | A group of items. |
| Support | Fraction of transactions that contain an itemset. |
| Minimum Support | Threshold for frequent itemsets. |
| Confidence | Probability that B occurs when A occurs. |
| Lift | Strength of an association rule. |
| Candidate Set | Potential frequent itemsets. |
| Frequent Itemset | Itemset that meets minimum support. |
| Apriori Principle | All subsets of a frequent itemset must also be frequent. |

---

### Definition about the algorithm

The **Apriori Algorithm** finds **frequent itemsets** in large transaction databases by using the **Apriori principle** to prune the search space.

It then uses these itemsets to generate **association rules** such as *“If A is bought, B is likely to be bought.”*

---

### Advantages / disadvantages

**Advantages**

- Simple and easy to understand.
- Effective for small to medium datasets.
- Uses pruning to reduce computation.

**Disadvantages**

- Requires multiple scans of the database.
- Slow for large datasets.
- Generates many candidate itemsets.
- High memory usage.

---

### Math equation

### Support

$total transactionssupport(X) = \frac{\text{number of transactions containing } X}{\text{total transactions}}$

### Confidence

$support(A)confidence(A \to B) = \frac{support(A \cup B)}{support(A)}$

### Lift

$lift(A \to B) = \frac{confidence(A \to B)}{support(B)}$

---

### Runtime

Let:

- n = number of transactions
- m = number of unique items

**Worst case**

$O(2^m)$

(because all possible itemsets may need to be checked)

---

### Python-like pseudo code

```python
defapriori(transactions, min_support):
    L1 = frequent_1_itemsets(transactions, min_support)
    L = [L1]
    k =2

while L[k-2] != []:
        Ck = generate_candidates(L[k-2])
        Lk = filter_by_support(Ck, transactions, min_support)
        L.append(Lk)
        k +=1

return L
```

---

### Step-by-step through the algorithm

1. Scan the database to find frequent 1-itemsets.
2. Generate candidate 2-itemsets.
3. Remove those below minimum support.
4. Generate candidate 3-itemsets from frequent 2-itemsets.
5. Prune candidates using the Apriori principle.
6. Repeat until no new frequent itemsets are found.
7. Use frequent itemsets to generate association rules.