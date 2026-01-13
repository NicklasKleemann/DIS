# Logistic Regression

## Logistic Regression

### Term definition table

| Term | Definition |
| --- | --- |
| Logistic Regression | A supervised learning algorithm used for **classification** that models the probability of a class using a logistic (sigmoid) function. |
| Sigmoid Function | A function that maps any real number to a value between 0 and 1. |
| Logit | The linear combination of inputs before applying the sigmoid. |
| Probability | Output of the model interpreted as likelihood of class 1. |
| Decision Boundary | The threshold (usually 0.5) that separates classes. |
| Cross-Entropy Loss | The cost function used to train logistic regression. |
| Maximum Likelihood | Method used to estimate model parameters. |
| Odds | Ratio of probability of success to failure. |

---

### Definition about the algorithm

**Logistic Regression** predicts the **probability** that an input belongs to a class (usually class 1).

It applies a **sigmoid function** to a linear combination of the input features, producing a value between 0 and 1.

If this probability is above a threshold (commonly 0.5), the output is classified as 1; otherwise 0.

---

### Advantages / disadvantages

**Advantages**

- Outputs meaningful probabilities.
- Fast and efficient.
- Easy to interpret.
- Works well for linearly separable classes.
- Less prone to overfitting than complex models.

**Disadvantages**

- Cannot model non-linear decision boundaries.
- Sensitive to outliers.
- Requires feature scaling.
- Performs poorly when classes overlap heavily.

---

### Math equation

### Linear score

$z = w_1x_1 + w_2x_2 + \dots + w_dx_d + b$

### Sigmoid function

$\sigma(z) = \frac{1}{1 + e^{-z}}$

### Prediction

$P(y=1 \mid x) = \sigma(z)$

### Cross-entropy loss

$J = -\frac{1}{n}\sum_{i=1}^{n} \left[y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)\right]$

---

### Runtime

Let:

- n = number of samples
- d = number of features

**Training**

- Best: O(nd)
- Worst: $O(nd \cdot k)$ (k = number of gradient descent iterations)

**Prediction**

- Best & Worst: O(d)

---

### Python-like pseudo code

```python
defsigmoid(z):
return1 / (1 + exp(-z))

deffit_logistic_regression(X, y, lr=0.01, epochs=1000):
    w = [0] *len(X[0])
    b =0

for _inrange(epochs):
for iinrange(len(X)):
            z = dot(w, X[i]) + b
            y_hat = sigmoid(z)
            error = y_hat - y[i]

for jinrange(len(w)):
                w[j] -= lr * error * X[i][j]
            b -= lr * error

return w, b

defpredict(w, b, x):
return1if sigmoid(dot(w, x) + b) >=0.5else0

```

---

### Step-by-step through the algorithm

1. Initialize weights and bias to zero.
2. Compute a linear score for each data point.
3. Apply the sigmoid function to convert it into a probability.
4. Compute the cross-entropy loss.
5. Adjust the weights and bias to minimize the loss.
6. Repeat until convergence.
7. For a new input, compute its probability.
8. Classify it using a threshold (e.g., 0.5).