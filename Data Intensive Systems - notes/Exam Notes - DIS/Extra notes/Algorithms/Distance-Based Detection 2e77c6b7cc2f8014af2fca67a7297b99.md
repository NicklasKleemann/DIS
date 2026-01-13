# Distance-Based Detection

## Distance-Based Detection (Anomaly Detection)

### Term definition table

| Term | Definition |
| --- | --- |
| Distance-Based Detection | An **outlier detection** method that flags points that are **far away** from other points. |
| Outlier | A point whose distance to neighbors is unusually large. |
| k-nearest neighbors | The k closest points to a given point. |
| Average Distance | Mean distance from a point to its neighbors. |
| Threshold | Distance above which a point is considered an outlier. |
| Global Outlier | A point far from all others. |
| Local Outlier | A point far from its neighbors. |

---

### Definition about the algorithm

**Distance-based detection** identifies anomalies by measuring how **far a data point is from other points**.

If a point’s distance to its neighbors is much larger than normal, it is labeled an **outlier**.

---

### Advantages / disadvantages

**Advantages**

- Simple to understand.
- Works well when outliers are far away from normal data.
- No need for data distribution assumptions.

**Disadvantages**

- Computationally expensive.
- Sensitive to scaling.
- Poor performance in high dimensions.

---

### Math equation

Average distance of point ppp:

$D_k(p) = \frac{1}{k} \sum_{o \in N_k(p)} d(p,o)$

Outlier if:

$D_k(p) > \tau$

---

### Runtime

Let:

- n = number of points
- d = dimensions

**Best & Worst**

$O(n^2 d)$

---

### Python-like pseudo code

```python
def distance_outliers(X, k, threshold):
    outliers = []

for iinrange(len(X)):
        distances = []
for jinrange(len(X)):
            distances.append(distance(X[i], X[j]))

        distances.sort()
        avg =sum(distances[:k]) / k

if avg > threshold:
            outliers.append(i)

return outliers
```

---

### Step-by-step through the algorithm

1. Choose k and distance threshold.
2. For each point, compute distance to all others.
3. Find its k nearest neighbors.
4. Compute average distance.
5. If it exceeds threshold, mark as outlier.
6. Output all outliers.