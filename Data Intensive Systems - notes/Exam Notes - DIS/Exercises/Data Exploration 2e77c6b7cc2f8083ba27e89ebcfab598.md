# Data Exploration

# IRIS Dataset: Descriptive Analytics & Visualization

## Exercise 2: Descriptive Analytics

> Download IRIS and conduct descriptive analytics. Report the descriptive statistic metrics for the whole dataset. Report the descriptive statistic metrics for each class.
> 

### Pseudocode

```python
FUNCTION descriptive_analytics(dataset):
    // Whole dataset statistics
    FOR each numerical column:
        COMPUTE count, mean, std, min, max, quartiles
    
    // Per-class statistics
    FOR each class in dataset:
        subset = FILTER dataset WHERE species == class
        FOR each numerical column in subset:
            COMPUTE count, mean, std, min, max, quartiles
    
    RETURN statistics
```

### Python Implementation

```python
import pandas as pd
from sklearn.datasets import load_iris

# =============================================================================
# Load Dataset
# =============================================================================

def load_iris_df():
    """Load IRIS as DataFrame with species names"""
    iris = load_iris()
    df = pd.DataFrame(
        data=iris.data,
        columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    )
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df

# =============================================================================
# Descriptive Statistics
# =============================================================================

df = load_iris_df()

# Whole dataset statistics
print("=" * 60)
print("DESCRIPTIVE STATISTICS - WHOLE DATASET")
print("=" * 60)
print(df.describe())

# Additional metrics
print("\nAdditional Metrics:")
print(f"Variance:\n{df.var(numeric_only=True)}")
print(f"\nSkewness:\n{df.skew(numeric_only=True)}")

# Per-class statistics
print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS - PER CLASS")
print("=" * 60)

for species in df['species'].unique():
    print(f"\n--- {species.upper()} ---")
    subset = df[df['species'] == species]
    print(subset.describe())
```

### Expected Output
```
============================================================
DESCRIPTIVE STATISTICS - WHOLE DATASET
============================================================
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

--- SETOSA ---
       sepal_length  sepal_width  petal_length  petal_width
count     50.000000    50.000000     50.000000    50.000000
mean       5.006000     3.428000      1.462000     0.246000
std        0.352490     0.379064      0.173664     0.105386
...
```

---
```

---

## Exercise 2: Visualization

> *Download IRIS and conduct visualization. Try to reproduce different types of visualization in this lecture.*
> 

### Pseudocode

```python
FUNCTION visualize_iris(dataset):
    // 1. Histogram - distribution of single variable
    FOR each feature:
        PLOT histogram(feature)
    
    // 2. Box Plot - distribution + outliers
    FOR each feature:
        PLOT boxplot(feature) grouped by species
    
    // 3. Scatter Plot - relationship between 2 variables
    PLOT scatter(feature1, feature2) colored by species
    
    // 4. Pair Plot - all pairwise relationships
    PLOT pairplot(all features) colored by species
    
    // 5. Heatmap - correlation matrix
    COMPUTE correlation matrix
    PLOT heatmap(correlation)
```

### Python Implementation

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load data
def load_iris_df():
    iris = load_iris()
    df = pd.DataFrame(
        data=iris.data,
        columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    )
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df

df = load_iris_df()

# =============================================================================
# 1. Histogram - Distribution of Features
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for ax, feature in zip(axes.flatten(), features):
    df[feature].hist(ax=ax, bins=20, edgecolor='black')
    ax.set_title(f'Histogram: {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# =============================================================================
# 2. Box Plot - Distribution by Class
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, feature in zip(axes.flatten(), features):
    df.boxplot(column=feature, by='species', ax=ax)
    ax.set_title(f'Box Plot: {feature}')

plt.tight_layout()
plt.show()

# =============================================================================
# 3. Scatter Plot - Two Variables
# =============================================================================

plt.figure(figsize=(8, 6))
colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(
        subset['sepal_length'], 
        subset['petal_length'],
        c=colors[species],
        label=species,
        alpha=0.7
    )

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.legend()
plt.show()

# =============================================================================
# 4. Pair Plot - All Pairwise Relationships
# =============================================================================

sns.pairplot(df, hue='species', diag_kind='hist')
plt.suptitle('Pair Plot of IRIS Features', y=1.02)
plt.show()

# =============================================================================
# 5. Heatmap - Correlation Matrix
# =============================================================================

plt.figure(figsize=(8, 6))
correlation = df.drop('species', axis=1).corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# =============================================================================
# 6. Violin Plot - Distribution Shape by Class
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, feature in zip(axes.flatten(), features):
    sns.violinplot(data=df, x='species', y=feature, ax=ax)
    ax.set_title(f'Violin Plot: {feature}')

plt.tight_layout()
plt.show()
```
```

### Visualization Sumamary

| **Plot Type** | **Purpose** | **Best For** |
| --- | --- | --- |
| **Histogram** | Distribution of single variable | Understanding data spread |
| **Box Plot** | Distribution + outliers | Comparing groups |
| **Scatter Plot** | Relationship between 2 variables | Finding correlations |
| **Pair Plot** | All pairwise relationships | Exploratory analysis |
| **Heatmap** | Correlation matrix | Feature relationships |
| **Violin Plot** | Distribution shape | Comparing distributions |