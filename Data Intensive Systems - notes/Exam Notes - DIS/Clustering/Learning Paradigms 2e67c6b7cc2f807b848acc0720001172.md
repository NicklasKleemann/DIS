# Learning Paradigms

## Supervised Learning

- Learning from labeled examples
- Automating decision-making processes
- Classification
- Regression

## Unsupervised Learning

- Learning without labeled examples
- Working directly on input data
- Clustering
- Association rules
- Dimensionality reduction

# **Learning Paradigms: The Machine Learning Landscape**

## **1. System Map & Context**

- **Context:** The high-level categorization of how machines learn from data.
- **Input:** A dataset (labeled or unlabeled).
- **Output:** A model (function) that maps inputs to outputs or finds hidden structures.
- **Goal:** To generalize from training data to unseen data.
- **Dependency:** This is the parent topic for specific techniques like **Clustering** (see [Clustering](../Clustering%202e67c6b7cc2f8013bb8ee14da16cd338.md)).

> The Golden Thread: Spotify AI We continue fitting our entire understanding into the Spotify ecosystem.
> 
> - **The Problem:** Spotify has millions of songs and users. How do we automate value creation?
> - **Supervised:** "Train a bot to tag songs with 'Explicit' vs 'Clean' by showing it 10,000 examples."
> - **Unsupervised:** "Throw 1 million songs at the bot and ask it to find 'Playlists' (Groups) without telling it what a 'Metal' song looks like."

---

## **2. Supervised Learning**

**"Learning with a Teacher"**

In supervised learning, the system is given a dataset of example pairs $(x,y)$, where x*x* is the input and y is the **correct label**. The goal is to learn a mapping function $f(x)→y$.

### **A. Classification**

**Goal:** Predict a **discrete category** (Class Label).

- **Spotify Golden Thread:** **Genre tagging** or **Explicit Content Filter**.
    - *Input:* Audio waveform properties (Tempo, Pitch, Lyrics).
    - *Output:* "Pop", "Rock", "Jazz" OR "Explicit"/"Clean".
- **Key Algorithms:**
    - **Decision Trees:** "If bpm > 140 and distortion > 0.8 -> Metal".
    - **k-Nearest Neighbors (k-NN):** "This song looks like the 5 nearest songs, which are all Jazz".
    - **Support Vector Machines (SVM):** Draw a wide line separating "Pop" from "Rock".
    - **Neural Networks:** Deep Learning for complex audio analysis.

### **B. Regression**

**Goal:** Predict a **continuous number**.

- **Spotify Golden Thread:** **Popularity Prediction**.
    - *Input:* Artist followers, Release date, Genre trends.
    - *Output:* Predicted streams in first week (e.g., "1,450,200 streams").
- **Key Algorithms:**
    - **Linear Regression:** "Popularity increases linearly with Artist Followers".
    - **Polynomial Regression:** Modeling curves (e.g., hype cycles).

---

## **3. Unsupervised Learning**

**"Learning by Discovery"**

In unsupervised learning, the system is given only inputs *x* (Raw Data). There are **no labels** (*y*). The goal is to discover hidden **structure** or **patterns** in the data.

### **A. Clustering**

**Goal:** Group similar objects together.

- **Spotify Golden Thread:** **Auto-Playlist Generation**.
    - *Input:* Millions of songs (Tempo, Energy, Danceability).
    - *Output:* Disjoint groups (Cluster 1 = "Workout Music", Cluster 2 = "Chill Vibes").
- **Reference:** See [Clustering](../Clustering%202e67c6b7cc2f8013bb8ee14da16cd338.md) for the deep dive on K-Means, Hierarchical, and DBSCAN.

### **B. Dimensionality Reduction**

**Goal:** Reduce the number of variables (features) while keeping the important information.

- **Spotify Golden Thread:** **Song Fingerprinting**.
    - *Input:* A song has 10,000 raw audio features (too complex).
    - *Output:* Compress it to 50 "Principal Components" that describe 95% of the song's essence. This makes algorithms faster and visualizations possible (2D plots).
- **Key Algorithms:**
    - **PCA (Principal Component Analysis):** Squashes data into lower dimensions.

### **C. Association Rules**

**Goal:** Discover rules that describe relations between items.

- **Spotify Golden Thread:** **"Fans also like..."**
    - *Input:* specialized user listening history playlists.
    - *Output:* Rules like "If User listens to *The Beatles*, there is an 80% chance they also listen to *Queen*."
- **Key Concepts:**
    - **Support:** How often do these appear together?
    - **Confidence:** If A happens, how likely is B?

---

## **4. Comparison & Trade-offs**

| Feature | Supervised Learning | Unsupervised Learning |
| --- | --- | --- |
| **Data** | **Labeled** (Input + Output). Expensive to obtain (Human annotation required). | **Unlabeled** (Input only). Cheap and abundant (Raw data). |
| **Goal** | **Prediction** (Predict y for new x*x*). | **Description** (Find structure in x). |
| **Feedback** | Direct feedback (Error = predicted - actual). | No direct feedback (Interpretation required). |
| **Complexity** | Easier to metricize (Accuracy = 95%). | Harder to evaluate (Is this cluster "good"?). |
| **Examples** | Spam Filter, Face Recognition, Price Prediction. | Customer Segmentation, Anomaly Detection, Recommender Systems. |

---

## **5. Exam Checklist (The "Cheat Code")**

1. **Labeled vs Unlabeled?** This is the immediate discriminator. If you have "Targets" or "Answers", it's Supervised. If you only have "Data", it's Unsupervised.
2. **Discrete vs Continuous?**
    - Supervised + Discrete Output → **Classification**.
    - Supervised + Continuous Output → **Regression**.
3. **Grouping vs Simplifying?**
    - Unsupervised + Grouping → **Clustering**.
    - Unsupervised + Simplifying → **Dimensionality Reduction**.

1. **Spotify Context?** Always tie it back to the Golden Thread. "Are we teaching it what 'Rock' is (Supervised), or asking it what types of music exist (Unsupervised)?"