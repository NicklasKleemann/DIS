# Hierarchical Clustering

- Agglomerative vs divisive
- Distance matrix
- Dendrogram
- Inter-cluster similarity
- Linkage methods
- Ward’s method
- Choosing number of clusters

---

## **1. The Concept Logic**

**Hierarchical Clustering** builds a nested hierarchy of clusters. It doesn't just give you groups; it gives you a **Structure** (Taxonomy).

- **Goal:** Build a tree (Dendrogram) showing how all points relate to each other.
- **Approach:** **Agglomerative** (Bottom-Up). Start with *N* clusters, merge until 1 remains.
    
    N
    
- **Parent Topic:** [Clustering Fundamentals](Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)

> The Spotify Golden Thread
> 
> - **Scenario:** We don't just want playlists; we want a **Genre Tree**.
> - **Action:**
>     1. Merge "Song A" and "Song B" into "Soft Rock".
>     2. Merge "Soft Rock" and "Hard Rock" into "Rock".
>     3. Merge "Rock" and "Pop" into "Mainstream".

---

## **2. The Algorithm (Agglomerative)**

1. **Start:** Treat every single data point as its own cluster. (If $*N=100*$, you have 100 clusters).
2. **Calculate Matrix:** Measure distance between **ALL** pairs of clusters.
3. **Merge:** Find the two **closest** clusters and combine them into one.
4. **Update:** You now have $*N−1*$ clusters. Recalculate distances.
5. **Repeat:** Keep merging until only **1 Giant Cluster** remains.

---

## **3. Linkage Criteria (How to measure distance?)**

When we merge "A Single Point" with a "Group of 5 Points", how do we measure distance?

| Linkage Type | Definition | Effect/Shape |
| --- | --- | --- |
| **Single Link** (Min) | Distance between the **closest** two points in the groups. | **"Chain" Effect:** Good for snake-like shapes. Risks connecting distinct blobs if there is a "bridge" of noise. |
| **Complete Link** (Max) | Distance between the **furthest** two points. | **Compact Spheres:** Forces tight, round clusters. Sensitive to outliers. |
| **Average Link** | Average distance between all pairs. | **Balanced:** Compromise between Single and Complete. |
| **Ward's Method** | Merge the pair that minimizes the increase in **Variance** (SSE). | **Most Common:** creates similar-sized, compact clusters. Behavies like K-Means. |

---

## **4. The Decision Tree (When to use?)**

> ✅ USE IF:
> 
> - You need a **Taxonomy/Hierarchy** (Biology, Library classification).
> - You don't know *K* (you can cut the tree later).
>     
>     K
>     
> - Dataset is **Small** to **Medium**.

> ❌ AVOID IF:
> 
> - **Big Data:** It is slow (*O*(*N*2) or *O*(*N*3)). If you have 1 million Spotify songs, this will crash.
>     
>     O(N2)
>     
>     O(N3)
>     

---

## **5. Reading the Dendrogram**

A **Dendrogram** is the tree diagram output.

- **X-axis:** The data points (Songs).
- **Y-axis:** The distance (dissimilarity) at which merges happened.
- **The Cut:** To turn the tree into specific clusters, draw a horizontal line across the graph.
    - If the line touches 3 vertical stems, you get $*K=3*$ clusters.

> Exam Tip (Determining K): Look for the longest vertical lines that are not crossed by horizontal merge lines. A big vertical jump means "These two groups are REALLY far apart, so we shouldn't merge them yet." That gap is the natural separation.
>