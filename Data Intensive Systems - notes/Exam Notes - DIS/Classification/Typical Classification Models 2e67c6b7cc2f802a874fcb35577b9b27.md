# Typical Classification Models

- Rule-based classifier
- Decision trees
- Random forest
- K-Nearest Neighbors (KNN)
- Eager vs lazy learning
- Overfitting

# Typical Classification Models

Classification models differ in:

- How they learn from data
- How they store knowledge
- How they make predictions

The slides group classifiers into **rule-based, tree-based, instance-based, and ensemble models**.

---

## Rule-Based Classifier

A **rule-based classifier** represents a model as a set of **if–then rules**.

General form:

```
IF condition1 AND condition 2 THEN class = C
```

Rules are learned from training data and applied sequentially.

### Properties

- Very **interpretable**
- Easy to understand and explain
- Works well when classes can be separated by clear logical conditions

### Limitations

- Hard to model complex or overlapping data
- Can grow large and hard to maintain

---

## Decision Trees

A **decision tree** is a tree-structured model where:

- Internal nodes test an attribute
- Branches represent test outcomes
- Leaf nodes represent class labels

Example (Iris):

- Test petal length
- Then test petal width
- Then predict species

Decision trees:

- Automatically create rules from data
- Are easy to visualize
- Can model non-linear decision boundaries

### Weakness

They tend to **overfit** when trees become too deep.

---

## Random Forest

A **random forest** is an ensemble of many decision trees.

Each tree:

- Is trained on a random subset of data
- Uses a random subset of features

Predictions are made by **voting** across all trees.

### Why it works

- Reduces overfitting
- Increases stability
- Handles noisy data well

Random forests are usually more accurate than a single decision tree.

---

## K-Nearest Neighbors (KNN)

KNN is an **instance-based classifier**.

To classify a new data point:

1. Find the **k closest training points**
2. Let them vote on the class
3. Choose the most common class

Distance is typically measured using:

- Euclidean distance (for numeric data)

### Properties

- No explicit training phase
- All training data must be stored
- Very sensitive to:
    - Noise
    - Data scaling

---

## Eager vs Lazy Learning

| Eager Learning | Lazy Learning |
| --- | --- |
| Builds a model during training | Does not build a model |
| Examples: Decision trees, Random forest | Example: KNN |
| Fast prediction | Slow prediction |
| More preprocessing | Minimal preprocessing |

KNN is lazy because it waits until a query arrives.

Decision trees are eager because they build a model in advance.

---

## Overfitting

Overfitting happens when a model:

- Fits training data too well
- Learns noise instead of patterns

An overfitted model:

- Has very high training accuracy
- Performs poorly on unseen data

Decision trees are especially prone to overfitting when:

- They become too deep
- They create too many rules

Random forests reduce overfitting by:

- Averaging many trees
- Using randomness

---

## Summary

Different classifiers trade off:

- Interpretability
- Accuracy
- Speed
- Sensitivity to noise

Understanding their strengths and weaknesses is essential for model selection.