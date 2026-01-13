# Foundation of Data Mining

# IRIS Dataset Normalization Exercise

> Download IRIS dataset, install Python Environment, write code to read IRIS dataset, implement normalization methods and apply them to IRIS.
> 

## Dataset Overview

The IRIS dataset contains 150 samples of iris flowers with 4 features:

| Feature | Description | Range |
| --- | --- | --- |
| Sepal Length | Length of sepal (cm) | 4.3 - 7.9 |
| Sepal Width | Width of sepal (cm) | 2.0 - 4.4 |
| Petal Length | Length of petal (cm) | 1.0 - 6.9 |
| Petal Width | Width of petal (cm) | 0.1 - 2.5 |

**Sample Data:**

```python
sepal_length  sepal_width  petal_length  petal_width  species
5.1           3.5          1.4           0.2          setosa
7.0           3.2          4.7           1.4          versicolor
6.3           3.3          6.0           2.5          virginica
```

---

## Normalization Methods

| Method | Formula | Range |
| --- | --- | --- |
| Min-Max | (x - min) / (max - min) | [0, 1] |
| Z-Score | (x - mean) / std | ~[-3, 3] |
| Decimal Scaling | x / 10^d (d = max digits) | varies |

## Pseudecode

**Load Dataset**

```python
FUNCTION load_iris():
    dataset = LOAD from sklearn or CSV file
    features = dataset[numerical columns]
    labels = dataset[species column]
    RETURN features, labels
```

**Min-Max Normalization**

```python
FUNCTION min_max_normalize(data):
    FOR each column in data:
        min_val = MIN(column)
        max_val = MAX(column)
        normalized_column = (column - min_val) / (max_val - min_val)
    RETURN normalized_data
```

**Z-Score Normalization**

```python
FUNCTION z_score_normalize(data):
    FOR each column in data:
        mean_val = MEAN(column)
        std_val = STD(column)
        normalized_column = (column - mean_val) / std_val
    RETURN normalized_data
```

**Decimal Scaling**

```python
FUNCTION decimal_scaling(data):
    FOR each column in data:
        max_abs = MAX(ABS(column))
        d = CEIL(LOG10(max_abs))
        normalized_column = column / (10 ^ d)
    RETURN normalized_data
```

---

## Python Implementation

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# =============================================================================
# Load Dataset
# =============================================================================

def load_iris_data():
    """
    Pseudocode:
        dataset = LOAD iris from sklearn
        RETURN features as DataFrame, labels
    """
    iris = load_iris()
    df = pd.DataFrame(
        data=iris.data,
        columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    )
    df['species'] = iris.target
    return df

# =============================================================================
# Normalization Methods
# =============================================================================

def min_max_normalize(data):
    """
    Pseudocode:
        FOR each column:
            normalized = (value - min) / (max - min)
        RETURN normalized_data
    """
    return (data - data.min()) / (data.max() - data.min())

def z_score_normalize(data):
    """
    Pseudocode:
        FOR each column:
            normalized = (value - mean) / std
        RETURN normalized_data
    """
    return (data - data.mean()) / data.std()

def decimal_scaling(data):
    """
    Pseudocode:
        FOR each column:
            d = number of digits in max absolute value
            normalized = value / 10^d
        RETURN normalized_data
    """
    max_abs = data.abs().max()
    d = np.ceil(np.log10(max_abs))
    return data / (10 ** d)

# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    # Load data
    df = load_iris_data()
    features = df.drop('species', axis=1)
    
    print("Original Data (first 5 rows):")
    print(features.head())
    
    # Apply normalizations
    print("\n" + "=" * 50)
    print("Min-Max Normalized:")
    print(min_max_normalize(features).head())
    
    print("\n" + "=" * 50)
    print("Z-Score Normalized:")
    print(z_score_normalize(features).head())
    
    print("\n" + "=" * 50)
    print("Decimal Scaling:")
    print(decimal_scaling(features).head())
```

---

## Expected Output
```
Original Data (first 5 rows):
   sepal_length  sepal_width  petal_length  petal_width
0          5.1          3.5           1.4          0.2
1          4.9          3.0           1.4          0.2
2          4.7          3.2           1.3          0.2
3          4.6          3.1           1.5          0.2
4          5.0          3.6           1.4          0.2

==================================================
Min-Max Normalized:
   sepal_length  sepal_width  petal_length  petal_width
0      0.222222     0.625000      0.067797     0.041667
1      0.166667     0.416667      0.067797     0.041667
2      0.111111     0.500000      0.050847     0.041667
3      0.083333     0.458333      0.084746     0.041667
4      0.194444     0.666667      0.067797     0.041667

==================================================
Z-Score Normalized:
   sepal_length  sepal_width  petal_length  petal_width
0     -0.900681     1.019004     -1.340227    -1.315444
1     -1.143017    -0.131979     -1.340227    -1.315444
2     -1.385353     0.328414     -1.397064    -1.315444
3     -1.506521     0.098217     -1.283389    -1.315444
4     -1.021849     1.249201     -1.340227    -1.315444

==================================================
Decimal Scaling:
   sepal_length  sepal_width  petal_length  petal_width
0          0.51         0.35          0.14         0.02
1          0.49         0.30          0.14         0.02
2          0.47         0.32          0.13         0.02
3          0.46         0.31          0.15         0.02
4          0.50         0.36          0.14         0.02
```