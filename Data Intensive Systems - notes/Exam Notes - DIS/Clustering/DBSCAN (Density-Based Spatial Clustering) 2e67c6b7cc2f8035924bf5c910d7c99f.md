# DBSCAN (Density-Based Spatial Clustering)

- Density-based clustering
- Core points
- Eps-neighborhood
- Density-reachable
- Density-connected
- Noise points
- DBSCAN algorithm
- Hyperparameters (Eps, MinPts)

## **1. The Concept Logic**

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) groups points that are closely packed together, marking points that lie alone in low-density regions as **outliers**.

- **Goal:** Find "dense" regions regardless of shape.
- **Parent Topic:** [Clustering Fundamentals](Clustering%20Fundamentals%202e67c6b7cc2f806eab64c3ea4cb420a1.md)

> The Spotify Golden Thread
> 
> - **Scenario:** We want to find specific sub-genres like "Norwegian Death Metal" (Dense tight group) but ignore weird experimental noise tracks.
> - **Action:** Look for "Neighborhoods" of songs. If a song has 5 friends nearby, it starts a genre. If a song has no friends, it's **Noise** (ignore it).

---

## **2. Key Parameters**

You must set two numbers:

1. **ϵ*ϵ* (Eps):** The **Radius**. "How far does my arm reach to find neighbors?"
2. **MinPts:** The **density threshold**. "How many neighbors do I need to be considered a Core point?"

---

## **3. Point Classifications**

Every point becomes one of three types:

1. **Core Point:** $Has ≥ MinPts$ neighbors within Eps radius. (The "Center of the Party").
2. **Border Point:** $Has < MinPts$ neighbors, BUT is within the radius of a Core point. (The "Sidekick" - part of the cluster, but on the edge).
3. **Noise Point:** Neither Core nor Border. (The "Loner").

---

## **4. The Algorithm (Step-by-Step)**

1. Pick a random unvisited point.
2. Check its radius ($*ϵ*$).
3. **If Neighbors < MinPts:** Label as **Noise** (Check later, might become Border).
4. **If Neighbors ≥≥ MinPts:** It is a **Core Point**. Create a **New Cluster**.
    - Add all its neighbors to the cluster.
    - **Expand:** Check *those* neighbors. If they are also Core, add *their* neighbors too. (Chain reaction).
5. Repeat until all points are visited.

---

## **5. Reachability (Exam Nuance)**

- **Directly Density-Reachable:** Point A is Core, Point B is in A's radius. ($*A→B*$).
- **Density-Reachable:** Chain of connections ($*A→C→D→E*$).
- **Density-Connected:** Two border points ($*B and C*$) might share the same Core parent ($*A*$). They are connected ($*B←A→C*$).

> Why it matters: This chaining allow DBSCAN to find Arbitrary Shapes (like S-shapes or rings) because the cluster just "snakes" along the density path.
> 

---

## **6. The Decision Tree (When to use?)**

> ✅ USE IF:
> 
> - Data has **Noise/Outliers** (DBSCAN handles them perfectly).
> - Clusters have **Weird Shapes “Non convex”** (Concentic rings, crescents).
> - You **don't** know K.

> ❌ AVOID IF:
> 
> - **Varying Density:** If Cluster A is very tight (dense) and Cluster B is very loose (spread out), you can't find a single $*ϵ*$ that works for both.
> - **High Dimensions:** In very high dimensions, "distance" stops meaning anything (Curse of Dimensionality).