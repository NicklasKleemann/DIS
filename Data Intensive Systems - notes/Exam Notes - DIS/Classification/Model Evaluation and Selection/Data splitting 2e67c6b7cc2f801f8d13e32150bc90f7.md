# Data splitting

- Training set
- Validation (test) set
- Holdout method
- Random sampling

# Data Splitting

Data splitting is used to **separate learning from evaluation**.

The slides emphasize that **a model must never be evaluated on the same data it was trained on**, otherwise the performance estimate is misleading.

---

## Training Set

The **training set** is the portion of labeled data used to:

- Construct the classification model
- Learn patterns and parameters

All algorithms (Decision Tree, Random Forest, KNN, etc.) use only the training set to:

- Fit their internal parameters
- Build decision rules

If the training data is not representative of the real-world data, the model will not generalize.

---

## Validation (Test) Set

The **validation set** (sometimes called the test set) is used to:

- Measure how well the trained model performs
- Tune hyperparameters
- Compare different models

The slides stress:

> Validation data must be independent of the training data, otherwise overfitting occurs.
> 

Predictions are compared with known labels to compute:

- Accuracy
- Precision
- Recall
- F-measure

---

## Holdout Method

The **holdout method** is the simplest data splitting technique.

Procedure:

1. Randomly split labeled data into two parts
    - Training set (e.g., 2/3)
    - Validation set (e.g., 1/3)
2. Train the model on the training set
3. Evaluate it on the validation set

The result is one estimate of model performance.

---

## Random Sampling

Random sampling is a variant of the holdout method.

It:

- Repeats the holdout process multiple times
- Each time uses a different random split

Final performance is:

$\text{Average of all holdout accuracies}$

This reduces the risk that a single unlucky split gives a misleading result.

---

## Why Data Splitting Matters

The slides emphasize:

> Different ways of splitting the same data can lead to different models and different performance.
> 

Therefore:

- Data splitting is part of model selection
- It directly affects the reliability of evaluation

---

## Summary

Data splitting ensures that:

- Learning and evaluation are separated
- Overfitting can be detected
- Model performance reflects real-world behavior

Holdout and random sampling provide simple but important ways to estimate how well a classifier generalizes.