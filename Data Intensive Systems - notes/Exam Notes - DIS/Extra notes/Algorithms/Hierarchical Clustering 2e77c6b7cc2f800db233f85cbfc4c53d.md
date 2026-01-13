# Hierarchical Clustering

## Hierarchical Clustering

### Term definition table

| Term | Definition |
| --- | --- |
| Hierarchical Clustering | An **unsupervised** method that builds a **tree of clusters** (hierarchy) showing how data points group together. |
| Dendrogram | A tree diagram that shows how clusters merge or split. |
| Agglomerative | Bottom-up approach (start with single points and merge). |
| Divisive | Top-down approach (start with one cluster and split). |
| Linkage | Rule for measuring distance between clusters. |
| Single Linkage | Uses closest pair between clusters. |
| Complete Linkage | Uses farthest pair between clusters. |
| Average Linkage | Uses average distance between all pairs. |
| Ward’s Method | Minimizes increase in within-cluster variance. |

---

### Definition about the algorithm

**Hierarchical Clustering** builds a nested hierarchy of clusters without needing to specify K in advance.

The most common version, **agglomerative clustering**, starts with every point as its own cluster and repeatedly merges the closest clusters until only one cluster remains.

---

### Advantages / disadvantages

**Advantages**

- No need to predefine the number of clusters.
- Produces a visual structure (dendrogram).
- Works with any distance metric.
- Can find clusters of different shapes and sizes.

**Disadvantages**

- Computationally expensive.
- Sensitive to noise and outliers.
- Once clusters are merged or split, it cannot be undone.
- Not suitable for very large datasets.

---

### Math equation

### Distance between clusters (Complete linkage example)

$D(A, B) = \max_{x \in A, y \in B} d(x, y)$

### Ward’s linkage

$\Delta E = \frac{|A||B|}{|A| + |B|} \|\mu_A - \mu_B\|^2$

---

### Runtime

Let:

- n = number of data points

**Training**

- Best: $O(n^2)$
- Worst: $O(n^3)$

**Prediction**

- Not applicable (clustering is done once)

---

### Python-like pseudo code

```python
defhierarchical_clustering(X):
    clusters = [[x]for xin X]

whilelen(clusters) >1:
        i, j = find_closest_clusters(clusters)
        new_cluster = clusters[i] + clusters[j]
        remove clusters iand j
        add new_cluster

return clusters
```

---

### Step-by-step through the algorithm (Agglomerative)

1. Treat every data point as its own cluster.
2. Compute distances between all clusters.
3. Find the two closest clusters.
4. Merge them into one cluster.
5. Update the distance matrix.
6. Repeat until only one cluster remains.
7. Use the dendrogram to choose the number of clusters.