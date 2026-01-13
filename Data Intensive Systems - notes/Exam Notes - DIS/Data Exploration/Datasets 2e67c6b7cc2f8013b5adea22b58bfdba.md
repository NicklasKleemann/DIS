# Datasets

- Iris Dataset
- Attributes and Labels
- Continuous Numeric Data
- Categorical (Nominal) Data
- Ordered Nominal Data

## Iris Dataset

The **Iris dataset** is one of the most widely used datasets in data science.

It was introduced by **Ronald Fisher** in his work on **discriminant analysis**.

The dataset contains:

- **150 observations**
- **Three species** of iris flowers:
    - setosa
    - versicolor
    - virginica
- **50 observations per species**

Each observation represents one flower and contains:

- **Sepal length**
- **Sepal width**
- **Petal length**
- **Petal width**
- **Species label**

The first four are **attributes**, and the fifth is the **label**.

---

## Attributes and Labels

An **attribute** (also called a feature or variable) describes a property of a data point.

In the Iris dataset:

- Sepal length
- Sepal width
- Petal length
- Petal width

are all attributes.

The **label** is the target variable:

- It identifies which species the flower belongs to.

The slides note that:

- Setosa can be easily separated from the other two species using simple rules (for example, petal length < 2.5 cm)
- Separating versicolor and virginica requires more complex combinations of attributes

---

## Continuous Numeric Data

All four Iris attributes are **numeric continuous values** measured in centimeters.

Continuous numeric data:

- Can take any real value within a range
- Supports mathematical operations such as:
    - Addition
    - Subtraction
    - Mean
    - Variance

Examples from the slides:

- Petal length = 1.4 cm
- Sepal width = 3.5 cm

These values allow precise measurement and statistical analysis.

---

## Categorical (Nominal) Data

Categorical (also called **nominal**) data represents:

- Names
- Symbols
- Categories

Examples from the slides:

- Eye color: black, green, blue, gray
- Iris species: setosa, versicolor, virginica

For categorical data:

- There is **no mathematical relationship** between values
- Only logical comparisons such as **equal / not equal** are meaningful

You cannot compute averages or distances between categories.

---

## Ordered Nominal Data

An **ordered nominal** (ordinal) data type is a special kind of categorical data where:

- There is a **natural order** among the values

Example from the slides:

- Temperature expressed as:
    - cold
    - mild
    - hot

These values have an order, but:

- The **distance between them is not numeric**
- You cannot say how much hotter “hot” is compared to “mild”

---

## Summary

Datasets consist of:

- **Attributes** (features)
- **Labels** (targets)

Understanding the **type of each attribute** (numeric, categorical, ordered) is crucial because:

- It determines what operations can be applied
- It affects which statistical and visualization techniques can be used

The Iris dataset is a standard example used to demonstrate these concepts.