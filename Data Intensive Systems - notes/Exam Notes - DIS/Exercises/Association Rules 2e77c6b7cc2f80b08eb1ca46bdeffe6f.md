# Association Rules

# Exercise 1: Support Bounds

> *Refer to the transaction table (1000 rows). Say sup(ab) = 100.*
> 
> - Determine the possible values of sup(a)
> - Determine the possible values of sup(abc)

## Key Concept: Apriori Property

```python
If itemset X is a subset of itemset Y, then:
    sup(Y) ≤ sup(X)
```

Because: Every transaction containing Y must also contain X

## Solution

**Given: $sup(ab)=100$** (meaning 100 transaction contain both a and b)

## Part 1: Possible values of sup(a)

```python
Since {ab} ⊆ {a} is FALSE (a is subset of ab)
Actually: {a} ⊆ {ab} is also FALSE

Correct relationship: {ab} contains {a}
So every transaction with {ab} must have {a}

Therefore: sup(a) ≥ sup(ab)
           sup(a) ≥ 100

Upper bound: sup(a) ≤ 1000 (total transactions)
```

**Answer: $sup(a)\ge100$**

*Why $sup(a) = 70$ is NOT possible:* If only 70 transactions contain 'a', then at most 70 transactions can contain 'ab'. But $sup(ab) = 100 > 70$, contradiction!

## Part 2: Possible values of $sup(abc)$

```python
{abc} is a superset of {ab}
Every transaction with {abc} must have {ab}

Therefore: sup(abc) ≤ sup(ab)
           sup(abc) ≤ 100

Lower bound: sup(abc) ≥ 0
```

**Answer: $sup(abc)\le100$**

*Why $sup(abc) = 120$  is NOT possible:* If 120 transactions contain 'abc', then at least 120 must contain 'ab'. But $sup(ab) = 100 < 120$, contradiction!

# Exercise 2: Association Rules on Store Data

> Use `mlxtend` library to find frequent itemsets and association rules on store_data.csv (7501 transactions, max 20 items each)
> 

## Sample Data Format

```python
shrimp,almonds,avocado,vegetables mix,green grapes,...
burgers,meatballs,eggs
chutney
turkey,avocado
```

## Pseudocode

```python
FUNCTION association_rule_mining(transactions, min_support, min_confidence):
    // Step 1: Convert to binary matrix
    FOR each transaction:
        FOR each item in transaction:
            matrix[transaction_id][item] = 1
    
    // Step 2: Find frequent itemsets (Apriori)
    frequent_itemsets = []
    k = 1
    WHILE candidates exist:
        candidates = generate_candidates(size=k)
        FOR each candidate:
            IF support(candidate) >= min_support:
                frequent_itemsets.ADD(candidate)
        k += 1
    
    // Step 3: Generate association rules
    rules = []
    FOR each itemset in frequent_itemsets:
        FOR each non-empty subset A of itemset:
            B = itemset - A
            confidence = support(itemset) / support(A)
            IF confidence >= min_confidence:
                rules.ADD(A → B)
    
    RETURN frequent_itemsets, rules
```

## Python Implementation

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# =============================================================================
# Load and Prepare Data
# =============================================================================

# Read CSV (each row is a transaction)
transactions = []
with open('store_data.csv', 'r') as f:
    for line in f:
        items = [item.strip() for item in line.strip().split(',') if item.strip()]
        transactions.append(items)

print(f"Total transactions: {len(transactions)}")
print(f"Sample transaction: {transactions[0][:5]}...")

# =============================================================================
# Convert to Binary Matrix
# =============================================================================

te = TransactionEncoder()
te_array = te.fit_transform(transactions)
df = pd.DataFrame(te_array, columns=te.columns_)

print(f"\nBinary matrix shape: {df.shape}")
print(df.head())

# =============================================================================
# Find Frequent Itemsets (Apriori)
# =============================================================================

# min_support = 0.01 means itemset appears in at least 1% of transactions
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

print(f"\nFrequent Itemsets (min_support=0.01):")
print(f"Total found: {len(frequent_itemsets)}")
print(frequent_itemsets.sort_values('support', ascending=False).head(10))

# =============================================================================
# Generate Association Rules
# =============================================================================

rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.3)

print(f"\nAssociation Rules (min_confidence=0.3):")
print(f"Total rules: {len(rules)}")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

# =============================================================================
# Filter Interesting Rules
# =============================================================================

# High confidence rules
high_conf = rules[rules['confidence'] > 0.5]
print(f"\nHigh Confidence Rules (>0.5):")
print(high_conf[['antecedents', 'consequents', 'confidence', 'lift']])

# High lift rules (strong association)
high_lift = rules[rules['lift'] > 2]
print(f"\nHigh Lift Rules (>2):")
print(high_lift[['antecedents', 'consequents', 'confidence', 'lift']])
```

## Expected Output

**Total transactions:** 7501
**Sample transaction:** ['shrimp', 'almonds', 'avocado', 'vegetables mix', 'green grapes']

**Binary matrix shape: $(7501, 120)$**

**Frequent Itemsets $(min_support=0.01)$:**

| support | itemsets |
| --- | --- |
| 0.238368 | (mineral water) |
| 0.174243 | (eggs) |
| 0.167578 | (spaghetti) |

| antecedents | consequents | support | confidence | lift |
| --- | --- | --- | --- | --- |
| (spaghetti) | (mineral water) | 0.0593 | 0.354 | 1.48 |
| (chocolate) | (mineral water) | 0.0527 | 0.328 | 1.37 |

## Metrics Explaination

| Metric | Formula | Interpretation |
| --- | --- | --- |
| **Support** | P(A∪B) | How often items appear together |
| **Confidence** | P(B|A) = sup(AB)/sup(A) | How often rule is true |
| **Lift** | P(B|A)/P(B) | How much A increases likelihood of B |

```
Lift = 1: Independent
Lift > 1: Positive association
Lift < 1: Negative association
```

---

## Complete Pipeline Summary

```python
# Quick reference pipeline
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# 1. Prepare data
te = TransactionEncoder()
df = pd.DataFrame(te.fit_transform(transactions), columns=te.columns_)

# 2. Find frequent itemsets
freq = apriori(df, min_support=0.01, use_colnames=True)

# 3. Generate rules
rules = association_rules(freq, metric='confidence', min_threshold=0.3)

# 4. Analyze
print(rules.sort_values('lift', ascending=False))
```