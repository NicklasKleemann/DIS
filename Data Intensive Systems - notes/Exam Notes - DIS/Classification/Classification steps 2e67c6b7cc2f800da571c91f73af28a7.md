# Classification steps

- Model construction
- Model validation
- Model application (test)
- Training vs validation vs unseen data
- Feature selection and feature engineering

# Classification Steps

Classification is a **supervised learning process** in which a model is trained on labeled data and then used to predict the class of unseen data.

The slides describe classification as a **three-phase pipeline**:

**model construction → model validation → model application**.

---

## 1. Model Construction

Model construction is the phase where a classifier is built from **training data**.

The slides state that this phase includes:

- Learning a model that maps input attributes (features) to class labels
- Using labeled examples of the form
    
    $(x_1, x_2, \dots, x_n) \rightarrow y$
    
    where $x_i$ are features and y is the class
    

The training data is assumed to be **representative of future data**.

During construction:

- The algorithm learns patterns that distinguish different classes
- Parameters of the model are fitted
- Overfitting can occur if the model becomes too complex for the amount of data

---

## 2. Model Validation

Validation is used to **estimate how well the model will perform on new data**.

The slides emphasize that:

- The validation set must be **separate from the training set**
- It is used to detect **overfitting**

During validation:

- The model makes predictions on validation data
- These predictions are compared to the true labels
- Performance measures (accuracy, precision, recall, etc.) are computed

If the performance is poor:

- The model may need to be changed
- Features may need to be adjusted
- Hyperparameters may be tuned

---

## 3. Model Application (Test Phase)

After a model has been validated, it is used in the **test (application) phase**.

Here:

- The classifier is applied to **unseen data**
- The true class labels are unknown
- The goal is to make predictions for real-world use

The slides stress that:

> Test data must never be used during training or validation.
> 

This ensures an **unbiased estimate of real performance**.

---

## Training vs Validation vs Unseen Data

The slides clearly separate the three types of data:

| Data Type | Purpose |
| --- | --- |
| Training Data | Used to build the classification model |
| Validation Data | Used to tune and select the best model |
| Unseen (Test) Data | Used only to measure final performance |

Using the same data for all three leads to **overoptimistic results** and poor real-world performance.

---

## Feature Selection and Feature Engineering

The slides identify **features** as one of the most important factors in classification.

### Feature Selection

Feature selection means choosing a subset of attributes that:

- Are most relevant
- Improve accuracy
- Reduce overfitting

Irrelevant or redundant features:

- Add noise
- Increase complexity
- Decrease performance

---

### Feature Engineering

Feature engineering means:

- Creating new features
- Transforming existing ones

Examples from the slides include:

- Combining attributes
- Scaling numeric features
- Converting categorical data

Good features often matter **more than the choice of algorithm**.

---

## How the Steps Work Together

The full classification workflow is:

1. Select and engineer features
2. Train a model on training data
3. Validate it using separate validation data
4. Tune features and parameters
5. Apply the final model to unseen data

This process ensures:

- High predictive accuracy
- Good generalization
- Reliable evaluation

---

## Summary

Classification is not just running an algorithm.

It is a **controlled pipeline** that separates:

- Learning
- Testing
- Deployment

and relies heavily on:

- Proper data splitting
- Feature quality
- Validation before use.