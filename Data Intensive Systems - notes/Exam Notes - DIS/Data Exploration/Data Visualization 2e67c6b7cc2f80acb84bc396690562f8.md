# Data Visualization

- Why Visualization is Needed
- Univariate Visualization
    - Histogram
    - Box Plot
    - Distribution Chart
- Multivariate Visualization
    - Scatterplot
    - Scatter Matrix
    - Bubble Chart
    - Density Chart
- Visualizing High-Dimensional Data
    - Parallel Coordinates
    - Deviation Charts
    - Andrews Curves

## Key Terms

| Term | Definition |
| --- | --- |
| Data Visualization | The process of representing data visually in charts, plots, or graphics to understand patterns and relationships. |
| Univariate Visualization | Visualization of one attribute at a time. |
| Multivariate Visualization | Visualization of two or more attributes at the same time. |
| Histogram | A bar chart showing the distribution of numeric data by grouping values into bins. |
| Box Plot | A visualization that shows median, quartiles, and outliers of a numeric attribute. |
| Scatterplot | A plot showing the relationship between two numeric attributes. |
| Scatter Matrix | A grid of scatterplots comparing all pairs of attributes. |
| Bubble Chart | A scatterplot where point size represents an additional attribute. |
| Density Chart | A scatterplot that includes density information using background color. |
| Parallel Coordinates | A chart where each attribute is a vertical axis and each data point is a line across them. |
| Andrews Curves | A technique that transforms each data point into a curve to visualize high-dimensional data. |

---

## Why Visualization is Needed

The slides state that **data visualization is one of the most important techniques for data discovery and exploration**.

Visual representation helps with:

- **Understanding dense information**
- **Identifying relationships between attributes**
- **Understanding patterns and structure** in complex datasets

Humans can recognize patterns and trends more easily in images than in tables of numbers.

---

## Univariate Visualization

Univariate visualization looks at **one attribute at a time**.

### Histogram

A histogram groups numeric values into bins and shows how many data points fall into each bin.

From the slides:

- Histograms were used to show distributions of petal length and sepal width.
    
    They help identify:
    
- Typical values
- Spread
- Skewness
- Outliers

---

### Box Plot

A box plot shows:

- Median
- Quartiles
- Range
- Outliers

Box plots allow fast comparison of distributions across attributes.

---

### Distribution Chart

Distribution charts show how values are spread over a range.

They help detect:

- Clusters
- Skewed distributions
- Extreme values

---

## Multivariate Visualization

Multivariate visualization shows **relationships between attributes**.

### Scatterplot

A scatterplot places two attributes on x and y axes.

It reveals:

- Correlation
- Clusters
- Trends

The slides use scatterplots to compare:

- Sepal length vs sepal width
- Petal length vs petal width

---

### Scatter Matrix

A scatter matrix is a grid of scatterplots for **all pairs of attributes**.

It allows:

- Visual comparison of all attribute relationships at once

---

### Bubble Chart

A bubble chart adds a **third dimension** by using:

- Bubble size to represent another attribute

This allows three attributes to be analyzed at the same time.

---

### Density Chart

A density chart adds:

- A background color to show how dense data points are

This helps identify areas with many overlapping points.

---

## Visualizing High-Dimensional Data

When data has many attributes, special methods are needed.

### Parallel Coordinates

Each attribute is shown as a vertical axis.

Each data point becomes a line crossing all axes.

This makes it possible to:

- Compare many attributes simultaneously

---

### Deviation Charts

Similar to parallel coordinates.

They show how each data point deviates from a reference.

---

### Andrews Curves

Each data point is transformed into a **curve**.

This technique:

- Projects high-dimensional data into a 2D plot
- Helps detect **outliers** and structure

The slides note that Andrews curves are useful for **time-series and high-dimensional data**.

---

## Summary

Data visualization:

- Converts numbers into images
- Makes patterns, relationships, and anomalies visible
- Supports both univariate and multivariate analysis
- Enables exploration of high-dimensional data

It is a core tool for understanding datasets before and after data mining.