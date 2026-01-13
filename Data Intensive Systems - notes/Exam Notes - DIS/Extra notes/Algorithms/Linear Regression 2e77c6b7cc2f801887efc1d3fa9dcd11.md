# Linear Regression

## Linear Regression

### Term definition table

| Term | Definition |
| --- | --- |
| Linear Regression | A supervised learning algorithm that models the relationship between inputs and a **continuous output** using a linear equation. |
| Dependent Variable | The target variable we want to predict. |
| Independent Variable | Input feature(s) used to predict the target. |
| Weight (Coefficient) | The slope of a feature in the linear model. |
| Bias (Intercept) | The value of y when all inputs are zero. |
| Residual | Difference between predicted and actual value. |
| Least Squares | Method that fits the line by minimizing squared residuals. |
| Cost Function | A function measuring prediction error (usually MSE). |
| Overfitting | Model fits noise instead of true pattern. |
| Underfitting | Model too simple to capture pattern. |

---

### Definition about the algorithm

**Linear Regression** predicts a numeric value by fitting a straight line (or hyperplane) that best describes the relationship between input features and the output.

The model finds parameters that minimize the total squared prediction error between predicted and actual values.

---

### Advantages / disadvantages

**Advantages**

- Simple and easy to interpret.
- Fast to train and predict.
- Works well when the relationship is roughly linear.
- Provides insight into feature importance.

**Disadvantages**

- Cannot model non-linear relationships.
- Sensitive to outliers.
- Assumes independence between features.
- Poor performance if assumptions are violated.

---

### Math equation

### Linear model

For one feature:

$y = wx + b$

For multiple features:

$y = w_1x_1 + w_2x_2 + \dots + w_dx_d + b$

### Mean Squared Error (MSE)

$J(w,b) = \frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

### Normal Equation (closed form)

$\mathbf{w} = (X^T X)^{-1} X^T y$

---

### Runtime

Let:

- n = number of samples
- d = number of features

**Training**

- Best: O(nd) (gradient descent, few iterations)
- Worst: $O(d^3 + nd^2)$ (normal equation matrix inversion)

**Prediction**

- Best & Worst: O(d)

---

### Python-like pseudo code

```python
deffit_linear_regression(X, y, lr=0.01, epochs=1000):
    w = [0] *len(X[0])
    b =0

for _inrange(epochs):
for iinrange(len(X)):
            y_hat = dot(w, X[i]) + b
            error = y_hat - y[i]

for jinrange(len(w)):
                w[j] -= lr * error * X[i][j]
            b -= lr * error

return w, b

defpredict(w, b, x):
return dot(w, x) + b
```

---

### Step-by-step through the algorithm

1. Assume a linear model $y = wx + b$.
2. Initialize all weights and bias to 0.
3. For each training example:
4. Predict y using current parameters.
5. Compute the error between prediction and actual value.
6. Update weights and bias to reduce the error.
7. Repeat until the error is minimized.
8. Use the learned equation to predict new values.