# K-Nearest Neighbors (KNN)

## K-Nearest Neighbors (KNN)

### Term definition table

| Term | Definition |
| --- | --- |
| K-Nearest Neighbors (KNN) | A **lazy, instance-based** algorithm that classifies a data point based on the labels of its **K closest** training points. |
| Neighbor | A training data point close to the query point. |
| Distance Metric | A function that measures similarity between points (e.g., Euclidean, Manhattan). |
| Euclidean Distance | Straight-line distance in feature space. |
| Manhattan Distance | Sum of absolute coordinate differences. |
| K | Number of neighbors used for voting. |
| Majority Vote | The class that appears most among the K neighbors. |
| Weighted Voting | Neighbors closer to the query point get more influence. |
| Feature Scaling | Normalizing features so distances are meaningful. |
| Lazy Learning | No model is trained; all work is done at prediction time. |

---

### Definition about the algorithm

**K-Nearest Neighbors** classifies a new data point by finding the **K closest labeled points** in the training set and assigning the class that appears most frequently among them.

KNN does **no training** in advance — it simply stores the data and performs computation when a prediction is needed.

---

### Advantages / disadvantages

**Advantages**

- Very simple and intuitive.
- No training phase.
- Can model very complex decision boundaries.
- Works well when similar points have similar labels.
- Easy to update with new data.

**Disadvantages**

- Very slow for large datasets.
- Requires storing the entire dataset.
- Sensitive to noise and irrelevant features.
- Sensitive to the choice of K.
- Requires feature scaling.
- Curse of dimensionality reduces performance.

---

### Math equation

### Euclidean distance

$d(x, y) = \sqrt{\sum_{i=1}^{d} (x_i - y_i)^2}$

### Manhattan distance

$d(x, y) = \sum_{i=1}^{d} |x_i - y_i|$

### Weighted voting

If neighbor iii has distance did_idi, weight:

$w_i = \frac{1}{d_i^2}$

Final class:

$\hat{y} = \arg\max_c \sum_{i \in K, y_i = c} w_i$

---

### Runtime

Let:

- n = number of training points
- d = number of features
- k = number of neighbors

**Prediction**

| Case | Runtime |
| --- | --- |
| Best | O(n) |
| Worst | $O(n \cdot d)$ |

Because distance must be computed to **all points**.

**Training**

- O(1) (just store the data)

---

### Python-like pseudo code

```python
defknn_predict(X_train, y_train, x, k):
    distances = []

for iinrange(len(X_train)):
        d = distance(X_train[i], x)
        distances.append((d, y_train[i]))

    distances.sort(key=lambda t: t[0])
    neighbors = distances[:k]

    votes = {}
for d, labelin neighbors:
        votes[label] = votes.get(label,0) +1

returnmax(votes, key=votes.get)
```

---

### Step-by-step through the algorithm

1. Store all training data.
2. Choose the value of K.
3. For a new data point x:
4. Compute the distance between x and **every** training point.
5. Sort all distances.
6. Select the **K smallest** distances (the nearest neighbors).
7. Collect the class labels of these K neighbors.
8. Perform **majority voting** (or weighted voting).
9. Assign the winning class to x.