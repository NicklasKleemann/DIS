# Accumulated In-Course Exercises

## 1. Foundation of Data Systems

We have a raw ID-Hashtag file, where each line is composed of a tweet ID and a number of hashtags, e.g., `1020253525161283584 #Hartberg #Finance #Job #Jobs #Hiring`. Find the right data models and tools/libraries to implement the following functionalities.

1. We may want to know the frequency of an arbitrary hashtag. How do you implement this if our requests are sparse? Will you implement in the same way if our requests are frequent?
2. How do you implement if we want to return the top-10 frequent hashtags?
3. If new lines are appended to the original raw file continuously, what would you change for your implementations in 1 and 2?

When you decide your design and implementation, think about the different paradigms such as relational databases, key-value stores, document databases and graph databases, and choose the most suitable one(s) to use.

## 2. Parallel Databases

1. We want to count *each* hashtag that appears in the ID-Hashtag file (in Moodle). If you have a shared-nothing cluster with m processors, how can that help to speed up the counting? Describe your data partitioning strategy and counting algorithm.

2. If we only want to know the frequency of a given specific hashtag, how can you make use of the shared-nothing architecture? Describe your data partitioning strategy and counting algorithm.

For each exercises:

* Suppose one of the m processors is designated as the ‘master’ node
    - It has the original data file, and it needs to store the final result.
    - It can ‘tell’ all other nodes what to do in some form of message.
* You’re encouraged to also write codes (in Python or another language) to simulate the parallelism of your algorithmic solutions.

## 3. Distributed Systems

### Exercise 1

Consider the following setting and statistics

* r<sub>1</sub> with schema R(A, B) at site S<sub>1</sub>
  $$ \text{card}(R) = 10,000 $$
* r<sub>2</sub> with schema S(A, C) at site S<sub>2</sub>
  $$ \text{card}(S) = 50,000 $$
* $$ \text{card}(\Pi_A(r_1)) = 1,000 $$
  $$ \text{card}(\Pi_B(r_1)) = 2,000 $$
* $$ \text{card}(\Pi_A(r_2)) = 3,000 $$
  $$ \text{card}(\Pi_C(r_2)) = 5,000 $$
* $$ \text{card}(r_1 \ltimes r_2) = 1,500 $$
* $$ \text{card}(r_2 \ltimes r_1) = 3,500 $$

* Attribute data value size:
    * A: 10 bytes; B: 20 bytes; C: 30 bytes.
* Basic costs:
    * c<sub>0</sub>: initial set-up cost between any two sites = 20
    * c<sub>1</sub>: transmission cost per data unit between any two sites = 1 per 500 bytes
* **Questions**: If we use the semijoin strategy to obtain $$ r_1 \bowtie r_2 $$,
    * What is the total cost to obtain the result at S<sub>1</sub>?
    * What is the total cost to obtain the result at S<sub>2</sub>?

### Exercise 2

Site 1: **EMPLOYEE**
* Schema: (EID, Name, Salary, DID)
    - EID: 10 bytes
    - Name: 20 bytes
    - Salary: 20 bytes
    - DID: 10 bytes
    - Totally 1000 tuples

Site 2: **DEPARTMENT**
* Schema: (DID, DName)
    - DID: 10 types
    - Dname: 20 types
    - Totally 50 tuples

* **Question**: Site 3 needs to find the name of employees and their department names. Figure out at least 3 strategies for this distributed join query and calculate the total amount of data transfer for each strategy.

## 5. Foundation of Data Mining

* Download IRIS dataset
    - https://www.kaggle.com/datasets/uciml/iris
    - OR https://scikit-learn.org/1.5/auto_examples/datasets/plot_iris_dataset.html
* Install Python Environment (Conda, WinPython)
* Write code to read IRIS dataset
* Implementing normalization methods and apply them to IRIS

### Mini-quizzes (Lecture 5)

**Mini-quiz 1**
* Suppose that the minimum and maximum values for the attribute income are $12,000 and $98,000, respectively. We would like to map income to the range [0.0,1.0]. By min-max normalization, what is the value of $73,600?

**Mini-quiz 2**
* Suppose that the mean and standard deviation of the values for the attribute income are $54,000 and $16,000, respectively. With z-score normalization, what is the value of $73,600?

## 6. Data Exploration (Descriptive Data Analytics)
    
### Exercises 1

* Download IRIS and conduct descriptive analytics
    - Report the descriptive statistic metrics for the whole datasets
    - Report the descriptive statistic metrics for each class

### Exercises 2

* Download IRIS and conduct visualization
    - Try to reproduce different types of visualization in this lecture

## 7. Classification

### Exercises (1)

1. Given two classes: $A = \{(1, 3), (2, 2), (3.5, 1), (5, 4), (1.5, 4), (4, 2)\}$ and $B = \{(2, 3), (3, 0.5), (4, 3), (3.5, 2), (1, 2.5), (2, 1)\}$ and three unclassified points $(4, 1), (1.5, 2.5)$ and $(3, 4)$.
    1. Use the kNN classification approach and Euclidean distance to decide the classes for the three points, for $k = 1, 2, 3$.
    2. Repeat 1.1 but use Manhattan distance instead. The Manhattan distance between $(x_1, y_1)$ and $(x_2, y_2)$ is defined as $|x_1 - x_2| + |y_1 - y_2|$.
    3. Compare the results of 1.1 and 1.2.

2. Suppose that labelled data is distributed in $M$ sites and we need to run kNN to decide the class label for a new point at site $S_0$.
    1. Describe a parallel algorithm for it. How much data do you need to transfer?
    2. Can it make a difference whether you run local kNN at $S_0$ or not?

### Exercises (2, hands-on, optional)

Using the Diabetes dataset (available in Moodle), do the following
1. Split the dataset D into two parts: 80% for training (D<sub>T</sub>) and 20% for validation/test D<sub>v</sub>.
   > NB: You may use different ratios, do the subsequent steps, and see the effect
   1. Build a decision tree for predicting if a person has diabetes or not. Use D<sub>T</sub> to train the model, apply the model to D<sub>v</sub>, and evaluate the classification accuracy.
      > Try to build a number of different trees using different parameters, see their accuracy
   2. Build a random forest on the same training/test datasets, obtain its accuracy, and plot the important features for it.
2. Apply KNN and cross validation
   1. Use a default KNN (K=5) to see the effect of data scaling (with vs. without).
   2. Try different K’s (2 to 8) for KNN, validate each classifier using stratified 3-fold, and plot the ROC with AUC for each model.

## 8. Clustering

### In-slide Exercises

* Work out the clustering result using 2-means but starting with m<sub>1</sub>=10, m<sub>2</sub>=20
* Work out the clustering result using 3-means.
    - Start with 3 initial random means
    - Or with 3 initial random clusters

*(Using the same set of numbers: 2, 3, 4, 10, 11, 12, 20, 25, 30)*

### Exercises (1)
    
1. K-means example on page 16
2. Use Euclidean distance based DBSCAN to decide the clustering result for the following data set.
    * A1=(2,10), A2=(2,5), A3=(8,4), A4=(5,8), A5=(7,5), A6=(6,4), A7=(1,2), A8=(4,9).
    * MinPts is 2 and Eps is also 2.
* Draw the dendrogram using the *complete linkage* agglomerative clustering for the given distance matrix. Use the *smallest* distance as the merge criterion.

<table>
  <thead>
    <tr>
        <th></th>
        <th>A</th>
        <th>B</th>
        <th>C</th>
        <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>A</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>6</td>
    </tr>
<tr>
        <td>B</td>
<td></td>
<td>0</td>
<td>2</td>
<td>5</td>
    </tr>
<tr>
        <td>C</td>
<td></td>
<td></td>
<td>0</td>
<td>3</td>
    </tr>
<tr>
        <td>D</td>
<td></td>
<td></td>
<td></td>
<td>0</td>
    </tr>
  </tbody>
</table>

### Exercises (2, hands-on, optional)

Work with the bikes dataset (in Moodle) in Jupyter Notebook

1. Apply K-means clustering
   - Vary k, e.g., 2, 3, 4, 5 ...
   - Use the Elbow method to find the best k
   - Visualize the K-means clustering result of the best k
2. Apply agglomerative clustering
   - Show the procedure of how 10 clusters are merged until a single cluster is obtained
   - Draw the dendrogram with linkage=ward
   - Figure out the best number of clusters
   - Generate the corresponding clustering result, and visualize it
3. Apply DBSCAN clustering
   - Vary eps and min_samples
   - Visualize the DBSCAN clustering results with their Silhouette scores

## 9. Association Rules

### In-slide Exercises

Example: $l = \{2,3,5\}$, $min\_conf = 75\%$

* $\{2,3\} \Rightarrow \{5\}$ $2/2=100\% \surd$
* $\{2,5\} \Rightarrow \{3\}$ $2/3=66.6\% \text{ X}$
* $\{3,5\} \Rightarrow \{2\}$ $2/2=100\% \surd$

*do the rest as an exercise* (Find all nonempty subsets $s$ of $l$, and generate rule $s \Rightarrow l-s$)

* Exercises on real data
    * store_data.csv (in Moodle)
    * (7501, 20) - 7501 transactions, each having at most 20 items

### Exercises

1. Refer to the transaction table to the right. Say sup(ab)=100
    * Determine the possible values of sup(a)
        - Conclusion: sup(a) \_\_\_ 100
        - Hint: Is it possible that sup(a)=70? Why?
    * Determine the possible values of sup(abc)
        - Conclusion: sup(abc) \_\_\_ 100
        - Hint: Is it possible that sup(abc)=120? Why?
    
> Choose either "$\le$" or "$\ge$"

2. Slides 33 (Hands-on, optional)

Transaction table
(1000 rows)

<table>
  <thead>
    <tr>
        <th>TID</th>
        <th>Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>1</td>
<td>a,b,c</td>
    </tr>
<tr>
        <td>2</td>
<td>a,c</td>
    </tr>
<tr>
        <td>3</td>
<td>b,e,f</td>
    </tr>
<tr>
        <td>...</td>
<td>......</td>
    </tr>
  </tbody>
</table>
## 10. Data Warehouse

### Exercises

* JPT book Section 2.10
    * 2, 3, 4, 5, 7, 8, 9
* JPT book Section 3.5
    * 4, 5                