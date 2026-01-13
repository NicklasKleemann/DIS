# Classification performance

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

# Classification Performance

Classification performance measures **how well a classifier predicts the correct class**.

The slides emphasize that predictions must always be compared to the **ground truth** to evaluate a model.

---

## Ground Truth vs Predicted Class

- **Ground truth** is the true class label of a data point.
- **Predicted class** is the label produced by the classifier.

Performance evaluation is based on comparing:

predicted = $\text{predicted class} \quad \text{vs} \quad \text{true class}$

Every prediction falls into one of four possible outcomes.

---

## The Four Prediction Outcomes

| Outcome | Meaning |
| --- | --- |
| **True Positive (TP)** | The instance is positive and is predicted as positive |
| **False Positive (FP)** | The instance is negative but is predicted as positive |
| **False Negative (FN)** | The instance is positive but is predicted as negative |
| **True Negative (TN)** | The instance is negative and is predicted as negative |

These four numbers form the basis of all classification metrics.

---

## Confusion Matrix

The confusion matrix is a table that compares:

- **Actual class** (rows)
- **Predicted class** (columns)

|  | Predicted Positive | Predicted Negative |
| --- | --- | --- |
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |

The slides use this matrix as the **central tool** for computing all performance measures.

---

## Accuracy

Accuracy measures **how many predictions were correct**:

$Accuracy = \frac{TP + TN}{TP + FP + FN + TN}$

It works well when:

- Classes are balanced

It is misleading when:

- One class dominates (class imbalance)

---

## Precision

Precision measures:

> Of all predicted positives, how many were actually positive?
> 

$Precision = \frac{TP}{TP + FP}$

High precision means:

- Few false positives

Used when:

- False alarms are expensive

---

## Recall (Sensitivity)

Recall measures:

> Of all actual positives, how many were detected?
> 

$Recall = \frac{TP}{TP + FN}$

High recall means:

- Few missed positives

Used when:

- Missing a positive case is costly

---

## F-Measure

Precision and recall often conflict, so the slides introduce the **F-measure**.

### F1 Score

Balances precision and recall equally:

$F_1 = \frac{2 \cdot Precision \cdot Recall}{Precision + Recall}$

### Fβ Score

Allows weighting recall more than precision:

$F_{β} = \frac{(1+\beta^2)\cdot P \cdot R}{\beta^2 \cdot P + R}$

If β > 1:

- Recall is more important
    
    If β < 1:
    
- Precision is more important

---

## Why Accuracy Is Not Enough

The slides emphasize:

> A classifier can have high accuracy but still be useless.
> 

Example:

- If 95% of samples are negative, a classifier that always predicts “negative” has 95% accuracy but zero recall for positives.

Therefore:

- Precision
- Recall
- F-measure

must be used.

---

## Multi-Class Performance

When more than two classes exist:

- A confusion matrix is built for each class using **one-vs-all** comparisons.

For each class:

- That class is treated as “positive”
- All others are treated as “negative”

Metrics are computed per class and then:

- Averaged
- Or analyzed individually

---

## Summary

Classification performance is based on:

- Comparing predictions to ground truth
- Counting TP, FP, FN, TN
- Computing precision, recall, accuracy, and F-measure

The confusion matrix is the **core evaluation tool** and all metrics come from it.