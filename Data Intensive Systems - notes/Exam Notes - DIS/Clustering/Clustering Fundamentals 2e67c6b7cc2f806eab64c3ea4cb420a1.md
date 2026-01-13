# Clustering Fundamentals

- What is clustering
- Similarity and distance
- Inter-cluster vs intra-cluster similarity
- Classification vs clustering
- Basic steps of clustering
- Preprocessing and scaling

# **Clustering Fundamentals**

## **1. What is Clustering?**

**Clustering** is a technique in *Unsupervised Learning* where the goal is to group a set of objects in such a way that objects in the same group (called a **cluster**) are more similar to each other than to those in other groups (clusters).

- **Input:** Raw data objects (e.g., Songs, Customers, Sensors) without labels.
- **Output:** Disjoint groups based on inherent structure.
- **Parent Topic:** See [**Learning Paradigms**](Learning%20Paradigms%202e67c6b7cc2f807b848acc0720001172.md).

> The Golden Thread: Spotify Auto-Categorizer
> 
> - **Goal:** Automatically sort millions of songs into "Mood Playlists" without a human tagging them.
> - **Data:** We only know the *features* (Tempo, Energy, etc.), not the *genre*.

---

## **2. Classification vs. Clustering (Exam Critical)**

| Feature | Classification (Supervised) | Clustering (Unsupervised) |
| --- | --- | --- |
| **Labels** | **Pre-defined** (e.g., "Spam" vs "Accurate"). | **None** (We discover labels). |
| **Training** | **Yes** (Train on labeled data). | **No** (Algorithm explores data directly). |
| **Goal** | Assign new object to *existing* class. | Group objects into *new* classes. |
| **Spotify Ex** | "Is this song Explicit? (Yes/No)" | "What genres exist in this database?" |

---

## **3. Core Concepts & Definitions**

### **Similarity and Distance**

To group things, we must mathematically define "similar". In most algorithms, **Similarity = 1 / Distance**. If distance is small, similarity is high.

**Euclidean Distance (The Standard)** For two points $P1(x1,y1)$and $P2(x2,y2)$(e.g., Song A and Song B):

$d(P_1, P_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

### **Inter-cluster vs. Intra-cluster**

Defining "Good" clusters involves two competing forces:

| Goal | Description | Spotify Example |
| --- | --- | --- |
| **Intra-cluster Similarity** (Cohesion) | Items *inside* a cluster should be very similar. | All songs in the "Metal" playlist should be loud and fast. |
| **Inter-cluster Similarity** (Separation) | Clusters should be distinct/far apart from *other* clusters. | "Metal" playlist should sound very different from "Lullaby" playlist. |

> Trade-off:
> 
> - **Too much Cohesion:** You get 1,000 tiny clusters (1 playlist per song).
> - **Too much Separation:** You merge distinct genres (Rock + Metal) into one generic blob.

### **Key Termiunology**

| Term | Formal Definition | Spotify Analogy |
| --- | --- | --- |
| **Centroid** | The geometric mean (average) of all points in a cluster. | The "perfect average song" of a genre. |
| **Outlier** | A point that does not fit well into any cluster. | A weird avant-garde track that sounds like a lawnmower. |
| **Dendrogram** | A tree diagram showing hierarchical relationships. | A "Family Tree" of music genres. |

---

## **4. The Basic Clustering Process**

Most clustering workflows follow these four steps:

1. **Preprocessing & Scaling:** Prepare the data (Crutial Step!).
2. **Choose Algorithm:** Decide between Partitioning (K-Means), Hierarchical, or Density-based (DBSCAN).
3. **Run Algorithm:** Execute the math to assign points to clusters.
4. **Evaluate:** Use metrics (Silhouette Score, SSE) to interpret if the clusters make sense.

---

## **5. Preprocessing & Scaling (The Foundation)**

**The Problem:** Raw data often has different scales.

- **Tempo:** 0 to 200 BPM.
- **Energy:** 0.0 to 1.0.

**The Naive Failure:** If you calculate Euclidean distance directly:

- A change of 1.0 in Energy is massive (0% to 100%), but numeric distance is just "1".
- A change of 1 BPM is tiny, but numeric distance is also "1".
- **Result:** Tempo dominates the distance calculation; Energy is ignored.

**The Solution: Scaling (Normalization)** We must scale all features to the same range so they contribute equally.

- **Min-Max Scaling:** Squishes everything to [0, 1].
    - *Formula:* $X_{new} = \frac{X - X_{min}}{X_{max} - X_{min}}$
- **Standard Scaler (Z-Score):** Centers around 0 with Variance=1.

> Golden Thread Application: We scale Tempo variables so that "150 BPM" becomes "0.75". Now it is comparable to Energy's "0.8".
>