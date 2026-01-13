# Classification

# Exercise 1: kNN Classification

> *Given two classes: A = {(1,3), (2,2), (3.5,1), (5,4), (1.5,4), (4,2)} and B = {(2,3), (3,0.5), (4,3), (3.5,2), (1,2.5), (2,1)} and three unclassified points (4,1), (1.5,2.5) and (3,4).*
> 
> 
> *1. Use the kNN classification approach and Euclidean distance to decide the classes for the three points, for k = 1, 2, 3.* *2. Repeat 1.1 but use Manhattan distance instead.* *3. Compare the results of 1.1 and 1.2.*
> 

## Pseudocode

```python
FUNCTION knn_classify(point, training_data, k, distance_func):
    distances = []
    
    FOR each (train_point, label) in training_data:
        dist = distance_func(point, train_point)
        distances.APPEND((dist, label))
    
    SORT distances by dist (ascending)
    k_nearest = distances[0:k]
    
    // Majority vote
    count_A = COUNT labels == 'A' in k_nearest
    count_B = COUNT labels == 'B' in k_nearest
    
    IF count_A > count_B:
        RETURN 'A'
    ELSE:
        RETURN 'B'

FUNCTION euclidean_distance(p1, p2):
    RETURN SQRT((p1.x - p2.x)^2 + (p1.y - p2.y)^2)

FUNCTION manhattan_distance(p1, p2):
    RETURN |p1.x - p2.x| + |p1.y - p2.y|
```

## Python Implementation

```python
import numpy as np
from collections import Counter

# =============================================================================
# Data Setup
# =============================================================================

class_A = [(1,3), (2,2), (3.5,1), (5,4), (1.5,4), (4,2)]
class_B = [(2,3), (3,0.5), (4,3), (3.5,2), (1,2.5), (2,1)]
unclassified = [(4,1), (1.5,2.5), (3,4)]

# Combine training data with labels
training_data = [(p, 'A') for p in class_A] + [(p, 'B') for p in class_B]

# =============================================================================
# Distance Functions
# =============================================================================

def euclidean(p1, p2):
    """Euclidean: sqrt((x1-x2)^2 + (y1-y2)^2)"""
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def manhattan(p1, p2):
    """Manhattan: |x1-x2| + |y1-y2|"""
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# =============================================================================
# kNN Classifier
# =============================================================================

def knn_classify(point, training_data, k, distance_func):
    """
    Pseudocode:
        COMPUTE distances to all training points
        SORT and SELECT k nearest
        RETURN majority class
    """
    # Calculate distances
    distances = []
    for train_point, label in training_data:
        dist = distance_func(point, train_point)
        distances.append((dist, label))
    
    # Sort and get k nearest
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    
    # Majority vote
    labels = [label for _, label in k_nearest]
    vote = Counter(labels).most_common(1)[0][0]
    
    return vote, k_nearest

# =============================================================================
# Run Classification
# =============================================================================

print("=" * 60)
print("1.1 EUCLIDEAN DISTANCE")
print("=" * 60)

for k in [1, 2, 3]:
    print(f"\nk = {k}:")
    for point in unclassified:
        result, neighbors = knn_classify(point, training_data, k, euclidean)
        print(f"  Point {point} → Class {result}")

print("\n" + "=" * 60)
print("1.2 MANHATTAN DISTANCE")
print("=" * 60)

for k in [1, 2, 3]:
    print(f"\nk = {k}:")
    for point in unclassified:
        result, neighbors = knn_classify(point, training_data, k, manhattan)
        print(f"  Point {point} → Class {result}")
```

### Expected Results

(3,4) | A | A/B | A |

**Euclidian Distance**

| Point | k=1 | k=2 | k=3 |
| --- | --- | --- | --- |
| (4,1) | A | A | A |
| (1.5,2.5) | B | B | B |
| (3,4) | A | A/B | A |

**Manhattan Distance**

| Point | $k=1$ | $k=2$ | $k=3$ |
| --- | --- | --- | --- |
| (4,1) | A | A | A |
| (1.5,2.5) | B | B | B |
| (3,4) | A | A/B | A |

- Results are mostly similar between distance metrics
- Manhattan may differ at boundary cases
- Euclidean penalizes large differences more (squared)
- Manhattan treats all dimensions equally

## Exercise 1.2: Parallel kNN

> Suppose that labelled data is distributed in M sites and we need to run kNN to decide the class label for a new point at site S₀.
1. Describe a parallel algorithm for it. How much data do you need to transfer?
2. Can it make a difference whether you run local kNN at S₀ or not?
> 

### Pseudocode

```python
FUNCTION parallel_knn(query_point, k, sites[1..M]):
    // Step 1: Broadcast query to all sites
    FOR each site S_i:
        SEND query_point to S_i
    
    // Step 2: Each site computes local k-nearest
    FOR each site S_i in PARALLEL:
        local_knn[i] = find_k_nearest(query_point, local_data[i], k)
    
    // Step 3: Gather results at S_0
    all_candidates = []
    FOR each site S_i:
        RECEIVE local_knn[i]
        all_candidates.APPEND(local_knn[i])
    
    // Step 4: Final merge - find global k-nearest
    global_knn = find_k_nearest from all_candidates (M × k points)
    
    RETURN majority_vote(global_knn)
```

### Python Simulation

```python
from multiprocessing import Pool
from functools import partial

def local_knn(site_data, query_point, k, distance_func):
    """
    Each site computes its local k-nearest neighbors
    Returns: list of (distance, label) tuples
    """
    distances = []
    for point, label in site_data:
        dist = distance_func(query_point, point)
        distances.append((dist, label, point))
    
    distances.sort(key=lambda x: x[0])
    return distances[:k]

def parallel_knn(query_point, sites_data, k, distance_func, num_sites):
    """
    Pseudocode:
        1. BROADCAST query to all sites
        2. Each site computes local k-nearest
        3. GATHER M × k candidates at S_0
        4. MERGE and find global k-nearest
    """
    # Step 2: Parallel local kNN at each site
    all_candidates = []
    for site_data in sites_data:
        local_result = local_knn(site_data, query_point, k, distance_func)
        all_candidates.extend(local_result)
    
    # Step 4: Global merge
    all_candidates.sort(key=lambda x: x[0])
    global_k_nearest = all_candidates[:k]
    
    # Majority vote
    labels = [label for _, label, _ in global_k_nearest]
    return Counter(labels).most_common(1)[0][0]

# Data transfer analysis
print("DATA TRANSFER ANALYSIS:")
print(f"  Query broadcast: 1 point × M sites = M transfers")
print(f"  Results gather: k points × M sites = M×k transfers")
print(f"  Total: O(M × k) data points transferred")
```

### Answers

**Parallel Algorithm & Data Transfer**

| Step | Data Transfer |
| --- | --- |
| Broadcast query | 1 point to M sites |
| Gather local k-nearest | M × k points to S₀ |
| **Total** | **O(M × k)** points |

**Does Local kNN at $S_0$ Matter?**

YES, it can make a difference

Without local kNN at S₀:

- Only considers data from remote sites
- May miss nearest neighbors in local data

With local kNN at S₀:

- Includes local data in candidate set
- More accurate if local data contains true nearest neighbors

Recommendation: Always include S₀'s local data in the merge step

# Exercise 2: Decision Tree, Random Forest & kNN on Diabetes Dataset (Optional)

> Using the Diabetes dataset, do the following:1. Split dataset 80/20, build decision tree, evaluate accuracy, build random forest and plot important features2. Apply KNN with cross validation, test effect of scaling, try different K's with ROC curves
> 

## Psudeocode

```python
FUNCTION ml_pipeline(dataset):
    // Data preparation
    X, y = SPLIT features and labels
    X_train, X_test = SPLIT 80/20
    
    // Decision Tree
    tree = DecisionTreeClassifier()
    tree.FIT(X_train, y_train)
    accuracy = tree.SCORE(X_test, y_test)
    
    // Random Forest
    forest = RandomForestClassifier()
    forest.FIT(X_train, y_train)
    importances = forest.feature_importances_
    PLOT importances
    
    // KNN with scaling comparison
    FOR scaling in [False, True]:
        IF scaling: X = NORMALIZE(X)
        knn = KNeighborsClassifier(k=5)
        score = CROSS_VALIDATE(knn, X, y)
    
    // KNN with different K values
    FOR k in [2, 3, 4, 5, 6, 7, 8]:
        knn = KNeighborsClassifier(k)
        CROSS_VALIDATE with stratified 3-fold
        PLOT ROC curve
```

## Python Implementation

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc, accuracy_score

# =============================================================================
# Load Data
# =============================================================================

# Load diabetes dataset (example with sklearn)
from sklearn.datasets import load_diabetes
# Or: df = pd.read_csv('diabetes.csv')

df = pd.read_csv('diabetes.csv')  # Assuming CSV format
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# =============================================================================
# 1.1 Train/Test Split & Decision Tree
# =============================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Decision Tree with different parameters
print("DECISION TREE RESULTS:")
for max_depth in [3, 5, 10, None]:
    tree = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    tree.fit(X_train, y_train)
    accuracy = tree.score(X_test, y_test)
    print(f"  max_depth={max_depth}: Accuracy = {accuracy:.4f}")

# =============================================================================
# 1.2 Random Forest & Feature Importance
# =============================================================================

forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)
print(f"\nRANDOM FOREST Accuracy: {forest.score(X_test, y_test):.4f}")

# Plot feature importance
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importances (Random Forest)")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=45)
plt.tight_layout()
plt.show()

# =============================================================================
# 2.1 KNN: Effect of Scaling
# =============================================================================

print("\nKNN SCALING COMPARISON (k=5):")

# Without scaling
knn = KNeighborsClassifier(n_neighbors=5)
scores_no_scale = cross_val_score(knn, X, y, cv=5)
print(f"  Without scaling: {scores_no_scale.mean():.4f} (+/- {scores_no_scale.std():.4f})")

# With scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
scores_scaled = cross_val_score(knn, X_scaled, y, cv=5)
print(f"  With scaling:    {scores_scaled.mean():.4f} (+/- {scores_scaled.std():.4f})")

# =============================================================================
# 2.2 KNN: Different K values with ROC
# =============================================================================

print("\nKNN WITH DIFFERENT K VALUES:")

plt.figure(figsize=(10, 8))
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

for k in range(2, 9):
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Cross-validation scores
    scores = cross_val_score(knn, X_scaled, y, cv=cv)
    print(f"  k={k}: Accuracy = {scores.mean():.4f} (+/- {scores.std():.4f})")
    
    # ROC curve (using full fit for visualization)
    knn.fit(X_train, y_train)
    y_prob = knn.predict_proba(scaler.transform(X_test))[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.plot(fpr, tpr, label=f'k={k} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves for Different K Values')
plt.legend()
plt.show()
```

## Answer

| Task | Method | Key Metric |
| --- | --- | --- |
| 1.1 | Decision Tree | Accuracy varies with max_depth |
| 1.2 | Random Forest | Higher accuracy, feature importance |
| 2.1 | KNN Scaling | Scaled > Unscaled performance |
| 2.2 | KNN K-values | Optimal K typically 3-7 |