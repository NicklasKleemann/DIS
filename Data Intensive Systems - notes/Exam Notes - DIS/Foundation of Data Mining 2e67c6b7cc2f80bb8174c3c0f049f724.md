# Foundation of Data Mining

# **Definitions**

| **Term** | **Definition** |
| --- | --- |
| **Data Mining** | The process of turning a large collection of data into knowledge by discovering patterns, correlations, and insights |
| **First-Order Logic** | A formal logical system that represents facts as true/false; limited because it cannot handle uncertainty or learn from data |
| **Supervised Learning** | Learning paradigm using labeled data to predict outcomes (classification, regression) |
| **Unsupervised Learning** | Learning paradigm using unlabeled data to discover patterns (clustering, association) |
| **Reinforcement Learning** | Learning paradigm where an agent learns through interaction with an environment using rewards/penalties |
| **Classification** | Predicting which predefined class a data point belongs to |
| **Regression** | Predicting a continuous numeric value |
| **Clustering** | Identifying natural groups in data without predefined labels |
| **Association Analysis** | Finding relationships between items in transaction data (e.g., market basket analysis) |
| **Anomaly Detection** | Identifying outliers or unusual data points |
| **Time Series Forecasting** | Predicting future values based on historical time-ordered data |
| **Recommendation Engine** | System that predicts user preferences for items |
| **Data Preprocessing** | Preparing raw data for mining; the most time-consuming step (60-80% of project time) |
| **Data Cleaning** | Removing noise and inconsistent data |
| **Data Integration** | Merging data from multiple sources |
| **Data Reduction** | Obtaining a smaller representation while maintaining data integrity |
| **Data Transformation** | Converting data into forms appropriate for mining |
| **Missing Values** | Empty values due to recording errors; handled by ignoring, filling manually, constants, mean, or prediction |
| **Noisy Data** | Random errors or variance in measured variables; smoothed by binning |
| **Binning** | Smoothing technique that groups values into bins to reduce noise or discretize continuous data |
| **Entity Identification Problem** | Challenge of matching attributes across databases (e.g., `customer_id` vs `cust_number`) |
| **Redundancy** | When an attribute can be derived from other attributes |
| **Dimensionality Reduction** | Reducing the number of attributes (e.g., PCA, wavelet transforms) |
| **Numerosity Reduction** | Reducing the number of data points (e.g., sampling, histograms) |
| **Lossless Compression** | Data compression where original data can be exactly reconstructed |
| **Lossy Compression** | Data compression where only an approximation can be reconstructed |
| **Normalization** | Scaling attribute values to a standard range |
| **Min-Max Normalization** | Scales values to a specified range using: $v'_i=\frac{v_i-min_A}{max_A-min_A}(new\_max_A-new\_min_A)+new\_min_A$ |
| **Z-Score Normalization** | Standardizes values using mean and standard deviation: $v'=\frac{v−μ}{σ}$ |
| **Decimal Scaling** | Normalizes by moving decimal point: $v'=\frac{v}{10^j}$ |
| **Discretization** | Converting continuous attributes to discrete/categorical values |
| **Support** | Frequency of an itemset in a dataset: $\frac{\text{transactions with itemset}}{\text{total transactions}}$ |
| **Confidence** | Reliability of an association rule: $\frac{\text{Support}(A\cup B)}{\text{Support}(A)}$ |
| **Lift** | Significance of an association rule beyond random chance |
| **K-Means** | Clustering algorithm that partitions data into k clusters based on centroids |
| **DBSCAN** | Density-based clustering algorithm that can find non-convex clusters |
| **Apriori** | Association rule mining algorithm using downward-closure property to prune candidates |
| **FP-Growth** | Association rule mining algorithm using frequent-pattern tree to avoid candidate generation |
| **KNN (K-Nearest Neighbors)** | Classification algorithm that assigns class based on k closest training examples |
| **Decision Tree** | Classification/discretization algorithm that splits data based on information gain or Gini index |
| **ARIMA** | Time series forecasting model (AutoRegressive Integrated Moving Average) |
| **Collaborative Filtering** | Recommendation approach based on similar users' preferences |
| **Content-Based Filtering** | Recommendation approach based on item features similar to user's past preferences |

[Introduction to Data Mining](Foundation%20of%20Data%20Mining/Introduction%20to%20Data%20Mining%202e67c6b7cc2f8006a75cd91dc13966b9.md)

[Data Mining Process](Foundation%20of%20Data%20Mining/Data%20Mining%20Process%202e67c6b7cc2f8046a062fead83a5acd9.md)

[Different Types of Data Mining](Foundation%20of%20Data%20Mining/Different%20Types%20of%20Data%20Mining%202e67c6b7cc2f80269901d3a28888e761.md)

[Technologies Used in Data Mining](Foundation%20of%20Data%20Mining/Technologies%20Used%20in%20Data%20Mining%202e67c6b7cc2f800bbd41eceaab098f9a.md)

[Data Preprocessing](Foundation%20of%20Data%20Mining/Data%20Preprocessing%202e67c6b7cc2f80628e7fed1a7f28f220.md)