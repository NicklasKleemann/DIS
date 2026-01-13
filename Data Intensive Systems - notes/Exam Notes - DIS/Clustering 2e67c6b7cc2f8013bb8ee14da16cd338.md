# Clustering

[Learning Paradigms](Clustering/Learning%20Paradigms%202e67c6b7cc2f807b848acc0720001172.md)

[**Clustering Fundamentals**](Clustering/Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)

[k-Means Clustering](Clustering/k-Means%20Clustering%202e67c6b7cc2f800091ebd2d1983b4136.md)

[Hierarchical Clustering](Clustering/Hierarchical%20Clustering%202e67c6b7cc2f80d095b1ff341350320f.md)

[**DBSCAN (Density-Based Spatial Clustering)**](Clustering/DBSCAN%20(Density-Based%20Spatial%20Clustering)%202e67c6b7cc2f8035924bf5c910d7c99f.md)

[Evaluation of Clustering](Clustering/Evaluation%20of%20Clustering%202e67c6b7cc2f8010bb69fb465b0412af.md)

[Choosing a Clustering Method](Clustering/Choosing%20a%20Clustering%20Method%202e67c6b7cc2f800e9ba0cf0bb1643e1c.md)

# **Clustering: Definitions**

> Context: This document aggregates all key terms, comparison tables, and logical structures from the Clustering documentation suite. It serves as a single "Cheat Sheet" for definitions. Parent Hub: Clustering Algorithm Hub
> 

---

## **1. Master Definitions Table**

| Term | Formal Definition | Spotify "Golden Thread" Analogy |
| --- | --- | --- |
| **Cluster** | A subset of objects where intra-cluster distance is minimized and inter-cluster distance is maximized. | A specific playlist (e.g., "Heavy Metal") where all songs sound alike. |
| **Centroid** | The geometric mean (average) of all points in a cluster. | The "perfect average song" of a genre (does not have to be a real song). |
| **Outlier (Noise)** | A point that does not fit well into any cluster. | A weird avant-garde track that sounds like a lawnmower. |
| **Dendrogram** | A tree diagram showing the taxonomic relationship between clusters. | A "Family Tree" of music genres (Music -> Rock -> Punk). |
| **SSE** | Sum of Squared Error (Distance from points to their centroid). | How "messy" a playlist is. Low SSE = very consistent vibe. |
| **Core Point** | A point with ≥≥ MinPts neighbors within radius ϵ*ϵ*. | The "Hit Song" that defines the genre. |
| **Border Point** | A point with < MinPts neighbors but within reach of a Core point. | The "Bridge Song" or B-side that loosely fits the genre. |
| **K-Means** | Partitioning algorithm that minimizes variance (SSE) using K*K* centroids. | Moving 3 pins around the map until they settle in the center of 3 genre clouds. |
| **Hierarchical** | Agglomerative algorithm building a nested tree structure. | Merging songs pair-by-pair to reconstruct the history of music genres. |
| **DBSCAN** | Density-based algorithm that finds arbitrary shapes and isolates noise. | Finding strict "underground scenes" and ignoring mainstream radio noise. |

---

## **2. Fundamental Comparisons**

### **Classification vs. Clustering**

| Feature | Classification (Supervised) | Clustering (Unsupervised) |
| --- | --- | --- |
| **Labels** | **Pre-defined** (e.g., "Spam" vs "Accurate"). | **None** (We discover labels). |
| **Training** | **Yes** (Train on labeled data). | **No** (Algorithm explores data directly). |
| **Goal** | Assign new object to *existing* class. | Group objects into *new* classes. |
| **Spotify Ex** | "Is this song Explicit? (Yes/No)" | "What genres exist in this database?" |

### **Inter-cluster vs. Intra-cluster Use**

| Goal | Description | Spotify Example |
| --- | --- | --- |
| **Intra-cluster Similarity** (Cohesion) | Items *inside* a cluster should be very similar. | All songs in the "Metal" playlist should be loud and fast. |
| **Inter-cluster Similarity** (Separation) | Clusters should be distinct/far apart from *other* clusters. | "Metal" playlist should sound very different from "Lullaby" playlist. |

---

## **3. Algorithm Selection Matrix**

Which algorithm should you use?

| Feature | **K-Means** | **Hierarchical** | **DBSCAN** |
| --- | --- | --- | --- |
| **Input Required** | K (Number of clusters) | None (Cut tree later) | ϵ (Radius), MinPts |
| **Shape Limit** | **Spherical** (Blobs) only | Depends on Linkage | **Arbitrary** (Rings, snakes) |
| **Outliers** | **Sensitive** (Bad) | Can handle (depends on linkage) | **Great** (Marks as Noise) |
| **Complexity** | **Fast** $(O(N))$ | **Slow** $(O(N2))$ | **Medium** $(O(Nlog⁡N))$ |
| **Best For...** | General partitioning, known K | Taxonomies, small data | Noisy data, complex shapes |

---

## **4. Specific Algorithm Details**

### **K-Means: Weaknesses & Fixes**

| Weakness | Description | The Fix |
| --- | --- | --- |
| **Local Optima** | If you pick bad starting points, you get bad clusters. | **Run Multiple Times:** Run it 10 times with different random starts and pick the best one. |
| **Outliers** | One "Lawnmower Sound" (Outlier) can pull the "Pop" centroid miles away. | **Pre-process:** Remove outliers before running K-Means. |
| **Choosing K** | We often don't know if there are 3 genres or 5. | **Elbow Method:** Plot SSE vs K and find the bend. |

### **Hierarchical: Linkage Criteria**

| Linkage Type | Definition | Effect/Shape |
| --- | --- | --- |
| **Single Link** (Min) | Distance between the **closest** two points. | **"Chain" Effect:** Good for snake-like shapes. Sensitive to noise. |
| **Complete Link** (Max) | Distance between the **furthest** two points. | **Compact Spheres:** Forces tight, round clusters. |
| **Average Link** | Average distance between all pairs. | **Balanced:** Compromise between Single and Complete. |
| **Ward's Method** | Merge pair minimizing **SSE** increase. | **Compact:** Most common, behaves like K-Means. |

### **DBSCAN: Point Classification**

| Point Type | Condition | Role |
| --- | --- | --- |
| **Core Point** | Neighbors ≥ MinPts within *ϵ*. | The dense interior of a cluster.Start of a new group. |
| **Border Point** | Neighbors < MinPts, but neighbor of Core. | The edge of the cluster. Assigned to the Core's group. |
| **Noise Point** | Neither Core nor Border. | **Discarded**. Does not belong to any cluster. |

---

## **5. Evaluation Metrics**

| Metric | Formula/Logic | Interpretation |
| --- | --- | --- |
| **Silhouette Score** |  $S = \frac{b - a}{\max(a, b)}$
$a$: Cohesion
$b$: Separation | **+1:** Perfect.
**0:** Overlapping.
**-1:** Wrong. |
| **SSE (Sum Sq Error)** | Sum of squared dists to centroid. | **Lower is better**. Used for Elbow Method. |
| **Rand Index (RI)** | $Accuracy = \frac{TP + TN}{All Pairs}$ | **0.0 - 1.0**. Measures agreement with ground truth. |
| **Purity** | % of dominant class in cluster. | Hard to use (Making 1 cluster per point gives 100% purity). |

# **Clustering: Spotify Song Segmentation**

## **1. System Map & Context**

- **Context:** Part of **Unsupervised Learning** (Machine Learning). Used when we have *data* but *no labels* (no specific "correct answer" to train on).
- **Input:** Raw data objects (e.g., Songs, Customers, Sensors).
- **Output:** Disjoint groups (Clusters) where items are *similar* to each other and *dissimilar* to others.
- 🔗 **Dependency:** Relates to **Big Data "Variety"** (see [Foundation of datasystems](Foundation%20of%20Data%20Systems%202e37c6b7cc2f805bb00dda7f622ed3a8.md)): handling unstructured/complex data often requires clustering to find structure.

> The Golden Thread: Spotify Song Segmentation Throughout this document, we are building a Spotify Auto-Categorizer.
> 
> - **Goal:** Automatically group millions of songs into "Mood Playlists" (e.g., "Chill", "Workout", "Party") without human inputs.
> - **Data Points (P*P*):** Each song is a 2D point:
>     - x: **Tempo** (0-200 BPM)
>     - y: **Energy** (0.0 Low - 1.0 High)

---

## **2. Definitions & Goals**

> 👉 Deep Dive: [Clustering Fundamentals](Clustering/Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)
> 

### **Classification vs. Clustering (Exam Critical)**

| Feature | Classification (Supervised) | Clustering (Unsupervised) |
| --- | --- | --- |
| **Labels** | **Pre-defined** (e.g., "Spam" vs "Accurate"). | **None** (We discover labels). |
| **Training** | **Yes** (Train on labeled data). | **No** (Algorithm explores data directly). |
| **Goal** | Assign new object to *existing* class. | Group objects into *new* classes. |
| **Spotify Ex** | "Is this song Explicit? (Yes/No)" | "What genres exist in this database?" |

### **Definitions Table**

| Term | Formal Definition | ELI5 (Spotify Example) |
| --- | --- | --- |
| **Cluster** | A subset of objects where intra-cluster distance is minimized and inter-cluster distance is maximized. | A specific playlist (e.g., "Heavy Metal") where all songs sound alike. |
| **Centroid** | The geometric mean (average) of all points in a cluster. | The "perfect average song" of a genre (does not have to be a real song). |
| **Outlier** | A point that does not fit well into any cluster. | A weird avant-garde track that sounds like a lawnmower. |
| **Dendrogram** | A tree diagram showing the taxonomic relationship between clusters. | A "Family Tree" of music genres (Music -> Rock -> Punk). |
| **SSE** | Sum of Squared Error (Distance from points to their centroid). | How "messy" a playlist is. Low SSE = very consistent vibe. |

### **System Goals**

| Goal | Description | Trade-off |
| --- | --- | --- |
| **Cohesion** | Items inside a cluster should be very similar. | **Overfitting:** If too cohesive, you get 1,000 tiny clusters (1 playlist per song). |
| **Separation** | Clusters should be distinct/far apart. | **Generalization:** If too separated, you might merge distinct genres (Rock + Metal) into one. |
| **Interpretability** | Clusters must make business sense. | **Complexity:** Mathematical optimals (weird shapes) might not be human-readable. |

---

## **3. Topic Walkthrough**

### **A. Preprocessing (The Foundation)**

**The Problem:** Raw data often has different scales. Tempo is 0-200, Energy is 0-1. **The Naive Approach:** Calculate Euclidean distance directly.

- *Fail:* A change of 1.0 in Energy is massive (0% to 100%), but numeric distance is just "1". A change of 1 BPM is tiny, but numeric distance is also "1". Tempo dominates the distance; Energy is ignored. **The Solution:** **Scaling** (Normalization/Standardization).
- **Min-Max Scaling:** Squishes everything to [0, 1]. (Good for image pixel data).
- **Standard Scaler (Z-Score):** Centers around 0 with Variance=1. (Good for Gaussian data).
- *Golden Thread:* Scale both Tempo and Energy to a 0-1 range so they contribute equally.

---

### **B. K-Means Clustering for Playlists**

> 👉 Deep Dive: [K-Means Algorithm & Elbow Method](Clustering/k-Means%20Clustering%202e67c6b7cc2f800091ebd2d1983b4136.md)
> 

**The Concept Logic**

- **The Problem:** We want to partition *N* songs into exactly *K* playlists.
- **The Solution:** Iteratively move *K* centers until they stabilize.
- **Golden Thread:** Place *K*=3 random dots on the Tempo/Energy graph. Move them until they sit in the middle of "Pop", "Rock", and "Jazz".

**The Decision Tree**

> If you know KK (or can guess it) AND data is globular (spherical blobs) →→ Use K-Means. If data has arbitrary shapes (Crescents, Rings) →→ Do NOT use K-Means (Use DBSCAN).
> 

**The Algorithm (Step-by-Step Solver)**

1. **Pick K:** Decide number of clusters (e.g., *K*=2).
2. **Initialize:** Pick *K* random points as initial centroids (*C*1,*C*2).
3. **Assign:** For every song point *Pi*:
    
    Pi
    
    - Calculate distance to $*C_1*$: $d_1 = \sqrt{(x_i - x_{c1})^2 + (y_i - y_{c1})^2}$
    - Calculate distance to $*C_2*$: *d*2=…
    - Assign *Pi* to closest Centroid.
4. **Update:** Recalculate Centroids.
    
    $New C_1 = (\text{Average } x \text{ of all points in } C_1, \text{Average } y \text{ of points})$.
    
5. **Repeat:** Steps 3-4 until centroids stop moving (Convergence).

**Weaknesses (Exam Warnings)**

- **Local Optima:** Bad random initialization = Bad results. (Fix: Run multiple times).
- **Outliers:** Mean is sensitive to outliers. One "Lawnmower Song" pulls the whole Pop centroid away.

**Elbow Method (Finding K)**

- Plot **SSE** (y-axis) vs **K** (x-axis).
- Look for the "Elbow" where the drop flattens out.
- *Logic:* Adding more clusters always reduces error, but after the elbow, you're just splitting coherent groups for tiny gains.

---

### **C. Hierarchical Clustering (The Taxonomy)**

> 👉 Deep Dive: [Hierarchical & Dendrograms](Clustering/Hierarchical%20Clustering%202e67c6b7cc2f80d095b1ff341350320f.md)
> 

**The Concept Logic**

- **The Problem:** We don't know *K*, and we want a structure (Genres have Sub-genres).
- **The Solution:** **Agglomerative Clustering** (Bottom-Up). Start with *N* clusters (every song is a cluster) and merge the closest pair.
- **Golden Thread:** Merge "Song A" and "Song B" -> "Pop Cluster". Merge "Pop Cluster" and "Rock Cluster" -> "Mainstream Cluster".

**The Decision Tree**

> If you need a hierarchy/tree structure → Use Hierarchical. If dataset is massive → Avoid (Complexity is $O(N^3)$ or $O(N^2)$, slow)
> 

**Likage Criteria (Measuring Distance Between Clusters)** When merging Cluster A (Pop) and Cluster B (Rock), how do we measure distance?

1. **Single Link (Min):** Distance between the **closest** two points.
    - *Effect:* Creates long, "chain-like" clusters. Good for non-spherical shapes. Sensitive to noise.
2. **Complete Link (Max):** Distance between the **furthest** two points.
    - *Effect:* Creates tight, compact spherical clusters.
3. **Average Link:** Average distance between all pairs.
4. **Ward's Method:** Merges the pair that minimizes the increase in **SSE** (Variance).
    - *Effect:* Creates very compact, similar-sized clusters (like K-Means but hierarchical). Default choice in many libraries.

**The Algorithm (Dendrogram Reading)**

1. **Construct Matrix:** Calculate distance between ALl pairs.
2. **Merge:** Find smallest distance. Combine into new cluster.
3. **Update Matrix:** Recalculate distance from New Cluster to all existing clusters.
4. **Repeat:** Until 1 giant cluster remains.
5. **Cut:** Draw a horizontal line on the Dendrogram to choose specific *K*.
    
    K
    
    - *Exam Tip:* The "Best" K is usually where the vertical lines crossed are longest (largest gap between merges).

---

### **D. DBSCAN (The Niche Finder)**

> 👉 Deep Dive: [DBSCAN & Density](Clustering/DBSCAN%20(Density-Based%20Spatial%20Clustering)%202e67c6b7cc2f8035924bf5c910d7c99f.md)
> 

**The Concept Logic**

- **The Problem:** K-Means fails on "weird shapes" (e.g., a "Ring" of songs surrounding a central genre). It also forces outliers into clusters.
- **The Solution:** Density-Based Spatial Clustering. Clusters are regions of high density.
- **Golden Thread:** Identify a "Mainstream Pop" core. If a song is close enough, it's in. If a song is far away from everyone, it's **Noise** (ignore it).

**The Decision Tree**

> If you have noise/outliers → Use DBSCAN. If clusters have irregular shapes (not circles) → Use DBSCAN. If density varies strictly (some clusters sparse, some dense) → DBSCAN struggles.
> 

**Key Parameters**

- **ϵ*ϵ* (Eps):** The "Reach" radius. How close considers "neighbors"?
- **MinPts:** Minimum neighbors to consider a "Core" point.

**Point Types**

1. **Core Point:** Has ≥ MinPts neighbors within radius *ϵ*. (The "Hit Song").
2. **Border Point:** Has < MinPts neighbors, but belongs to a Core point's neighborhood. (The "Bridge" song).
3. **Noise:** Neither Core nor Border. (The "Garbage").

**Reachability vs Connectivity (Exam Nuance)**

- **Directly Density-Reachable:** *A*→*B* (A is Core, B is in A's circle). *Not symmetric* (B might not be Core).
- **Density-Reachable:** Chain of direct reaches ($*A→C→D*$).
- **Density-Connected:** $*B←A→C*$. B and C are connected because they share a Core ancestor A. *Symmetric*. (**Rule:** Clusters form based on this).

**The Algorithm (Step-by-Step)**

1. Pick an unvisited point *P*.
2. Count neighbors within *ϵ* distance.
3. **If Neighbors < MinPts:** Mark as **Noise** (might change later).
4. **If Neighbors ≥ MinPts:** Mark as **Core**. Start a New Cluster.
    - Add all neighbors to cluster.
    - Recursively check *their* neighbors (if they are also Core, expand cluster).
5. Repeat until all points visited.

---

## **4. Comparisons & Trade-offs**

### **Algorithm Comparison**

| Feature | K-Means | Hierarchical | DBSCAN |
| --- | --- | --- | --- |
| **Input Required** | K (Number of clusters) | None (Cut tree later) | *ϵ*, MinPts |
| **Shape Limit** | Spherical (Convex) only | Depends on Linkage | Arbitrary shapes |
| **Outliers** | Forces them into clusters (Bad) | Can handle (depends) | **Great** (Marks as Noise) |
| **Complexity** | Fast $(O(N))$ | Slow $(O(N2))$ | Medium ($O(N\log⁡N))$ |
| **Best For...** | General purpose, simple partitioning | Taxonomies, small data | Noisy data, complex shapes |

### **Evaluation Metrics (Is the playlist good?)**

| Metric | Formula/Logic | Interpretation |
| --- | --- | --- |
| **Silhouette Score** | $S = \frac{b - a}{\max(a, b)}$
$*a*$: Cohesion, 
$*b*$: Separation | **+1:** Perfect.
**0:** Overlapping.
**-1:** Wrong. |
| **SSE (Sum Sq Error)** | Sum of squared dists to centroid. | **Lower is better**. Used for Elbow Method. |
| **Rand Index (RI)** | $Accuracy = \frac{TP + TN}{All Pairs}$ | **0 - 1**. Measures agreement with ground truth. |
| **Adjusted RI (ARI)** | Corrected for random chance. | **0.0:** Random guessing (Bad).
**1.0:** Perfect Match. |
| **Purity** | % of dominant class in cluster. | Hard to use (Making 1 cluster per point gives 100% purity). |

---

## **5. Exam Checklist (The "Cheat Code")**

1. **Preprocessing?** Always check if data needs Normalization (Scaling) first.
2. **Choosing Algo?**
    - Arbitrary Shapes/Noise? → **DBSCAN**.
    - Taxonomy needed? → **Hierarchical**.
    - Fixed *K* / Speed needed? → **K-Means**.
3. **Dendo-Cut?** To get *K* clusters from a Dendrogram, draw a horizontal line that intersects *K* vertical lines. Look for the *longest* vertical drop.
4. **K-Means Update?** New Centroid is simply the average (*x*,*y*) of all current points.