# Decision Tree (DT)

## Decision Tree (DT)

### Term definition table

| Term | Definition |
| --- | --- |
| Decision Tree | A tree-structured model that predicts a target by **recursively splitting** the data on feature tests. |
| Node | A point in the tree where a decision/split is made (internal node) or a prediction is produced (leaf). |
| Root | The first node of the tree (top). |
| Leaf | Terminal node that outputs a class label (classification) or a value (regression). |
| Split / Test | A rule like `x_j ≤ t` (numeric) or `x_j ∈ S` (categorical) that partitions the data. |
| Feature | An input variable used to split the data. |
| Threshold | A numeric cut value `t` used in a split. |
| Impurity | A measure of how “mixed” the labels are in a node (e.g., entropy, Gini). Lower is better. |
| Information Gain | Reduction in impurity achieved by a split (used in ID3/C4.5). |
| Gini Index | Impurity measure commonly used in CART. |
| Overfitting | Tree becomes too complex and fits noise; performs worse on unseen data. |
| Pruning | Reducing tree size (pre- or post-) to improve generalization. |

---

### Definition about the algorithm

A **Decision Tree classifier** learns a set of **if–then rules** by repeatedly choosing a feature split that best separates the classes.

At each node, it selects the split that maximizes “purity” (minimizes impurity). The process continues until a stopping condition is met (e.g., max depth, min samples, or pure node). A leaf predicts the **majority class** (or class distribution).

---

### Advantages / disadvantages

**Advantages**

- Easy to understand and explain (rule-like decisions).
- Handles non-linear relationships and feature interactions naturally.
- Works with numeric and categorical features.
- Minimal preprocessing (no scaling required).
- Fast inference (a few comparisons along one path).

**Disadvantages**

- Prone to overfitting without pruning/regularization.
- High variance: small data changes can produce very different trees.
- Greedy splitting can miss the globally optimal tree.
- Biased toward features with many possible split points (esp. ID3; C4.5 reduces this with gain ratio).
- Piecewise-constant decision boundaries; can underperform on smooth problems.

---

### Math equation

### 1) Entropy (ID3 / C4.5)

For a node with class proportions $kp_1, \dots, p_k$:

$H(S) = -\sum_{c=1}^{k} p_c \log_2(p_c)$

### 2) Information Gain

Split dataset SSS into subsets SvS_vSv (e.g., by feature value / threshold):

$IG(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$

### 3) Gini Impurity (CART)

$Gini(S) = 1 - \sum_{c=1}^{k} p_c^2$

### 4) Weighted impurity after split

For a split into left/right: $S_L, S_R$

$Impurity_{\text{split}} = \frac{|S_L|}{|S|}Imp(S_L) + \frac{|S_R|}{|S|}Imp(S_R)$

Choose the split that **minimizes** this.

### 5) (Optional) Cost-complexity pruning (CART idea)

$R_\alpha(T) = R(T) + \alpha \cdot |Leaves(T)|$

Trade off training error R(T) vs tree size.

---

### Runtime

Let:

- n = number of samples
- d = number of features
- Tree depth $\approx h$

**Training**

- Typical (with sorting / efficient split search): about
    
    **Best/average**: $O(n \, d \, \log n)$
    
- Worst case (very unbalanced tree or naive split scanning): up to
    
    **Worst**: $O(n^2 d)$
    

**Inference (predict one sample)**

- **Best**: O(1) (root is leaf or very shallow)
- **Worst**: O(h) comparisons (depth of tree), typically $O(\log n)$ if balanced, O(n) if extremely skewed.

---

### Python-like pseudo code

```python
deffit_decision_tree(X, y, depth=0):
# stopping conditions
if all_same_class(y):
return Leaf(class_label=y[0])
if depth >= MAX_DEPTHorlen(y) < MIN_SAMPLES_SPLIT:
return Leaf(class_label=majority_class(y))

    best_feature, best_threshold, best_score =None,None, +inf

for jinrange(num_features(X)):
for tin candidate_thresholds(X[:, j]):# e.g., midpoints of sorted unique values
            left_idx  = X[:, j] <= t
            right_idx = ~left_idx
if left_idx.sum() ==0or right_idx.sum() ==0:
continue

            score = weighted_impurity(y[left_idx], y[right_idx])# gini or entropy
if score < best_score:
                best_feature, best_threshold, best_score = j, t, score

if best_featureisNone:
return Leaf(class_label=majority_class(y))

    left_idx  = X[:, best_feature] <= best_threshold
    right_idx = ~left_idx

    left_child  = fit_decision_tree(X[left_idx],  y[left_idx],  depth +1)
    right_child = fit_decision_tree(X[right_idx], y[right_idx], depth +1)

return Node(feature=best_feature, threshold=best_threshold,
                left=left_child, right=right_child)

defpredict_one(tree, x):
    node = tree
whileisinstance(node, Node):
if x[node.feature] <= node.threshold:
            node = node.left
else:
            node = node.right
return node.class_label
```

---

### Step-by-step through the algorithm (classification)

1. **Start with all training data at the root node**.
2. **Check stopping conditions**:
    - If all labels are the same → make a **leaf**.
    - If max depth reached / too few samples / no good split → **leaf** with majority class.
3. **For each feature**, consider possible splits:
    - Numeric: try thresholds (often midpoints between sorted unique values).
    - Categorical: try partitions (implementation-dependent).
4. **Compute impurity** of the resulting child nodes (entropy or Gini).
5. **Pick the best split** (lowest weighted impurity / highest information gain).
6. **Partition the data** into left/right (or multiple) subsets using that split.
7. **Recurse**: repeat steps 2–6 for each child node.
8. **Finish** when all branches end in leaves.
9. (Optional but common) **Prune / regularize**:
    - Pre-pruning: limit depth, min samples, min impurity decrease.
    - Post-pruning: remove branches that don’t help validation performance.
10. **Prediction**: for a new sample, follow split rules from root to leaf → output leaf class.