# C-Means (Fuzzy)

## C-Means (Fuzzy C-Means)

### Term definition table

| Term | Definition |
| --- | --- |
| Fuzzy C-Means (FCM) | A **soft clustering** algorithm where each point belongs to **multiple clusters** with different degrees of membership. |
| Cluster | A group of similar data points. |
| Membership Value | Degree (between 0 and 1) that a point belongs to a cluster. |
| C | Number of clusters. |
| Fuzzifier (m) | Controls how fuzzy the clustering is (typically m=2). |
| Centroid | Weighted center of a cluster. |
| Objective Function | Function minimized by the algorithm. |
| Convergence | When membership values stop changing significantly. |

---

### Definition about the algorithm

**Fuzzy C-Means** assigns each data point a **degree of belonging** to every cluster instead of assigning it to exactly one cluster.

This is useful when clusters **overlap** and boundaries are not clearly defined.

---

### Advantages / disadvantages

**Advantages**

- More flexible than K-Means.
- Handles overlapping clusters well.
- Produces richer information via membership values.

**Disadvantages**

- Slower than K-Means.
- Sensitive to noise.
- Requires choosing C and fuzzifier m.
- May converge to local minima.

---

### Math equation

### Membership update

$u_{ij} =
\frac{1}{\sum_{k=1}^{C}
\left(\frac{d_{ij}}{d_{ik}}\right)^{\frac{2}{m-1}}}$

Where:

- $u_{ij}$ = membership of point i in cluster j
- $d_{ij}$ = distance between point i and centroid j

### Centroid update

$c_j =
\frac{\sum_{i=1}^{n} u_{ij}^m x_i}
{\sum_{i=1}^{n} u_{ij}^m}$

---

### Runtime

Let:

- n = number of points
- d = dimensions
- c = number of clusters
- i = iterations

**Best & Worst**

$O(ncd i)$

---

### Python-like pseudo code

```python
deffuzzy_c_means(X, c, m=2, max_iters=100):
    U = random_membership(len(X), c)

for _inrange(max_iters):
        centroids = []
for jinrange(c):
            centroids.append(weighted_mean(X, U[:, j], m))

for iinrange(len(X)):
for jinrange(c):
                U[i][j] = compute_membership(X[i], centroids, j, m)

return centroids, U
```

---

### Step-by-step through the algorithm

1. Choose number of clusters C and fuzzifier m.
2. Initialize membership values randomly.
3. Compute cluster centroids using weighted means.
4. Update membership values.
5. Repeat steps 3–4 until convergence.
6. Output clusters and membership matrix.