# Formulas

# Parallel Database Algorithms & Formulas

## 1. Data Partitioning Formulas

Partitioning determines how data is split across $n$ disks ($D_0, D_1, ..., D_{n-1}$).

### A. Round-Robin Partitioning

**Concept:** "Dealing cards." Tuples are distributed sequentially to ensure equal load balancing.

- **Formula:**
The $i$-th tuple is sent to disk:
$d = i \mod n$
    
    *(where* $i$ *is the row number and* $n$ *is the number of disks)*
    
- **Example:**
    - **System:** 3 Disks ($D_0, D_1, D_2$).
    - **Data:** 5 tuples ($t_1, t_2, t_3, t_4, t_5$).
    - **Distribution:**
        - $t_1 \rightarrow 1 \mod 3 \rightarrow$ **Disk 1** (or Disk 0 depending on 0-indexing)
        - $t_2 \rightarrow$ **Disk 2**
        - $t_3 \rightarrow$ **Disk 0**
        - $t_4 \rightarrow$ **Disk 1**
        - $t_5 \rightarrow$ **Disk 2**

### B. Hash Partitioning

**Concept:** Randomizing data based on a key to enable fast specific lookups.

- **Formula:**
For a tuple with attribute value $v$, the destination disk is:
$d = h(v) \mod n$
    
    *(where* $h$ *is a hash function returning an integer)*
    
- **Example:**
    - **System:** 3 Disks ($n=3$). Hash function is simply $h(x) = x$.
    - **Data IDs:** 8, 5, 20.
    - **Distribution:**
        - ID 8: $8 \mod 3 = 2 \rightarrow$ **Disk 2**
        - ID 5: $5 \mod 3 = 2 \rightarrow$ **Disk 2** (Skew/Collision!)
        - ID 20: $20 \mod 3 = 2 \rightarrow$ **Disk 2**
        - ID 9: $9 \mod 3 = 0 \rightarrow$ **Disk 0**

### C. Range Partitioning

**Concept:** Grouping "similar" values together. Good for range queries.

- **Formula/Logic:**
Define a partitioning vector $[v_0, v_1, ..., v_{n-2}]$.
    - If $v < v_0 \rightarrow$ Disk 0
    - If $v_i \le v < v_{i+1} \rightarrow$ Disk $i+1$
    - If $v \ge v_{n-2} \rightarrow$ Disk $n-1$
- **Example:**
    - **System:** 3 Disks.
    - **Vector:** $[5, 10]$ (This creates 3 ranges: $<5$, $5-10$, $>10$).
    - **Data IDs:** 2, 8, 20.
    - **Distribution:**
        - ID 2 ($2 < 5$) $\rightarrow$ **Disk 0**
        - ID 8 ($5 \le 8 < 10$) $\rightarrow$ **Disk 1**
        - ID 20 ($20 \ge 10$) $\rightarrow$ **Disk 2**

## 2. Parallel Join Algorithms

How to join relation $R$ and relation $S$ using $n$ processors ($P_0...P_{n-1}$).

### A. Partitioned Parallel Join (The Standard)

**Condition:** Only works for **Equi-Joins** (e.g., `R.id = S.id`).

- **Algorithm Steps:**
    1. **Partition:** Apply the **same** partitioning function (e.g., $h(x) \mod n$) to *both* tables on the join attribute.
    2. **Transport:** Move partitions so $P_i$ holds $R_i$ and $S_i$.
    3. **Local Join:** Each processor computes $R_i \bowtie S_i$.
- **Example:**
    - **Task:** Join `Student` and `Course` on `Semester`.
    - **Hash Function:** $Semester \mod 2$ (2 Processors).
    - **Data:**
        - Student Adam (Sem 1), Christian (Sem 3), Helle (Sem 4).
        - Course "Math" (Sem 1), "Algo" (Sem 3), "Data" (Sem 4).
    - **Execution:**
        - $P_0$ receives even semesters: Helle (Sem 4) + "Data" (Sem 4). -> **Join Found.**
        - $P_1$ receives odd semesters: Adam (Sem 1), Christian (Sem 3) + "Math" (Sem 1), "Algo" (Sem 3). -> **Joins Found.**

### B. Fragment-and-Replicate Join (Broadcast Join)

**Condition:** Use for **Non-Equi-Joins** OR when one table ($S$) is very small.

- **Algorithm Steps (Asymmetric):**
    1. **Fragment:** Keep the large table ($R$) partitioned as is (e.g., $R_0$ on $P_0$, $R_1$ on $P_1$).
    2. **Replicate:** Copy the **entire** small table ($S$) to **every** processor.
    3. **Local Join:** Each processor $P_i$ computes $R_i \bowtie S_{complete}$.
- **Example:**
    - **Task:** Find Apartments cheaper than a Person's budget. (Condition: `A.price < P.budget`). **This is not an equi-join.**
    - **Large Table:** `Person` (1 million rows).
    - **Small Table:** `Apartment` (100 rows).
    - **Execution:**
        - $P_0$ holds `Person` rows 1-500k. It receives a copy of ALL 100 `Apartment` rows. It checks joins locally.
        - $P_1$ holds `Person` rows 500k-1m. It receives a copy of ALL 100 `Apartment` rows. It checks joins locally.

## 3. Parallel Sort Algorithms

### A. Range-Partitioning Sort

**Key Concept:** "Divide by value first, sort later." No final merge step is needed.

- **Algorithm Steps:**
    1. **Range Partition:** Redistribute data globally so $P_0$ gets lowest keys, $P_1$ gets medium keys, $P_2$ gets highest keys.
    2. **Local Sort:** Each processor sorts its own chunk.
    3. **Result:** Just concatenate $P_0 + P_1 + P_2$.
- **Example:**
    - **Data:** `[100, 5, 20, 90]` on 2 Processors.
    - **Range Vector:** `[50]` (Split at 50).
    - **Redistribute:**
        - $P_0$ receives `[5, 20]` (Values < 50).
        - $P_1$ receives `[100, 90]` (Values >= 50).
    - **Local Sort:**
        - $P_0$ sorts to `[5, 20]`.
        - $P_1$ sorts to `[90, 100]`.
    - **Final:** `[5, 20]` + `[90, 100]` = Sorted.

### B. Parallel External Sort-Merge

**Key Concept:** "Sort locally first, merge later."

- **Algorithm Steps:**
    1. **Local Sort:** Every processor sorts whatever random data it currently has.
    2. **Redistribute:** $P_0$ asks for the "low range" from everyone else. $P_1$ asks for the "high range".
    3. **Merge:** $P_0$ merges the sorted streams it received.

## 4. Cost Estimation Logic (Query Types)

For the exam, you need to know how many disks are "touched" for different queries.

### A. Point Query (`SELECT * FROM T WHERE id = 8`)

| Partitioning Strategy | Disks Accessed | Why? |
| --- | --- | --- |
| **Round-Robin** | $n$ **(All)** | ID 8 could be anywhere. |
| **Hash** | **1 (Single)** | We calculate $h(8)$ and know exactly which disk has it. |
| **Range** | **1 (Single)** | We check the vector, see where 8 fits, and go to that disk. |

### B. Range Query (`SELECT * FROM T WHERE id > 5 AND id < 20`)

| Partitioning Strategy | Disks Accessed | Why? |
| --- | --- | --- |
| **Round-Robin** | $n$ **(All)** | Data is scattered randomly. |
| **Hash** | $n$ **(All)** | Hashing destroys order. ID 6 might be on Disk 0, ID 7 on Disk 2. |
| **Range** | **Few** | Only disks covering the range [5, 20] are accessed. |

### C. Formulas for "Skew"

If data is not balanced, one processor works harder. This is the **Bottleneck**.

- **Response Time Formula:**$Time = \max(T_{P0}, T_{P1}, ..., T_{Pn})$
    
    *The system is only as fast as its slowest processor.*
    
- **Example of Skew:**
    - Range Partitioning on `Age`.
    - Partition 1: Ages 0-20 (Very few people in database).
    - Partition 2: Ages 21-80 (Millions of people).
    - **Result:** Partition 2 is the bottleneck. Parallelism fails.

## 1. Distributed Data Storage

How data is split or copied across sites ($S_1, S_2, ...$).

### A. Fragmentation (Partitioning)

Splitting a relation $r$ into fragments $r_1, r_2, ..., r_n$.

- **Horizontal Fragmentation**
    - **Formula:** Select rows based on a condition (Selection $\sigma$).
    $r_i = \sigma_{condition}(r)$
    - **Example:** `Account` table split by branch.
        - $r_1 = \sigma_{branch="Hillside"}(Account)$
        - $r_2 = \sigma_{branch="Valleyview"}(Account)$
- **Vertical Fragmentation**
    - **Formula:** Select specific columns (Projection $\Pi$).
    - **Constraint:** You **must** include a common key (or tuple-id) in every fragment to reconstruct the table later.
    $r_i = \Pi_{key, attr_A, attr_B}(r)$

### B. Replication

Storing copies of the same data at multiple sites.

- **Full Replication:** The entire database is stored at every site.
- **Advantages:** High availability (if Site 1 fails, Site 2 works), faster local reads.
- **Disadvantages:** High update cost (writing to ID 5 requires updating *all* copies).

## 2. Distributed Query Processing (The Semijoin)

In distributed systems, **Network Transmission Cost** is the main bottleneck. The goal is to minimize data shipped.

### A. The Semijoin Strategy ($R_1 \ltimes R_2$)

**Concept:** Instead of shipping the huge table $R_1$ to join with $R_2$, we only ship the *join keys* to filter $R_2$ first.

**Formal Definition:**

$r_1 \ltimes r_2 = \Pi_{R_1}(r_1 \bowtie r_2)$

*(Selects only tuples of* $r_1$ *that actually contribute to the join with* $r_2$*)*

**The Algorithm (Step-by-Step Walkthrough):**
Assume Site 1 has $R_1$ and Site 2 has $R_2$. We want the result at Site 1.

1. **Project Keys:** Site 1 projects only the join column from $R_1$ into a temp file.
$Temp_1 = \Pi_{JoinAttr}(R_1)$
2. **Ship Keys:** Send $Temp_1$ from Site 1 $\rightarrow$ Site 2.
3. **Reduce Target:** Site 2 joins $Temp_1$ with $R_2$ to find matches.
$Temp_2 = R_2 \bowtie Temp_1$
    
    *(This* $Temp_2$ *is now the "Semijoin" - it only contains useful rows from* $R_2$*)*
    
4. **Ship Back:** Send $Temp_2$ from Site 2 $\rightarrow$ Site 1.
5. **Final Join:** Site 1 performs the final join locally.
$Result = R_1 \bowtie Temp_2$

## 3. Cost Estimation Formulas

You will likely be asked to calculate the cost of a Naïve Join vs. a Semijoin.

**Cost Formula:**

$Total Cost = \sum (c_0 + c_1 \times DataSize)$

- $c_0$: Initial setup cost (latency/handshake).
- $c_1$: Transmission cost per byte/unit.

### Example Calculation (from Slides)

- **Scenario:** Join $R_1$ (at Site 1) and $R_2$ (at Site 2). Result needed at Site 1.
- **Naïve Strategy:** Ship entire $R_2$ to Site 1.
$Cost = c_0 + c_1 \times size(R_2)$
- **Semijoin Strategy:**
    1. Cost to ship Keys ($Temp_1$) to Site 2.
    2. (+) Cost to ship Matches ($Temp_2$) back to Site 1.
    $Cost = (c_0 + c_1 \times size(Temp_1)) + (c_0 + c_1 \times size(Temp_2))$
- **Exam Tip:** Compare the Naïve cost vs. Semijoin cost. If $R_2$ is huge but only a few rows match, Semijoin is purely cheaper.

## 4. Distributed Transactions (2PC)

### Two-Phase Commit Protocol (2PC)

Ensures a transaction $T$ either commits everywhere or aborts everywhere.

### Phase 1: Obtaining a Decision (Voting)

1. **Coordinator** asks: "Prepare to commit $T$?" (Writes `<prepare T>` to log).
2. **Participants** check if they can commit locally.
    - If **Yes**: Write `<ready T>` to log, send "Ready".
    - If **No**: Write `<no T>` to log, send "Abort".

### Phase 2: Recording the Decision

1. **Coordinator** collects votes:
    - If **ALL** say "Ready" $\rightarrow$ Global Commit.
    - If **ANY** say "Abort" (or timeout) $\rightarrow$ Global Abort.
2. Coordinator writes decision (`<commit T>` or `<abort T>`) to log and tells participants.
3. Participants execute the decision.

### Failure Handling Rules

If a site recovers and checks its log:

- **Log contains `<commit T>`:** Must Redo.
- **Log contains `<abort T>`:** Must Undo.
- **Log contains `<ready T>` ONLY:**
    - This is the dangerous state. The site promised to be ready but crashed before hearing the result.
    - **Action:** It must contact the Coordinator (or other sites) to find out what happened. It cannot decide on its own.

# MapReduce

## 1. Functional Programming Roots (The Math)

MapReduce is based on Lisp-style functional programming. The lecture uses a **Vector Length** calculation to demonstrate this.

### Vector Magnitude Formula

To calculate the length of a vector $v(v_1, v_2, ..., v_n)$:

$|v| = \sqrt{\sum v_i^2}$

**MapReduce Logic:**

1. **Map (Transformation):** Apply $f(x) = x^2$ to every element $v_i$.
    - Input: $[v_1, v_2, v_3]$
    - Output: $[v_1^2, v_2^2, v_3^2]$
2. **Fold/Reduce (Aggregation):** Apply $g(x_1, x_2) = x_1 + x_2$ to sum them up.
    - Result: $\sum v_i^2$

## 2. The MapReduce Programming Model

You must know the input/output types for the two core functions.

### Function Signatures

- **Map Function:**
Takes a single key/value pair and produces a list of intermediate pairs.
$map: (k_1, v_1) \rightarrow list(k_2, v_2)$
- **Reduce Function:**
Takes an intermediate key and *all* values associated with that key.
$reduce: (k_2, list(v_2)) \rightarrow list(k_3, v_3)$
    
    *(Note: In Google's original paper, it returns just a list of values, but Hadoop typically emits key/value pairs).*
    

## 3. The Standard Algorithm: WordCount

This is the "Hello World" of MapReduce. You may be asked to write pseudocode for this or a similar counting task (like Hashtags).

### Algorithm Steps

1. **Map Phase:**
    - **Input:** `(DocID, DocContent)`
    - **Logic:** Loop through words in `DocContent`. For every word $w$, emit `(w, 1)`.
    - **Output:** `[(apple, 1), (banana, 1), (apple, 1)]`
2. **Shuffle & Sort (System Phase):**
    - The system groups values by key.
    - **Input to Reducer:** `(apple, [1, 1])`, `(banana, [1])`
3. **Reduce Phase:**
    - **Input:** `(Word, List of Counts)`
    - **Logic:** Sum the numbers in the list.
    - **Output:** `(Word, TotalSum)`

### Pseudocode (Python-style)

```
# Map Function
def map(key, value):
    # key: document name
    # value: document contents
    for word in value.split():
        emit(word, 1)

# Reduce Function
def reduce(key, values):
    # key: a word
    # values: a list of counts (e.g., [1, 1, 1, 1])
    result = 0
    for v in values:
        result += v
    emit(result)

```

## 4. Execution & Cost Formulas

### A. Shuffle Complexity

The "Shuffle and Sort" phase is the bottleneck (the barrier) between Map and Reduce.

- **Formula:** If a job has $m$ **mappers** and $r$ **reducers**:
$Total Copy Operations = m \times r$
    
    *(Every mapper potentially sends data to every reducer).*
    

### B. HDFS Replication Strategy

MapReduce relies on the Distributed File System (HDFS) for data safety.

- **Standard Algorithm:**
    - Default Replication Factor = **3**.
    - **Replica 1:** Local node (where the writer is).
    - **Replica 2:** Different node, *same* rack.
    - **Replica 3:** Different node, *different* rack.
    - *Why? Handles node failure AND rack switch failure.*

### C. Combiner Optimization ("Mini-Reducer")

- **Logic:** Run a local "reduce" on the mapper node before sending data over the network.
- **Effect:** Reduces network traffic.
- **Constraint:** The operation must be **commutative and associative** (like Sum or Max), but NOT operations like Average (mean).

# Data Mining

## 1. Data Cleaning Algorithms

When dealing with missing or noisy data, you need to apply specific mathematical substitutions.

### A. Missing Value Imputation

If a value $x$ is missing in a dataset of size $N$:

1. **Mean Substitution (Central Tendency):**
Replace missing $x$ with the average of all known values:
$x_{new} = \frac{1}{N} \sum_{i=1}^{N} x_i$
2. **Linear Regression/Interpolation:**
If attribute $x$ is correlated with $y$ and $z$, predict the missing value using the formula:
$x = \alpha \cdot y + \beta \cdot z + C$
    
    *(Where* $\alpha$ *and* $\beta$ *are learned weights).*
    

### B. Binning (Smoothing Noisy Data)

Used to handle noise by grouping values into "bins" and replacing them with a representative value (like the bin mean or boundary).

- **Logic:**
    1. Sort the data.
    2. Partition into equal-frequency or equal-width bins.
    3. Replace values in the bin with the **Bin Mean** or **Bin Boundaries**.

## 2. Data Transformation Formulas (Normalization)

Normalization scales numeric data into a specific range (e.g., [0, 1]) to prevent large numbers from dominating the model.

### A. Min-Max Normalization

Scales data to fit exactly within a new range $[new\_min, new\_max]$.

- **Formula:**$v' = \frac{v - min_A}{max_A - min_A}(new\_max_A - new\_min_A) + new\_min_A$
- **Variables:**
    - $v$: The original value.
    - $min_A, max_A$: The original minimum and maximum of the attribute.
    - $new\_min_A, new\_max_A$: The target range (usually 0 and 1).
- **Example (from slides):**
    - Range: [12,000, 98,000]. Target: [0.0, 1.0]. Value to normalize: 73,600.
    - Calculation:
    $\frac{73,600 - 12,000}{98,000 - 12,000}(1.0 - 0) + 0 = \mathbf{0.716}$

### B. Z-Score Normalization (Zero-Mean)

Scales data based on how many standard deviations it is from the mean. Useful when actual min/max are unknown or outliers exist.

- **Formula:**$v' = \frac{v - \bar{A}}{\sigma_A}$
- **Variables:**
    - $\bar{A}$ (or $\mu$): The mean (average) of the attribute.
    - $\sigma_A$: The standard deviation.
- **Example (from slides):**
    - Mean: 54,000. Std Dev: 16,000. Value: 73,600.
    - Calculation:
    $\frac{73,600 - 54,000}{16,000} = \mathbf{1.225}$

### C. Decimal Scaling

Moves the decimal point based on the maximum absolute value.

- **Formula:**$v' = \frac{v}{10^j}$
    
    *(Where* $j$ *is the smallest integer such that* $\max(|v'|) < 1$*).*
    

## 3. Discretization

### Binning Logic

Converting continuous data (e.g., exact salary) into categorical ranges (e.g., "Low", "Medium", "High").

- **Algorithm Steps:**
    1. **Equal-Width Partitioning:** Divides the range into $N$ intervals of equal size.
    $Width = \frac{max - min}{N}$
    2. **Equal-Frequency Partitioning:** Divides data so that each bin contains approximately the same number of records.

# Data Exploration

## 1. Descriptive Statistics Formulas

Descriptive statistics condense dataset characteristics into simple metrics.

### A. Univariate Statistics (Single Attribute)

Understanding the center and spread of one variable at a time.

1. **Mean (Arithmetic Average):**
The sum of all observations divided by the count.
$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$
2. **Standard Deviation (Spread/Variance):**
Measures how much values differ from the mean.
$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2}$
    
    *(Note: Using* $n-1$ *for sample standard deviation).*
    
3. **Range:**
The difference between the maximum and minimum values.
$Range = Max(x) - Min(x)$

### B. Multivariate Statistics (Correlation)

Measuring the relationship between two attributes $x$ and $y$.

- **Pearson Correlation Coefficient (**$r$**):**
Measures the strength of linear dependence between two variables.$r_{xy} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \sum_{i=1}^{n}(y_i - \bar{y})^2}} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{(n-1) \cdot s_x \cdot s_y}$
    - **Range:** $-1 \le r \le 1$
    - **+1:** Perfect positive correlation.
    - **1:** Perfect negative correlation.
    - **0:** No linear relationship.
    
    **Formula:**
    
    *(Where* $s_x$ *and* $s_y$ *are the standard deviations of* $x$ *and* $y$*).*
    

## 2. Data Visualization Formulas

### A. Normal Distribution Function (Bell Curve)

Used in Distribution Charts to visualize continuous numeric attributes. Instead of plotting raw data, you plot this function:

$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$

- $\mu$ (Mu): Mean of the distribution.
- $\sigma$ (Sigma): Standard deviation of the distribution.

### B. High-Dimensional Projection: Andrews Curves

A technique to visualize high-dimensional data by projecting each data point into a vector space as a curve.

- **Logic:**
Each data point $X = (x_1, x_2, x_3, ..., x_d)$ with $d$ dimensions defines a Fourier series function:
$f_x(t) = \frac{x_1}{\sqrt{2}} + x_2 \sin(t) + x_3 \cos(t) + x_4 \sin(2t) + x_5 \cos(2t) + \dots$
- **Plotting:** This function is plotted for $-\pi < t < \pi$.
- **Interpretation:**
    - **Similar points:** Curves will be close together.
    - **Different classes:** Curves will be far apart or have distinct shapes.
    - **Outliers:** Curves that look significantly different from the group.

# Classification

## 1. Performance Metrics (Evaluation)

How to mathematically measure if your classifier is "good."

### A. The Confusion Matrix (Base Counts)

For a binary classifier (Positive/Negative):

- **TP (True Positive):** Correctly predicted as Positive.
- **TN (True Negative):** Correctly predicted as Negative.
- **FP (False Positive):** Predicted Positive, but actually Negative (Type I Error).
- **FN (False Negative):** Predicted Negative, but actually Positive (Type II Error).

### B. Core Metric Formulas

1. **Accuracy:**
The overall percentage of correct predictions.
$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$
2. **Precision (Exactness):**
Of all the instances predicted as Positive, how many were actually Positive?
$Precision = \frac{TP}{TP + FP}$
3. **Recall (Sensitivity / True Positive Rate):**
Of all the actual Positive instances, how many did the classifier catch?
$Recall = \frac{TP}{TP + FN}$
4. **Specificity (True Negative Rate):**
Of all the actual Negative instances, how many did the classifier correctly identify?
$Specificity = \frac{TN}{TN + FP}$
5. **F-Measure (F1 Score):**
The harmonic mean of Precision and Recall. Used when you need a balance between the two.
$F_1 = \frac{2 \times Precision \times Recall}{Precision + Recall}$
    - **Generalized F-beta Score:**
    Weighted F-measure where $\beta$ determines the weight of recall vs. precision.
    $F_\beta = \frac{(1 + \beta^2) \times Precision \times Recall}{\beta^2 \times Precision + Recall}$

## 2. K-Nearest Neighbors (KNN)

An "Instance-Based" or "Lazy" learner. It stores all training data and classifies a new point based on its neighbors.

### A. Distance Formulas

To find the "nearest" neighbors, you calculate the distance between points $A(x_1, y_1)$ and $B(x_2, y_2)$.

1. **Euclidean Distance (Straight Line):**
The most common metric.
$d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$
2. **Manhattan Distance (City Block):**
The distance if you can only move along a grid (sum of absolute differences).
$d(A, B) = |x_1 - x_2| + |y_1 - y_2|$

### B. Decision Rules

Once the $K$ nearest neighbors are found:

- **Majority Vote:** Assign the class that appears most frequently among the neighbors.
- **Weighted Vote:** Give closer neighbors more influence (e.g., weight = $1/distance^2$).

## 3. Data Scaling Formulas

KNN relies on distance, so if one feature has a large range (e.g., salary: 20000-100000) and another is small (e.g., age: 0-100), salary will dominate. You must scale the data.

### A. Min-Max Normalization

Scales features to a fixed range, typically [0, 1].

$x' = \frac{x - min(x)}{max(x) - min(x)}$

### B. Z-Score Standardization

Scales features so they have a mean ($\mu$) of 0 and a standard deviation ($\sigma$) of 1.

$x' = \frac{x - \mu}{\sigma}$

## 4. AUC-ROC (Area Under Curve)

Used to compare binary classifiers across *all* possible decision thresholds.

1. **TPR (True Positive Rate):** Same as Recall. Plotted on Y-axis.
$TPR = \frac{TP}{TP + FN}$
2. **FPR (False Positive Rate):** Plotted on X-axis.
$FPR = \frac{FP}{TN + FP} = 1 - Specificity$
- **Logic:** You calculate TPR and FPR at various probability thresholds (e.g., >0.5, >0.6, >0.9) and plot the curve.
- **AUC (Area Under Curve):**
    - **1.0:** Perfect classifier.
    - **0.5:** Random guessing (diagonal line).

# Clustering

## 1. K-Means Clustering (Partitioning)

An iterative algorithm that splits data into $K$ disjoint clusters.

### A. The Centroid Formula

The "center" of a cluster is the arithmetic mean of all points assigned to it.
If cluster $C_k$ has $N$ points, the centroid $\mu_k$ is:

$\mu_k = \frac{1}{N} \sum_{x \in C_k} x$

*(Sum all the vectors in the cluster and divide by the count).*

### B. The Objective: Sum of Squared Errors (SSE)

We want to minimize the distance between every point $p$ and its cluster centroid $c_i$. This metric is used in the **Elbow Method** to find the best $K$.

$SSE = \sum_{i=1}^{K} \sum_{p \in C_i} (p - c_i)^2$

- **Elbow Method Logic:**
    1. Calculate SSE for $K=1, 2, 3...$
    2. Plot $K$ vs. SSE.
    3. Choose the $K$ where the drop in SSE starts to flatten (the "elbow").

## 2. Hierarchical Clustering (Agglomerative)

Starts with every point as its own cluster and merges them step-by-step. The key math is in **how** we measure the distance between two clusters ($X$ and $Y$).

### A. Linkage Metrics (Distance Formulas)

1. **Single Link (MIN):**
Distance between the **two closest** members (closest friends). Good for non-spherical shapes, sensitive to noise/bridges.
$dist_{sl}(X, Y) = \min_{x \in X, y \in Y} dist(x, y)$
2. **Complete Link (MAX):**
Distance between the **two farthest** members (farthest enemies). Produces tight, spherical clusters.
$dist_{cl}(X, Y) = \max_{x \in X, y \in Y} dist(x, y)$
3. **Average Link (AVG):**
Average distance between **all pairs** of points from both clusters.
$dist_{al}(X, Y) = \frac{1}{|X| \cdot |Y|} \sum_{x \in X} \sum_{y \in Y} dist(x, y)$

## 3. DBSCAN (Density-Based)

Does not use a formula to find centroids. Instead, it uses logic rules based on density.

### A. Parameters

- $\epsilon$ **(Eps):** The radius around a point.
- **MinPts:** Minimum number of points required within radius $\epsilon$ to form a dense region.

### B. Point Classification Logic

1. **Core Point:** Has $\ge MinPts$ neighbors within distance $\epsilon$.
2. **Border Point:** Has $< MinPts$ neighbors, but is close enough (within $\epsilon$) to a Core Point.
3. **Noise (Outlier):** Neither Core nor Border.

## 4. Evaluation Metrics

How to check if clustering is good without a teacher.

### A. Silhouette Coefficient

Measures how similar a point is to its own cluster compared to other clusters. Range: $[-1, 1]$.

For a single point $i$:

1. Calculate $a(i)$: Average distance to all other points in the **same** cluster (Cohesion).
2. Calculate $b(i)$: Average distance to all points in the **nearest neighboring** cluster (Separation).

**Formula:**

$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$

- **Interpretation:**
    - **Close to +1:** Well clustered (far from neighbors).
    - **0:** On the border/indifferent.
    - **Close to -1:** Assigned to the wrong cluster.

### B. Purity (External Validation)

If you know the true labels (Ground Truth), calculate how "pure" the clusters are.

$Purity = \frac{1}{N} \sum_{k} \max_j |C_k \cap L_j|$

*(Sum of the majority class count in each cluster, divided by total points).*

### C. Rand Index (RI)

Measures agreement between the clustering $X$ and ground truth $Y$.

$RI = \frac{a + b}{a + b + c + d}$

- **a:** Pairs in same cluster in $X$ AND same cluster in $Y$ (True Positive).
- **b:** Pairs in different cluster in $X$ AND different in $Y$ (True Negative).
- **c, d:** Disagreements.

# Association Rules

## 1. Core Metrics (The Formulas)

Association rules find relationships like "If you buy A, you likely buy B" ($A \rightarrow B$).

### A. Support (Frequency)

How popular is an itemset in the entire dataset?

- **Formula:**$Support(A) = \frac{\text{Transactions containing } A}{\text{Total Transactions}}$
- **Example:**
    - Total Transactions = 100.
    - 20 people bought Milk.
    - Support(Milk) = $20 / 100 = 0.2$ (or 20%).
- **Interpretation:** High support means the item is bought often.

### B. Confidence (Reliability)

If I buy $A$, how likely am I to *also* buy $B$? (Conditional Probability).

- **Formula:**$Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)}$
- **Example:**
    - 20 people bought Milk ($A$).
    - 15 of those 20 people *also* bought Bread ($B$).
    - Confidence(Milk $\rightarrow$ Bread) = $15 / 20 = 0.75$ (or 75%).
- **Interpretation:** "75% of Milk buyers also buy Bread."

### C. Lift (Correlation)

Is the relationship real, or just coincidence?

- **Formula:**$Lift(A \rightarrow B) = \frac{Confidence(A \rightarrow B)}{Support(B)} = \frac{Support(A \cup B)}{Support(A) \times Support(B)}$
- **Interpretation:**
    - **Lift > 1:** Positive correlation (Buying A *increases* chance of buying B).
    - **Lift = 1:** Independent (No relationship).
    - **Lift < 1:** Negative correlation (Buying A *decreases* chance of buying B).

## 2. The Apriori Algorithm

A strategy to find frequent itemsets efficiently without checking every possible combination.

### A. The Apriori Principle (Anti-Monotonicity)

**"If an itemset is frequent, then all of its subsets must also be frequent."**

- **Logic:** If `{Beer, Diapers}` is frequent, then `{Beer}` MUST be frequent.
- **Contrapositive (Pruning):** If `{Beer}` is NOT frequent, then `{Beer, Diapers}` CANNOT be frequent. **(Stop checking it!)**.

### B. Algorithm Steps

1. **Find Frequent 1-itemsets (**$L_1$**):** Count all individual items. Remove those below `min_support`.
2. **Join Step (Candidate Generation):** Combine frequent items to make larger sets ($k$-itemsets).
    - Join $L_{k-1}$ with itself.
3. **Prune Step:** Remove any candidate set that contains a subset which is NOT frequent (using the Apriori Principle).
4. **Repeat:** Count support for remaining candidates, keep the frequent ones, and move to $k+1$.
5. **Stop:** When no more frequent itemsets can be found.

## 3. Example Walkthrough

**Dataset:**

- T1: {Milk, Bread, Eggs}
- T2: {Milk, Bread}
- T3: {Milk, Eggs}
- T4: {Bread, Eggs}

**Settings:** `min_support` = 50% (2 transactions).

**Step 1: Count Items**

- Milk: 3 (Pass)
- Bread: 3 (Pass)
- Eggs: 3 (Pass)

**Step 2: Generate Pairs (Candidates)**

- {Milk, Bread}, {Milk, Eggs}, {Bread, Eggs}

**Step 3: Count Pairs**

- {Milk, Bread}: In T1, T2 -> Count = 2. Support = 50% (**Pass**)
- {Milk, Eggs}: In T1, T3 -> Count = 2. Support = 50% (**Pass**)
- {Bread, Eggs}: In T1, T4 -> Count = 2. Support = 50% (**Pass**)

**Step 4: Generate Triples**

- Candidate: {Milk, Bread, Eggs}
- **Prune Check:** Are all subsets ({Milk, Bread}, {Milk, Eggs}, {Bread, Eggs}) frequent? **Yes.**
- **Count Triple:** In T1 only -> Count = 1. Support = 25%. (**Fail** - below 50%).

**Result:** The largest frequent patterns are the pairs.

# Data Warehouse Algorithms & Logic

## 1. The Schema "Formulas" (Structure)

How do we organize the tables? This is the foundation of the warehouse.

### A. Star Schema (The Standard)

The simplest and most common design.

- **Logic:** Put the numbers (Facts) in the center, and the descriptive text (Dimensions) around it.
- **Formula:**$1 \text{ Fact Table} + N \text{ Dimension Tables}$
- **Key Rule:** Dimension tables are **denormalized**.
    - *Dummy Proof:* Instead of splitting "City" and "Country" into two tables, put "City" and "Country" in the *same* Customer table. It repeats data ("USA" appears many times), but it's **fast** to read (fewer joins).

### B. Snowflake Schema

- **Logic:** The "Normalized" version of the Star.
- **Key Rule:** Dimension tables are split into sub-tables.
    - *Example:* `Sales` $\rightarrow$ `Store` $\rightarrow$ `Region` $\rightarrow$ `Country`.
- **Trade-off:** Saves disk space (no repeated "USA"), but **slower** queries (requires many joins: $Sales \bowtie Store \bowtie Region \bowtie Country$).

## 2. OLAP Query Algorithms (The Moves)

How we navigate the data cube to find answers.

### A. Roll-up (Aggregation)

"Zooming Out." moving from detailed data to a summary.

- **Logic:** Climbing *up* the concept hierarchy.
- **Direction:** $Day \rightarrow Month \rightarrow Year$ or $City \rightarrow Country$.
- **Formula/Operation:**$\text{SUM(Sales) GROUP BY Year}$

### B. Drill-down

"Zooming In." The reverse of Roll-up.

- **Logic:** Climbing *down* the hierarchy to see details.
- **Direction:** $Year \rightarrow Month$ or $Country \rightarrow City$.
- **Operation:** Adding more columns to the `GROUP BY`.

### C. Slice & Dice (Filtering)

- **Slice:** Cutting the cube on **ONE** dimension.
    - *Formula:* `WHERE Year = 2023` (Result is a 2D page).
- **Dice:** Cutting the cube on **TWO or MORE** dimensions.
    - *Formula:* `WHERE Year = 2023 AND Product = 'Shoes'` (Result is a smaller sub-cube).

## 3. Changing Dimensions Algorithms (SCD)

The most "algorithmic" part. What happens when a customer moves or changes their name?

### Type 0: Retain Original (Do Nothing)

- **Algorithm:** Ignore the change.
- **Example:** Customer was born in "Berlin". They move to "Paris".
- **Result:** Database still says "Berlin". (Bad for addresses, good for "Date of Birth").

### Type 1: Overwrite (The Eraser)

- **Algorithm:** Update the specific cell. Old data is **lost forever**.
- **Logic:** `UPDATE Customer SET City = 'Paris' WHERE ID = 101`
- **Consequence:** All historical sales for this customer now look like they happened in Paris.
- **Use Case:** Correcting spelling errors.

### Type 2: Add New Row (The Historian) **[Most Important]**

- **Algorithm:** Keep the old row, create a new row with the new info.
- **Requirement:** You need **Surrogate Keys** (a new fake ID, like `Key_1`, `Key_2`) because the real Customer ID (`101`) is now duplicated.
- **Formulas/Columns Needed:**
    - `Valid_From`: Date the row started.
    - `Valid_To`: Date the row expired (NULL if current).
    - `Is_Current`: Flag (1 or 0).
- **Example Walkthrough:**
    1. **Row 1 (Old):** `SurrogateKey: 1` | `CustID: 101` | `City: Berlin` | `ValidTo: 2023-01-01`
    2. **Row 2 (New):** `SurrogateKey: 2` | `CustID: 101` | `City: Paris` | `ValidTo: NULL`

### Type 3: Add New Column (The Brief History)

- **Algorithm:** Keep the old value in a specific "Previous" column.
- **Structure:** Columns are `[Current_City, Previous_City]`.
- **Result:** `Current: Paris` | `Previous: Berlin`.
- **Limitation:** Can only remember the *immediate* past (can't handle moving from Berlin $\rightarrow$ London $\rightarrow$ Paris).

## 4. Measure Types (Math Rules)

When aggregating (Summing) numbers, you must follow these rules:

1. **Additive:** Can be summed across **ALL** dimensions.
    - *Example:* `Sales_Amount`. (Sum by Day? Yes. Sum by Store? Yes.)
2. **Semi-Additive:** Can be summed across **SOME** dimensions.
    - *Example:* `Inventory_Level` (Stock count).
    - *Logic:*
        - Sum across Stores? **Yes** (Total stock in company).
        - Sum across Time? **NO!** (Stock on Mon + Stock on Tue $\neq$ Real stock). You usually want *Average* or *Last Value* for time.
3. **Non-Additive:** Cannot be summed at all.
    - *Example:* `Unit_Price`, `Ratios`, `Temperature`.
    - *Logic:* You must use `AVG` or `MAX`, never `SUM`.

# Spatial Data & R-Tree Algorithms

## 1. Spatial Relationships (The Logic)

How do we know if two objects (like a Park and a Road) interact?

### A. Topological Relationships

Math rules for how two objects ($A$ and $B$) relate in space.

- **Disjoint:** No contact. (A is here, B is way over there).
    - *Formula:* $A \cap B = \emptyset$
- **Touch (Adjacent):** They kiss at the border but don't overlap inside.
    - *Formula:* $Boundary(A) \cap Boundary(B) \neq \emptyset$, but $Interior(A) \cap Interior(B) = \emptyset$.
- **Overlap:** They share some interior points, but not all.
- **Contains:** $A$ is fully inside $B$.
    - *Formula:* $A \subseteq B$.

## 2. R-Tree Structure (The "Box" Index)

A tree data structure used to index spatial data (like coordinates). It works by grouping nearby objects into boxes.

### A. MBR (Minimum Bounding Rectangle)

The smallest possible rectangle that can fully contain an object (or a group of objects).

- **Formula:**
    - $x_{min} = \min(\text{all x coords})$
    - $x_{max} = \max(\text{all x coords})$
    - $y_{min} = \min(\text{all y coords})$
    - $y_{max} = \max(\text{all y coords})$
- **Example:** Points (1,2) and (5,8).
    - MBR = Rectangle from (1,2) to (5,8).

### B. Tree Properties

- **Balanced:** All leaf nodes are at the same height (like a B-Tree).
- **Capacity:** Each node has between $m$ and $M$ entries. (e.g., must have at least 2 children, max 4).
- **Overlap:** Boxes *can* overlap (this is bad for performance, but allowed).

## 3. R-Tree Insertion Algorithm

How to add a new object $O$ into the tree.

### Step 1: Choose Leaf (Navigation)

Start at the root and go down. At each level, which child do we pick?

- **Rule:** Pick the child that needs the **Least Enlargement** to fit $O$.
- **Formula:**
    - Calculate Area of $Child_{MBR}$.
    - Calculate Area of ($Child_{MBR} \cup O$).
    - $Enlargement = \text{New Area} - \text{Old Area}$.
    - *Pick the child with the smallest Enlargement value.*

### Step 2: Handle Overflow (Splitting)

If the chosen leaf is full (already has $M$ entries), we must split it into two nodes ($L_1$ and $L_2$).

- **Goal:** Minimize the total area of $L_1 + L_2$.
- **Quadratic Split Algorithm (The Standard):**
    1. **Pick Seeds:** Find the two objects that would waste the most space if put in the same group (the "worst pair").
        - *Formula:* $Waste = Area(MBR(A, B)) - Area(A) - Area(B)$.
        - Pick pair with Max Waste.
    2. **Distribute:** Assign remaining objects to whichever seed they are closest to.

## 4. R*-Tree (Optimized R-Tree)

An improved version with smarter rules.

### Optimization Criteria

Instead of just minimizing "Area," it tries to minimize:

1. **Overlap:** (Crucial for search speed). If Node A and Node B overlap, a query might have to search *both*.
2. **Margin:** (Perimeter). Makes boxes more square-like. Square boxes pack better than long thin strips.

### Forced Re-Insertion (The Trick)

- **Logic:** When a node is full, **don't** split immediately.
- **Action:** Take the 30% of entries that are "farthest" from the center, remove them, and **re-insert** them into the tree.
- **Why?** This gives the tree a second chance to reorganize itself better without making a new node.

## 5. Bulk Loading (STR)

How to build a whole tree from scratch (instead of inserting 1 by 1).

### Sort-Tile-Recursive (STR) Algorithm

- **Step 1:** Sort all rectangles by $X$ coordinate.
- **Step 2:** Slice them into $N$ vertical columns.
- **Step 3:** Sort each column by $Y$ coordinate.
- **Step 4:** Pack them into nodes.
- **Result:** A highly optimized tree with almost zero overlap.

# R-Tree Query

## 1. The Distance Formulas (The "Yardsticks")

To find the Nearest Neighbor (NN), we need to measure the distance from a query point $P$ to a "Box" (MBR) before we even open it.

### A. MINDIST (The "Optimistic" Distance)

**"What is the closest this box *could possibly* be?"**

- **Logic:** The shortest distance from point $P$ to the **edge** of the rectangle $R$.
- **Why we need it:** If `MINDIST` > `Current_Best_Object`, we can **PRUNE** (ignore) this whole box.
- **Calculation (Dummy Proof):**
    - If $P$ is to the **left** of the box: $dist = x_{min} - p_x$
    - If $P$ is **inside** the box: $dist = 0$
    - If $P$ is to the **right** of the box: $dist = p_x - x_{max}$
    - *Repeat for Y-axis and combine (Pythagoras).*$MINDIST(P, R) = \sqrt{\sum (r_i - p_i)^2}$
        
        *(Where* $r_i$ *is the closest edge coordinate).*
        

### B. MINMAXDIST (The "Pessimistic" Distance)

**"What is the furthest I might have to travel to find *at least one* object in this box?"**

- **Logic:** It guarantees that there is an object *at least* this close inside.
- **Why we need it:** If `MINDIST(Box A)` > `MINMAXDIST(Box B)`, we can safely ignore Box A. Box B is **guaranteed** to have something closer than the *best case* of Box A.

## 2. Nearest Neighbor (NN) Algorithms

**Goal:** Find the 1 gas station closest to my GPS location.

### A. Depth-First Search (Branch-and-Bound)

**"The Diver"** - Goes deep into the tree, finds a candidate, then backtracks.

1. **Sort:** Look at all children. Sort them by `MINDIST` (closest first).
2. **Dive:** Go into the best child.
3. **Update Best:** If we find a real object at distance $d=5$, update `Best_Dist = 5`.
4. **Prune:** As we backtrack, if a sibling box has `MINDIST = 8` (which is $> 5$), **ignore it**.

### B. Best-First Search (The "Global" Planner)

**"The Scanner"** - Uses a global Priority Queue to always pick the absolute best box available anywhere.

1. **Queue:** Put the Root in a Priority Queue (sorted by `MINDIST`).
2. **Loop:**
    - Pop the top element (e.g., Box A with dist=2).
    - Is it an object? **Done!** (Since the queue is sorted, nothing else can be closer).
    - Is it a node? Open it, calculate `MINDIST` for all children, and throw them into the queue.
3. **Result:** Optimal I/O (opens fewer boxes than Depth-First).

## 3. Spatial Join Algorithm

**Goal:** "Find all overlapping Forests and Rivers." (Join Tree $R$ and Tree $S$).

### Synchronized Traversal

Instead of checking every forest against every river ($N \times M$ checks), we walk down both trees together.

1. Start at $Root_R$ and $Root_S$.
2. **Check:** Do $MBR(Root_R)$ and $MBR(Root_S)$ overlap?
    - **No:** Stop. Nothing inside can overlap.
    - **Yes:** Expand both.
3. **Recursion:** Compare every child of $R$ against every child of $S$. Only follow pairs that overlap.

## 4. Tree Size Formulas (Exam Math)

You might be asked to calculate the "Height" or "Fanout" of a tree given disk specs.

### A. Fanout ($M$) - "How many entries fit in a node?"

- **Variables:**
    - `Page_Size` (e.g., 4KB = 4096 bytes).
    - `Entry_Size` (e.g., 4 coordinates + 1 pointer = 36 bytes).
- **Formula:**$M = \lfloor \frac{\text{Page\_Size}}{\text{Entry\_Size}} \rfloor$
- **Example:**$M = \lfloor \frac{4096}{36} \rfloor = 113 \text{ entries per node}$

### B. Tree Height ($h$) - "How deep is the tree?"

- **Variables:**
    - `N`: Total number of objects (e.g., 1,000,000).
    - `M`: Fanout (calculated above, e.g., 113).
- **Formula:**$h = \lfloor \log_M(N) \rfloor$
    
    *(Log base M of N)*
    
- **Example:**$h = \log_{113}(1,000,000) \approx 3$
    
    *Interpretation:* You only need **3 disk clicks** to find any object in a million!