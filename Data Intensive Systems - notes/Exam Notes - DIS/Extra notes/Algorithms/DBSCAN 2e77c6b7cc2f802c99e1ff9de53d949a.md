# DBSCAN

## DBSCAN

### Term definition table

| Term | Definition |
| --- | --- |
| DBSCAN | **Density-Based Spatial Clustering of Applications with Noise** – a clustering algorithm that groups dense regions and labels sparse points as noise. |
| ε (Eps) | Radius used to define the neighborhood around a point. |
| MinPts | Minimum number of points required to form a dense region. |
| Core Point | A point with at least MinPts neighbors within ε. |
| Border Point | A point that is close to a core point but not dense enough itself. |
| Noise (Outlier) | A point that is neither core nor border. |
| Density Reachable | A point that can be reached from a core point via neighbors. |
| Density Connected | Two points connected through a chain of core points. |

---

### Definition about the algorithm

**DBSCAN** finds clusters by identifying **dense areas** of data points separated by **low-density regions**.

It does not require the number of clusters in advance and naturally identifies **outliers**.

---

### Advantages / disadvantages

**Advantages**

- Does not require choosing K.
- Can find arbitrarily shaped clusters.
- Automatically detects outliers.
- Robust to noise.

**Disadvantages**

- Difficult to choose good ε and MinPts.
- Performs poorly on datasets with varying density.
- Not ideal for very high-dimensional data.

---

### Math equation

A point ppp is a **core point** if:

$|N_\varepsilon(p)| \ge \text{MinPts}$

Where:

$N_\varepsilon(p) = \{q \mid d(p,q) \le \varepsilon \}$

---

### Runtime

Let:

- n = number of data points

**With spatial index (k-d tree, R-tree)**

- Best: $O(n \log n)$
- Worst: $O(n \log n)$

**Without index**

- Best & Worst: $O(n^2)$

---

### Python-like pseudo code

```python
defdbscan(X, eps, minPts):
    labels = [UNVISITED] *len(X)
    cluster_id =0

for iinrange(len(X)):
if labels[i] != UNVISITED:
continue

        neighbors = region_query(X, i, eps)

iflen(neighbors) < minPts:
            labels[i] = NOISE
else:
            cluster_id +=1
            expand_cluster(X, labels, i, neighbors, cluster_id, eps, minPts)

return labels
```

```python
defexpand_cluster(X, labels, i, neighbors, cluster_id, eps, minPts):
    labels[i] = cluster_id

for jin neighbors:
if labels[j] == NOISE:
            labels[j] = cluster_id
if labels[j] != UNVISITED:
continue

        labels[j] = cluster_id
        new_neighbors = region_query(X, j, eps)

iflen(new_neighbors) >= minPts:
            neighbors.extend(new_neighbors)
```

---

### Step-by-step through the algorithm

1. Choose ε and MinPts.
2. Pick an unvisited point.
3. Find all points within ε.
4. If fewer than MinPts → mark as noise.
5. If it is a core point → create a new cluster.
6. Add all density-reachable points to this cluster.
7. Repeat until all points are processed.
8. Output clusters and noise points.