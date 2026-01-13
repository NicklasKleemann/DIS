# ROC and AUC

- ROC curve
- True Positive Rate vs False Positive Rate
- Area Under Curve (AUC)
- Random vs perfect classifier

# ROC and AUC

ROC and AUC are used to **compare binary classifiers** over all possible thresholds.

Instead of fixing one threshold, the ROC curve shows **how a classifier behaves when the threshold changes**.

---

## ROC Curve

ROC stands for **Receiver Operating Characteristics**.

To build a ROC curve, the slides describe this procedure:

1. Rank all classification results by **prediction probability** (from highest to lowest)
2. Move down the ranked list, one data point at a time
3. After each step:
    - Compute **TPR** (True Positive Rate)
    - Compute **FPR** (False Positive Rate)
4. Plot each point as (FPR,TPR)(FPR, TPR)(FPR,TPR)
5. Connect the points to form a curve

Each point corresponds to a **different threshold**.

---

## True Positive Rate vs False Positive Rate

The ROC curve plots:

- **X-axis**: False Positive Rate (FPR)

$FPR = \frac{FP}{TN + FP}$

- **Y-axis**: True Positive Rate (TPR)

$TPR = \frac{TP}{TP + FN}$

This shows the trade-off between:

- Catching positives (TPR)
- Avoiding false alarms (FPR)

A good classifier:

- Has high TPR
- Has low FPR

---

## Area Under the Curve (AUC)

The **AUC** is the area under the ROC curve.

It measures:

> The probability that a randomly chosen positive example is ranked higher than a randomly chosen negative example.
> 

From the slides:

- AUC = 1.0 → perfect classifier
- AUC = 0.5 → random guessing

The closer AUC is to **1**, the better the classifier.

---

## Random vs Perfect Classifier

The ROC diagram in the slides shows:

- **Random classifier** → diagonal line from (0,0) to (1,1)
    - AUC ≈ 0.5
- **Perfect classifier** → curve that goes straight up to (0,1) and then across
    - AUC = 1.0

A classifier that is close to the diagonal:

- Has little predictive power

A classifier that bows strongly toward the top-left:

- Is very accurate

---

## Why ROC and AUC Are Important

The slides emphasize that ROC and AUC:

- Do not depend on one specific threshold
- Allow fair comparison of different classifiers
- Are especially useful for imbalanced datasets

---

## Summary

ROC and AUC provide a **threshold-independent way** to evaluate binary classifiers.

They show:

- How TPR and FPR trade off
- How good a classifier is at ranking positives above negatives