# Descriptive Statistics

- Dataset Characteristics
    - Center (Mean, Median, Mode)
    - Spread (Range, Variance, Standard Deviation)
    - Shape (Symmetry, Skewness, Kurtosis)
- Univariate Descriptive Statistics
- Multivariate Descriptive Statistics
- Correlation (Pearson Correlation Coefficient)

# Descriptive Statistics

Descriptive statistics is the study of the **aggregate quantities of a dataset**.

It summarizes large amounts of data into **simple numerical measures** that describe how the data behaves.

Examples from the slides include:

- Average annual income
- Median home price
- Range of credit scores

---

## Dataset Characteristics

The slides describe three main ways to characterize a dataset:

### 1. Center of the Dataset

These describe the **typical value**.

- **Mean**
    
    The arithmetic average of all observations.
    
- **Median**
    
    The value at the center of the distribution.
    
- **Mode**
    
    The most frequently occurring value.
    

These measures help identify what a “normal” data point looks like.

---

### 2. Spread of the Dataset

These describe **how much the values vary**.

- **Range**
    
    Maximum value − minimum value.
    
- **Variance**
    
    Measures how far values deviate from the mean.
    
- **Standard Deviation**
    
    The square root of variance, showing typical distance from the mean.
    

The slides define **deviation** as:

$x_i - \mu$

where xix_ixi is a value and μ\muμ is the mean.

---

### 3. Shape of the Distribution

These describe how the data is distributed.

- **Symmetry** – whether the distribution is balanced
- **Skewness** – whether it leans left or right
- **Kurtosis** – how heavy or light the tails are

These help understand whether the data is normally distributed or not.

---

## Univariate Descriptive Statistics

Univariate analysis studies **one attribute at a time**.

It is used to understand:

- The distribution of a single attribute
- Its central value
- Its variation

The slides give Iris dataset examples where statistics such as mean, median, mode, range, variance, and standard deviation are computed for:

- Sepal length
- Sepal width
- Petal length
- Petal width

Univariate statistics do **not** show relationships between attributes.

---

## Multivariate Descriptive Statistics

Multivariate analysis studies **multiple attributes simultaneously**.

It is used to understand:

- How attributes interact
- How data points relate to each other in multi-dimensional space

Each Iris flower is a point in **four-dimensional space**:

$\{sepal\ length,\ sepal\ width,\ petal\ length,\ petal\ width\}$

The dataset has a **central mean point** in this 4-D space, calculated from the means of each attribute.

This helps measure how far each data point is from the center of the dataset.

---

## Correlation (Pearson Correlation Coefficient)

Correlation measures the **statistical relationship between two attributes**.

It tells:

- Whether two attributes change together
- Whether one increases when the other increases or decreases

The slides use the **Pearson correlation coefficient** rrr, where:

$-1 \le r \le 1$

- $r = 1$ → perfect positive correlation
- $r=−1$ → perfect negative correlation
- r = 0 → no linear relationship

High correlation means attributes are strongly related.

---

## Summary

Descriptive statistics:

- Quantifies datasets
- Describes typical values
- Measures variability
- Shows how attributes relate

It provides the **numerical foundation** for data exploration and supports visualization and data mining.