# Cross-validation

- k-fold cross validation
- Stratified k-fold
- Leave-one-out

# Cross-Validation

Cross-validation (CV) is a method for **estimating how well a type of model will generalize to unseen data**.

The slides emphasize:

> Cross-validation is not used to build the final model.
> 
> 
> It is used to **compare models and tune hyperparameters**.
> 

---

## k-Fold Cross-Validation

In **k-fold cross-validation**:

1. The labeled dataset is split into **k equal parts (folds)**
2. For each iteration:
    - One fold is used as validation data
    - The remaining k-1folds are used as training data
3. This is repeated **k times**
4. The final performance is the **average of the k results**

This ensures:

- Every data point is used for validation exactly once
- More reliable evaluation than a single holdout split

---

## Problem with Standard k-Fold

The slides show that if the **class distribution is uneven**, standard k-fold can produce bad folds.

Example:

- One fold may contain mostly one class
- Another fold may contain very few samples of a class

This leads to:

- Biased performance estimates

---

## Stratified k-Fold

**Stratified k-fold** fixes this.

It ensures:

- Each fold has **approximately the same class distribution** as the full dataset

This is especially important for:

- Class-imbalanced data

The slides note that:

> Stratified 5-fold is the default in scikit-learn.
> 

---

## Leave-One-Out Cross-Validation (LOO)

Leave-one-out is an extreme case of k-fold where:

$\text{number of data points}$

Procedure:

- Train on all data except one point
- Test on that one point
- Repeat for every data point

Advantages:

- Uses almost all data for training each time
- Good for very small datasets

Disadvantages:

- Very expensive to compute

---

## What Cross-Validation Is Used For

The slides state that CV is used to:

- Compare model types (DT, RF, KNN, etc.)
- Tune hyperparameters (K in KNN, depth of trees, etc.)

It does **not** produce the final deployable model.

---

## Summary

Cross-validation provides:

- Reliable model evaluation
- Protection against overfitting
- A way to choose the best model and hyperparameters

Stratified k-fold is the preferred method when class distributions matter.