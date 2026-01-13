# Support Vector Machine (SVM)

## Support Vector Machine (SVM)

### Term definition table

| Term | Definition |
| --- | --- |
| Support Vector Machine (SVM) | A supervised learning algorithm that finds the **best separating boundary** between classes by maximizing the margin. |
| Hyperplane | A decision boundary that separates classes in feature space. |
| Margin | The distance between the hyperplane and the closest data points. |
| Support Vectors | The data points that lie closest to the decision boundary and define the margin. |
| Kernel | A function that maps data into a higher-dimensional space. |
| Linear SVM | SVM using a straight-line (hyperplane) boundary. |
| Soft Margin | Allows some misclassifications for better generalization. |
| Regularization (C) | Controls trade-off between margin size and classification errors. |

---

### Definition about the algorithm

**Support Vector Machine** finds the hyperplane that separates two classes with the **maximum margin**.

Instead of simply separating the data, SVM chooses the boundary that is **as far as possible** from the nearest points of both classes, making it more robust to noise and unseen data.

---

### Advantages / disadvantages

**Advantages**

- Works well in high-dimensional spaces.
- Very strong theoretical foundation.
- Effective even when number of features > number of samples.
- Can model non-linear boundaries using kernels.

**Disadvantages**

- Choosing the right kernel and parameters is difficult.
- Computationally expensive for large datasets.
- Not easily interpretable.
- Sensitive to noisy data if C is large.

---

### Math equation

### Decision boundary

$w \cdot x + b = 0$

### Margin constraints

$w \cdot x_i + b \ge 1 \quad \text{if } y_i = 1$

$w \cdot x_i + b \le -1 \quad \text{if } y_i = -1$

### Optimization objective

$\min_{w,b} \frac{1}{2} \|w\|^2$

(soft margin adds slack variables and penalty C)

---

### Runtime

Let:

- n = number of samples
- d = number of features

**Training**

- Best: $O(n^2)$
- Worst: $O(n^3)$

**Prediction**

- Best & Worst: O(d)

---

### Python-like pseudo code

```python
deffit_svm(X, y, lr=0.01, epochs=1000, C=1):
    w = [0] *len(X[0])
    b =0

for _inrange(epochs):
for iinrange(len(X)):
            condition = y[i] * (dot(w, X[i]) + b)
if condition <1:
                w = w - lr * (w - C * y[i] * X[i])
                b = b + lr * C * y[i]
else:
                w = w - lr * w

return w, b

defpredict(w, b, x):
return1if dot(w, x) + b >= 0 else -1
```

---

### Step-by-step through the algorithm

1. Choose a kernel (linear by default).
2. Initialize weights and bias.
3. Find the hyperplane that separates the two classes.
4. Adjust the hyperplane to maximize the margin.
5. Identify the support vectors.
6. Optimize using gradient descent or quadratic programming.
7. Use the hyperplane to classify new data points.