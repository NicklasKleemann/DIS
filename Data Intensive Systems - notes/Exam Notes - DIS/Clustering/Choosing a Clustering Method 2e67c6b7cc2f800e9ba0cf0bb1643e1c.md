# Choosing a Clustering Method

- When to use k-means
- When to use hierarchical clustering
- When to use DBSCAN
- Data shape
- Noise and outliers
- Unknown number of clusters

## **1. The Decision Matrix**

Which algorithm should you use for your dataset?

| Feature | **K-Means** | **Hierarchical** | **DBSCAN** |
| --- | --- | --- | --- |
| **Input Required** | K*K* (Number of clusters) | None (Cut tree later) | ϵ*ϵ* (Radius), MinPts |
| **Shape Limit** | **Spherical** (Blobs) only | Depends on Linkage | **Arbitrary** (Rings, snakes) |
| **Outliers** | **Sensitive** (Bad) | Can handle (depends on linkage) | **Great** (Marks as Noise) |
| **Complexity** | **Fast** $(O(N))$ | **Slow** $(O(N2))$ | **Medium** $(O(N log⁡ N))$ |
| **Best For...** | General partitioning, known K | Taxonomies, small data | Noisy data, complex shapes |

---

## **2. Exam Decision Checklist**

Follow this logic flow to answer "Design a System" questions.

### **Question 1: Do we know the number of clusters?**

- **Yes:** Lean towards **K-Means**.
- **No:** Lean towards **Hierarchical** or **DBSCAN**.

### **Question 2: How big is the data?**

- **Massive (Big Data):** **K-Means** (Partitioning). Hierarchical will crash.
- **Small/Medium:** Hierarchical is acceptable.

### **Question 3: What is the shape of the data?**

- **Globular (Blobs):** **K-Means** is fine.
- **Roads, Rivers, Rings:** **DBSCAN**. K-Means will cut a "Ring" shape in half linearly, which is wrong.

### **Question 4: Is there noise?**

- **System must be robust:** **DBSCAN** explicitly isolates noise.
- **Clean data:** K-Means is fine.

### **Question 5: Do we need a taxonomy?**

- **"Build a family tree of biology":** Must use **Hierarchical**.

---

## **3. Spotify Case Study Application**

**Scenario A: "Daily Mix" Generation**

- *Need:* Fast, grouping millions of songs into "Morning", "Workout", "Evening".
- *Choice:* **K-Means**. (Fast, *K* is set by UI design).

**Scenario B: "Genre Discovery"**

- *Need:* Map the evolution of Rock music from 1950 to 2020.
- *Choice:* **Hierarchical**. (We want to see Sub-genres splitting off from parent genres).

**Scenario C: "Niche Detection"**

- *Need:* Find very specific, tight-knit communities of "Viking Metal" fans, ignoring casual listeners.
- *Choice:* **DBSCAN**. (Finds dense cores, ignores the 'noise' of mainstream listeners).