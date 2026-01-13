# Density-based detection

## Density-Based Detection (Anomaly Detection)

### Term definition table

| Term | Definition |
| --- | --- |
| Density-Based Detection | An **outlier detection** method that identifies points in **low-density regions**. |
| Density | Number of data points in a region. |
| Neighborhood | Set of points within a given radius. |
| Core Region | High-density area. |
| Sparse Region | Area with few data points. |
| Outlier | A point in a sparse region. |
| ε-neighborhood | Points within distance ε. |
| Threshold | Minimum density required to be normal. |

---

### Definition about the algorithm

**Density-based detection** identifies anomalies by measuring how **dense** the area around a point is.

Points located in **sparse regions** compared to the rest of the data are considered **outliers**.

---

### Advantages / disadvantages

**Advantages**

- Detects outliers in unevenly distributed data.
- Works without labeled data.
- Can find local anomalies.

**Disadvantages**

- Sensitive to parameter choices.
- Computationally expensive.
- Struggles in high-dimensional data.

---

### Math equation

Density of point ppp:

$density(p) = |N_\varepsilon(p)|$

Outlier if:

$density(p) < \tau$

Where:

- $Nε(p) = ε-neighborhood$
- $\tau$ = density threshold

---

### Runtime

Let:

- n = number of points

**Best & Worst**

$O(n^2)$

---

### Python-like pseudo code

```python
def density_outliers(X, eps, threshold):
     outliers = []

 for iinrange(len(X)):
         neighbors =0
  for jinrange(len(X)):
   if distance(X[i], X[j]) <= eps:
                  neighbors +=1

   if neighbors < threshold:
              outliers.append(i)

return outliers
```

---

### Step-by-step through the algorithm

1. Choose ε and density threshold.
2. For each data point, find neighbors within ε.
3. Count number of neighbors.
4. If count is below threshold, mark as outlier.
5. Output all outliers.