# Classification

# Definition

| Term | Definition |
| --- | --- |
| Supervised Learning | A learning approach that generalizes from known examples to automate decision-making processes |
| Classifcation | The process of predicting a discrete value (class label) from a pre-defined set based on input features |
| Regression | The process of predicting a continuous value from a continuous range (e.g., stock prices) |
| Training Set | The set of tuples (known examples) used to construct a model |
| Validation Set | A set of labeled data, independent of the training set, used to estimate model accuracy and tune parameters |
| Overfitting | A situation where a model focuses so much on the training data that it fails to generalize well to unseen data |
| Continuous Numeric Data | An $*N×N*$ table used to evaluate performance, where cell $*M[i,j]*$ counts the cases where ground truth $i$ is classified as $*j*$ |
| Precision | The measure of exactness, indicating how often a positive classification is correct $(TP/(TP+FP))$ |
| Recall (Sensitivity) | The measure of completeness, indicating how many actual positive cases are classified as positive $(TP/(TP+FN))$ |
| Accuracy | The fraction of time the classifier gives the correct classification $(TP+TN/All)$ |
| Decision Tree | A hierarchical model where internal nodes represent attributes (splits) and leaf nodes represent predicted class labels |
| Random Forest | An ensemble method consisting of a collection of decision trees, using majority voting to improve prediction and reduce overfitting |
| Eager Learning | Methods (like Decision Trees) that construct a classification model before receiving new data to classify |
| Lazy Learning | Methods (like KNN) that store training data as instances and perform processing only when a new instance needs classification |
| K Nearest Neighbors (KNN) | A classification method that assigns a class label based on the most frequent label among the $*K*$ closest items in the training set |
| Data Scaling | The process of adjusting data values (e.g., Standardization or Normalization) so features with different scales contribute appropriately to the model |
| Cross-Validation | A technique (e.g., $*k$-*fold) that splits data into mutually exclusive subsets to train and evaluate a model multiple times for better generalization estimates |
| Bootstrap | A sampling technique using uniform sampling with replacement to create training sets, often used when data is insufficient |
| ROC Curve | A graph showing the trade-off between the True Positive Rate (TPR) and the False Positive Rate (FPR) |
| AUC | The Area Under the ROC Curve; a measure of model accuracy where 1.0 is perfect and 0.5 represents random guessing |

## Classification and Model Evaluation

### Classification steps

- Model construction
- Model validation
- Model application (test)
- Training vs validation vs unseen data
- Feature selection and feature engineering

### Classification performance

- Ground truth vs predicted class
- True Positive (TP)
- False Positive (FP)
- False Negative (FN)
- True Negative (TN)
- Precision
- Recall
- Accuracy
- F-measure (F1, Fβ)
- Confusion matrix
- Multi-class performance

---

## Typical Classification Models

- Rule-based classifier
- Decision trees
- Random forest
- K-Nearest Neighbors (KNN)
- Eager vs lazy learning
- Overfitting

---

## Data Scaling

- Why data scaling is needed
- Standardization
- Normalization
- StandardScaler
- MinMaxScaler
- RobustScaler
- Normalizer
- When to use each

---

## Model Evaluation and Selection

### Data splitting

- Training set
- Validation (test) set
- Holdout method
- Random sampling

### Cross-validation

- k-fold cross validation
- Stratified k-fold
- Leave-one-out

### Model selection

- Hyperparameters vs model parameters
- Cross-validation for model choice
- Using all labeled data after validation

### Binary classifier evaluation

- Sensitivity (TPR)
- Specificity (TNR)
- False Positive Rate (FPR)
- False Negative Rate (FNR)
- Prediction probabilities
- Thresholds

### ROC and AUC

- ROC curve
- True Positive Rate vs False Positive Rate
- Area Under Curve (AUC)
- Random vs perfect classifier

---

[Classification steps](Classification/Classification%20steps%202e67c6b7cc2f800da571c91f73af28a7.md)

[Classification performance](Classification/Classification%20performance%202e67c6b7cc2f8058a4f7c842663e0a97.md)

[Typical Classification Models](Classification/Typical%20Classification%20Models%202e67c6b7cc2f802a874fcb35577b9b27.md)

[Data Scaling](Classification/Data%20Scaling%202e67c6b7cc2f80d79978c2822873a226.md)

[Model Evaluation and Selection](Classification/Model%20Evaluation%20and%20Selection%202e67c6b7cc2f805f994fffaa500cb090.md)