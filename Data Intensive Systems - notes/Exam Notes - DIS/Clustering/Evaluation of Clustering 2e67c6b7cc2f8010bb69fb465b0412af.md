# Evaluation of Clustering

- What is good clustering
- Intra-cluster vs inter-cluster similarity
- Ground truth vs no ground truth
- Rand Index
- Adjusted Rand Index (ARI)
- Purity
- Normalized Mutual Information (NMI)
- Silhouette score

## **1. The Concept Logic**

Since Clustering is **Unsupervised**, we don't have a "Correct Answer" key to check against. So how do we know if our Spotify playlists are actually good?

- **Parent Topic:** [Clustering Fundamentals](Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)

We measure two main qualities:

1. **Cohesion:** Are songs in the "Rock" playlist actually similar? (Inner quality).
2. **Separation:** Is "Rock" distinct from "Jazz"? (Outer quality).

---

## **2. Internal Metrics (No Labels Needed)**

These metrics use the data geometry itself. You don't need to know the "True Genres".

### **A. SSE (Sum of Squared Error)**

Also called "Cohesion" or "Internal Variance".

- **Formula:** Sum of squared distances from every point to its cluster centroid.
- **Interpretation:**
    - **Lower is Better.**
    - **0** = Every point sits exactly on the centroid (Perfect, but likely overfitting).
    - **Use Case:** The **Elbow Method** for K-Means.

### **B. Silhouette Score**

Measures both Cohesion (a*a*) and Separation (b*b*) for a single point.

- a*a* = Average distance to own cluster (Cohesion).
- b*b* = Average distance to *neighbor* cluster (Separation).

**Formula:**

$S = \frac{b - a}{\max(a, b)}$

- **Interpretation:**
    - **+1:** Perfect! Far from neighbors, close to friends.
    - **0:** On the border/Overlapping.
    - **1:** Wrong assignment. Closer to neighbor than to own cluster.

---

## **3. External Metrics (Labels Required)**

These metrics are cheated—we use them only when **testing** our algorithm on data where we *actually know* the answers (Ground Truth), to benchmark performance.

### **A. Entropy**

Measures randomness/chaos.

- **Goal:** Low Entropy (Pure clusters).
- **Spotify Ex:** If a playlist is 50% Pop and 50% Metal, Entropy is High (Bad). If 100% Pop, Entropy is 0 (Good).

### **B. Purity**

The percent of the cluster belonging to the dominant class.

- *Warning:* Purity is easy to "game". If you make 1 cluster per song, Purity is 100% (Perfect), but use useless.

### **C. Rand Index (RI)**

Similar to "Accuracy" in Classification. Ideally 1.0 (100%).

$RI = \frac{TP + TN}{\text{All Pairs}}$

- **TP (True Positive):** Two similar songs put in same cluster. (Correct).
- **TN (True Negative):** Two different songs put in different clusters. (Correct).

### **D. F-Measure**

Combining Precision and Recall. Used if we care more about finding specific relationships than just overall sorting.