# k-Means Clustering

- Partitioning approach
- K-means algorithm
- Initialization and convergence
- Choosing K
- Elbow method
- Weaknesses of k-means
- Outliers and non-convex shapes

# **k-Means Clustering**

## **1. The Concept Logic**

**K-Means** is a *partitioning* algorithm that splits the data into K*K* non-overlapping subsets (clusters). It tries to find "spherical" blobs of data.

- **Goal:** Minimize the distance between points and their assigned cluster center (Centroid).
- **Parent Topic:** [Clustering Fundamentals](Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)

> The Spotify Golden Thread
> 
> - **Scenario:** We want to create exactly **3 Playlists** (Pop, Rock, Jazz).
> - **Action:** We place 3 random dots on our graph. We move them around until they sit perfectly in the center of the three main clouds of songs.

---

## **2. The Algorithm (Step-by-Step)**

The algorithm is iterative. It repeats until the centroids stop moving (Convergence).

1. **Pick K:** Decide the number of clusters (e.g., $*K=3*$).
2. **Initialize:** Select $*K*$ random points as initial **Centroids**.
3. **Assign (E-Step):** For every data point (Song):
    - Calculate distance to all $*K*$ centroids.
    - Assign the point to the **closest** centroid.
4. **Update (M-Step):** Recalculate the Centroids.
    - New Centroid = The **Average** $(x,y)$ of all points currently assigned to that cluster.
5. **Repeat:** Go back to Step 3. Stop if centroids don't change.

> Exam Tip: The "New Centroid" is literally just the mean. If a cluster has points (2,2) and (4,4), the new centroid is (3,3).
> 

---

## **3. The Decision Tree (When to use?)**

> ✅ USE IF:
> 
> - You verify that the data is "Globular" (Blob-shaped).
> - You know *K* in advance (or can estimate it).
>     
>     K
>     
> - You need speed (It's *O*(*N*), very fast).
>     
>     O(N)
>     

> ❌ AVOID IF:
> 
> - Data has complex shapes (Rings, moons, spirals).
> - Data has many **Outliers** (K-Means is very sensitive to noise).
> - Clusters have different sizes/densities.

---

## **4. Weaknesses & Fixes**

| Weakness | Description | The Fix |
| --- | --- | --- |
| **Local Optima** | If you pick bad starting points, you get bad clusters. | **Run Multiple Times:** Run it 10 times with different random starts and pick the best one (Lowest SSE). |
| **Outliers** | One "Lawnmower Sound" (Outlier) can pull the "Pop" centroid miles away. | **Pre-process:** Remove outliers before running K-Means. |
| **Choosing K** | We often don't know if there are 3 genres or 5. | **Elbow Method:** (See below). |

---

## **5. The Elbow Method (Finding K)**

How do we pick the perfect K*K*?

1. Run K-Means with *K*=1, calculate **SSE** (Total Error).
2. Run with $*K=2,*$ calculate SSE.
3. Run with $*K=3…10.*$
4. **Plot:** SSE (y-axis) vs *K* (x-axis).
5. **Find the Elbow:** The graph will drop rapidly and then flatten out. The **"Elbow Point"** (the angle) is the optimal *K*.

> Logic: Adding more clusters always reduces error (if K=NK=N, error is 0). But after the elbow, you are splitting meaningful groups into tiny irrelevant fragments.
>