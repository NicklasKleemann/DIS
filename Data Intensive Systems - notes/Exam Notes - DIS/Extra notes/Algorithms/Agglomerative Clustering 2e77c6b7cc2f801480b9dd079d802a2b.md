# Agglomerative Clustering

## Agglomerative Clustering

### Term definition table

| Term | Definition |
| --- | --- |
| Agglomerative Clustering | A **bottom-up hierarchical** clustering algorithm that merges the closest clusters step by step. |
| Cluster | A group of similar data points. |
| Dendrogram | Tree that shows how clusters are merged. |
| Linkage | Rule used to measure distance between clusters. |
| Single Linkage | Distance between closest points of two clusters. |
| Complete Linkage | Distance between farthest points of two clusters. |
| Average Linkage | Average distance between all pairs. |
| Ward’s Method | Merges clusters that cause the smallest increase in variance. |
| Distance Matrix | Table storing distances between clusters. |

---

### Definition about the algorithm

**Agglomerative Clustering** starts with each data point as its own cluster and repeatedly merges the two closest clusters until all points are in one cluster.

The result is a **hierarchy of clusters**, visualized using a **dendrogram**.

---

### Advantages / disadvantages

**Advantages**

- No need to choose K in advance.
- Produces a dendrogram for visualization.
- Works with any distance metric.
- Can discover complex cluster structures.

**Disadvantages**

- Slow for large datasets.
- Sensitive to noise.
- Merges cannot be undone.
- Requires storing full distance matrix.

---

### Math equation

### Complete linkage

$D(A,B) = \max_{x \in A, y \in B} d(x,y)$

### Single linkage

$D(A,B) = \min_{x \in A, y \in B} d(x,y)$

### Ward’s linkage

$\Delta E = \frac{|A||B|}{|A|+|B|} \|\mu_A - \mu_B\|^2$

---

### Runtime

Let:

- n = number of data points

**Training**

- Best: $O(n^2)$
- Worst: $O(n^3)$

**Prediction**

- Not applicable

---

### Python-like pseudo code

```python
defagglomerative_clustering(X):
    clusters = [[x]for xin X]

whilelen(clusters) >1:
        i, j = find_closest_clusters(clusters)
        clusters[i] = clusters[i] + clusters[j]
        remove clusters[j]

return clusters
```

---

### Step-by-step through the algorithm

1. Start with each data point as its own cluster.
2. Compute distances between all clusters.
3. Find the two closest clusters.
4. Merge them.
5. Update the distance matrix.
6. Repeat until one cluster remains.
7. Use the dendrogram to select final clusters.