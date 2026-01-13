# Object of Data Exploration

The slides define the **object of data exploration** as supporting the entire data science workflow — from understanding raw data to interpreting the results of data mining.

It has **four main objectives**:

- Data understanding
- Data preparation
- Data mining tasks
- Interpreting the results

---

## Data Understanding

Data exploration provides a **high-level overview of each attribute (variable)** in the dataset and how attributes interact.

It answers questions such as:

- What is the **typical value** of an attribute?
- How much do data points **differ from the typical value**?
- Are there **extreme values (outliers)**?

By computing descriptive statistics and using visualization, data exploration reveals:

- The distribution of values
- Variability
- Relationships between attributes

This is essential before applying any statistical or machine-learning models.

---

## Data Preparation

Before running data mining algorithms, the dataset must be cleaned and prepared.

The slides emphasize that data exploration is used to detect:

- **Outliers**
- **Missing values**
- **Highly correlated attributes**

Highly correlated attributes are especially important because:

> Some data mining algorithms do not work well when input attributes are correlated.
> 

Therefore, correlated attributes must be **identified and removed or handled** before further analysis.

---

## Data Mining Tasks

Data exploration can sometimes **replace complex data mining**.

The slides give examples:

- **Scatterplots** can reveal **clusters** in low-dimensional data
- Visual patterns can help build **regression** or **classification** models using simple rules

This means that:

- Instead of always using advanced algorithms, visual and statistical exploration can already give strong insights.

---

## Interpreting the Results

After data mining has been performed, data exploration is used again to **understand the output**.

It helps analyze:

- Predictions
- Classifications
- Clusters

For example:

- **Histograms** help understand the distribution of predicted values
- They are also useful for **error rate estimation** in prediction models

Thus, data exploration is used both **before and after** data mining.

---

## Summary

Data exploration is not just a preparation step — it is involved in:

- Understanding data
- Cleaning and preparing it
- Supporting data mining
- Interpreting results

It acts as the **foundation and validation tool** for the entire data science process.