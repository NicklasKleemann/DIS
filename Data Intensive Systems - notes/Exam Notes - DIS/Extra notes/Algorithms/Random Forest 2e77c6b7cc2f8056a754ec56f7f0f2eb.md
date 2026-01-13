# Random Forest

## Random Forest

### Term definition table

| Term | Definition |
| --- | --- |
| Random Forest | An **ensemble** learning algorithm that builds many decision trees and combines their predictions (usually by majority vote). |
| Ensemble | A set of models whose predictions are combined to get a better result. |
| Decision Tree (DT) | A tree-based classifier or regressor used as a base learner in the forest. |
| Bootstrap Sampling | Sampling with replacement from the training set to create different datasets for each tree. |
| Bagging (Bootstrap Aggregating) | Training multiple models on different bootstrap samples and aggregating their outputs. |
| Feature Subsampling | At each split, only a random subset of features is considered. |
| Out-of-Bag (OOB) Sample | Data points not selected in a tree’s bootstrap sample; used for validation. |
| Majority Vote | The final class chosen by the most trees. |
| Overfitting | When a model fits noise; reduced in random forests by averaging many trees. |
| Variance | How sensitive a model is to small changes in data; reduced by ensembles. |

---

### Definition about the algorithm

A **Random Forest** is a collection of **many decision trees**, where each tree is trained on a **randomly sampled version of the data** and uses **random subsets of features** at each split.

Each tree is a **weak but diverse** classifier. By combining them through **majority voting**, Random Forest achieves **high accuracy and low overfitting**.

Instead of trusting a single decision tree, we trust the **wisdom of the crowd**.

---

### Advantages / disadvantages

**Advantages**

- Much **higher accuracy** than a single decision tree.
- **Strong resistance to overfitting**.
- Works well for high-dimensional data.
- Handles non-linear relationships and feature interactions.
- Provides **feature importance** scores.
- Out-of-bag error gives built-in validation.

**Disadvantages**

- Less interpretable than a single decision tree.
- More memory and computation needed.
- Slower prediction than a single tree.
- Can struggle with extremely noisy data.

---

### Math equation

Let:

- T = number of trees
- $C_i(x)$ = class predicted by tree i for input x

### Majority vote (classification)

$\hat{y}(x) = \text{mode}\{ C_1(x), C_2(x), \dots, C_T(x) \}$

### Average (regression)

$\hat{y}(x) = \frac{1}{T} \sum_{i=1}^{T} C_i(x)$

### Out-of-Bag (OOB) error

For a data point $x_j$, use only trees that did **not** train on $x_j$ and compare their vote to the true label.

---

### Runtime

Let:

- n = number of samples
- d = number of features
- T = number of trees
- h = depth of each tree

**Training**

- **Best / typical**:

$O(T \cdot n \cdot \sqrt{d} \cdot \log n)$

(because only d\sqrt{d}d features are tested per split)

- **Worst case** (very deep trees):

$O(T \cdot n^2 \cdot d)$

**Prediction (one sample)**

- **Best**: O(T) if trees are shallow
- **Worst**: $O(T \cdot h)$

---

### Python-like pseudo code

```python
deffit_random_forest(X, y, T):
    forest = []

for iinrange(T):
        Xb, yb = bootstrap_sample(X, y)
        tree = fit_decision_tree_random_features(Xb, yb)
        forest.append(tree)

return forest

deffit_decision_tree_random_features(X, y):
# same as normal decision tree
# BUT at each split only try a random subset of features
pass

defpredict_random_forest(forest, x):
    votes = []
for treein forest:
        votes.append(predict_one(tree, x))
return majority_vote(votes)

```

---

### Step-by-step through the algorithm

1. Choose the number of trees T.
2. For each tree:
    - Randomly draw n samples from the dataset **with replacement** (bootstrap).
    - Train a **decision tree** on this dataset.
    - At each split, choose the best split **only from a random subset of features**.
3. Repeat until T trees are built.
4. To predict a new sample:
    - Send it through **all trees**.
    - Each tree outputs a class.
5. The forest returns the **majority vote** (classification) or **average** (regression).
6. (Optional) Use **out-of-bag samples** to estimate test error without cross-validation.