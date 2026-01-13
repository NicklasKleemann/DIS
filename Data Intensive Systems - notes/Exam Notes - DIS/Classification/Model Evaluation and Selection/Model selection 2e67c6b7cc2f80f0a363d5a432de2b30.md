# Model selection

- Hyperparameters vs model parameters
- Cross-validation for model choice
- Using all labeled data after validation

# Model Selection

Model selection is the process of choosing **which type of classifier and which configuration** should be used for final deployment.

The slides emphasize that:

> The goal is not to find the best model on the training data, but the model with the best expected generalization to unseen data.
> 

---

## Hyperparameters vs Model Parameters

The slides make a clear distinction between:

### Model Parameters

These are learned automatically from the training data.

Examples:

- The structure of a decision tree
- The split thresholds
- The weights in a model

These values **cannot be set directly** by the user.

---

### Hyperparameters

These are set **before training** by the user.

Examples from the slides:

- K in KNN
- **Gini** vs **entropy in a decision tree**
- **test_size** and **random_state** in **train_test_split**

Hyperparameters control:

- How a model is built
- How complex it becomes

---

## Cross-Validation for Model Choice

The slides explain that cross-validation is used to:

- Compare different model types
- Compare different hyperparameter settings

Procedure:

1. Choose a model type (e.g., KNN, decision tree, random forest)
2. Try different hyperparameter values
3. Use cross-validation to evaluate each option
4. Select the model with the best **average CV performance**

This avoids choosing a model that only works well on one specific split.

---

## Using All Labeled Data After Validation

After cross-validation:

- The best model type and hyperparameters are chosen

Then the slides state:

> We train the selected model using all labeled data.
> 

Why?

- CV uses only parts of the data for training each time
- The final model should use **all available information**

Final workflow:

1. Use CV to select model + hyperparameters
2. Train the selected model on **100% of labeled data**
3. Apply it to unseen (real-world) data

---

## Summary

Model selection ensures:

- The chosen classifier generalizes well
- Hyperparameters are optimized
- All labeled data is used to build the final model

It separates **evaluation** from **final training**, which is critical for reliable machine learning.