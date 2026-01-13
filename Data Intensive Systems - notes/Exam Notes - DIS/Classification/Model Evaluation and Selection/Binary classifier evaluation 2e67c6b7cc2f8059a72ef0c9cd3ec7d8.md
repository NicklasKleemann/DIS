# Binary classifier evaluation

- Sensitivity (TPR)
- Specificity (TNR)
- False Positive Rate (FPR)
- False Negative Rate (FNR)
- Prediction probabilities
- Thresholds

# Binary Classifier Evaluation

Binary classification evaluates a model that predicts **two classes** (positive vs negative).

All measures are derived from the **confusion matrix** with:

- **TP** (True Positive), **FP** (False Positive),
- **FN** (False Negative), **TN** (True Negative).

---

## Sensitivity (True Positive Rate, TPR, Recall)

Measures how many actual positives are correctly detected:

$\text{TPR} = \frac{TP}{TP + FN}$

High TPR means:

- The classifier rarely misses positive cases.

Used when:

- Missing a positive is costly (e.g., disease, fraud). 7. Classification

---

## Specificity (True Negative Rate, TNR)

Measures how many actual negatives are correctly rejected:

$\text{TNR} = \frac{TN}{TN + FP}$

High TNR means:

- The classifier produces few false alarms. 7. Classification

---

## False Positive Rate (FPR)

Fraction of negatives incorrectly labeled as positive:

$\text{FPR} = \frac{FP}{TN + FP} = 1 - \text{TNR}$

High FPR means:

- Many false alarms (e.g., innocent users flagged). 7. Classification

---

## False Negative Rate (FNR)

Fraction of positives incorrectly labeled as negative:

$\text{FNR} = \frac{FN}{TP + FN} = 1 - \text{TPR}$

High FNR means:

- Many true positives are missed. 7. Classification

---

## Prediction Probabilities

Many classifiers output **probabilities** for each class instead of a hard label.

Example: a point might be predicted as **P(positive)=0.72**, **P(negative)=0.28**.

These probabilities allow:

- Ranking predictions
- Adjusting how strict the classifier is
- Building ROC curves later 7. Classification

---

## Thresholds

A **threshold** converts probabilities into class labels.

Typical default:

Predict positive if $P(\text{positive}) \ge 0.5$

Changing the threshold changes behavior:

- **Lower threshold** → more positives predicted
    - Higher TPR, higher FPR
- **Higher threshold** → fewer positives predicted
    - Lower FPR, higher FNR

Thus, different thresholds produce **different confusion matrices** and therefore different TPR, FPR, etc. 
7. Classification

---

## Why Thresholds Matter

The slides emphasize that:

> Different thresholds lead to different metric values.
> 

So in practice:

- We do **not** evaluate a classifier at a single threshold
- We analyze performance **across all thresholds** (this leads to ROC/AUC)

---

## Summary

Binary evaluation is based on:

- TPR (sensitivity)
- TNR (specificity)
- FPR and FNR

Using **prediction probabilities and thresholds**, we can tune a classifier for:

- Fewer false alarms
- Fewer missed positives
    
    depending on the application.