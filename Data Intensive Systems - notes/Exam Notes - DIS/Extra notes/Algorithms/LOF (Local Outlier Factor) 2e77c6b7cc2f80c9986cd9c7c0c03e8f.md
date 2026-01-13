# LOF (Local Outlier Factor)

## LOF (Local Outlier Factor)

### Term definition table

| Term | Definition |
| --- | --- |
| Local Outlier Factor (LOF) | An **anomaly detection** algorithm that measures how isolated a point is compared to its neighbors. |
| Outlier | A data point that is very different from its surrounding points. |
| k-distance | Distance to the k-th nearest neighbor. |
| k-nearest neighbors | The k closest data points to a given point. |
| Reachability Distance | Smoothed distance used to avoid instability. |
| Local Reachability Density (LRD) | Density of a point based on its neighbors. |
| LOF Score | Ratio of neighbor densities to the point’s density. |
| Inlier | A normal data point. |

---

### Definition about the algorithm

**LOF** identifies outliers by comparing the **local density** of a point to the densities of its neighbors.

If a point lies in a much less dense region than its neighbors, it is considered an **outlier**.

---

### Advantages / disadvantages

**Advantages**

- Detects **local** anomalies (not just global ones).
- Works well when data density varies.
- No need to assume data distribution.

**Disadvantages**

- Sensitive to choice of k.
- Computationally expensive.
- Struggles in high-dimensional data.

---

### Math equation

### Reachability distance

$reach\_dist_k(p,o) = \max(k\text{-distance}(o), d(p,o))$

### Local reachability density (LRD)

$LRD_k(p) =
\left(
\frac{\sum_{o \in N_k(p)} reach\_dist_k(p,o)}{|N_k(p)|}
\right)^{-1}$

### LOF score

$LOF_k(p) =
\frac{\sum_{o \in N_k(p)} \frac{LRD_k(o)}{LRD_k(p)}}{|N_k(p)|}$

If LOF>1LOF > 1LOF>1, point is an outlier.

---

### Runtime

Let:

- n = number of points
- d = dimensions

**Best**

$O(n \log n)$

(using spatial index)

**Worst**

$O(n^2)$

---

### Python-like pseudo code

```python
def lof(X, k):
     distances = compute_knn_distances(X, k)
     lrd = compute_lrd(X, distances)
 
     lof_scores = []
 for iinrange(len(X)):
         score =0
 for jin neighbors(i):
             score += lrd[j] / lrd[i]
         lof_scores.append(score / k)

return lof_scores
```

---

### Step-by-step through the algorithm

1. Choose k (number of neighbors).
2. For each point, find its k-nearest neighbors.
3. Compute reachability distances.
4. Compute local reachability density (LRD).
5. Compare LRD of each point with its neighbors.
6. Compute LOF score.
7. If LOF ≫ 1, mark as outlier.