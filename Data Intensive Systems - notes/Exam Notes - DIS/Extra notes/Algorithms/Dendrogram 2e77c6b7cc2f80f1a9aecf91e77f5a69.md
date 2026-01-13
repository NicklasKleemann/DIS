# Dendrogram

## Dendrogram

### Term definition table

| Term | Definition |
| --- | --- |
| Dendrogram | A **tree diagram** that shows how clusters are merged or split in hierarchical clustering. |
| Leaf | A single data point at the bottom of the tree. |
| Branch | A merge between two clusters. |
| Height | Distance at which two clusters are merged. |
| Cut | A horizontal line used to select clusters. |
| Linkage | Rule used to compute distances between clusters. |
| Agglomerative | Bottom-up hierarchical clustering that produces dendrograms. |
| Cluster | Group of points below a cut. |

---

### Definition about the concept

A **dendrogram** visualizes the entire **hierarchical clustering process**.

It shows **when** and **at what distance** clusters were merged, allowing you to choose the number of clusters by drawing a horizontal cut across the tree.

---

### Advantages / disadvantages

**Advantages**

- Visual and intuitive.
- No need to specify number of clusters beforehand.
- Shows relationships between clusters.

**Disadvantages**

- Hard to read for large datasets.
- Sensitive to distance metric and linkage.
- Requires hierarchical clustering to generate.

---

### Math equation

The height of a merge is given by the **linkage distance**, e.g. (complete linkage):

$D(A,B) = \max_{x \in A, y \in B} d(x,y)$

---

### Runtime

The dendrogram has the same runtime as hierarchical clustering:

- Best: $O(n^2)$
- Worst: $O(n^3)$

---

### Python-like pseudo code

```python
defbuild_dendrogram(X):
    clusters = [[x]for xin X]
    history = []

whilelen(clusters) >1:
        i, j, dist = find_closest_clusters(clusters)
        history.append((clusters[i], clusters[j], dist))
        clusters[i] = clusters[i] + clusters[j]
        remove clusters[j]

return history
```

---

### Step-by-step through the concept

1. Perform hierarchical clustering.
2. Each data point starts as a leaf.
3. Closest clusters are merged step by step.
4. Each merge becomes a branch.
5. The height shows the distance.
6. Draw a horizontal cut.
7. Each branch below the cut is a cluster.