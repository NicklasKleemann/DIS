# ARIMA

## ARIMA (AutoRegressive Integrated Moving Average)

### Term definition table

| Term | Definition |
| --- | --- |
| ARIMA | A time-series forecasting model combining **autoregression**, **differencing**, and **moving average**. |
| AR (p) | Uses past values to predict current value. |
| I (d) | Differencing to make the series stationary. |
| MA (q) | Uses past forecast errors. |
| Stationary | Time series with constant mean and variance. |
| Lag | Previous time step. |
| Residual | Prediction error. |
| White Noise | Random noise with zero mean. |

---

### Definition about the algorithm

**ARIMA** models a time series by using past values and past errors to predict future values.

It is widely used in **time-series forecasting** when data shows trends but no strong seasonality.

---

### Advantages / disadvantages

**Advantages**

- Powerful for short-term forecasting.
- Well-studied and interpretable.
- Works well for stationary or differenced data.

**Disadvantages**

- Requires stationary data.
- Poor for highly seasonal patterns.
- Parameter tuning is difficult.
- Not suitable for complex non-linear trends.

---

### Math equation

$y_t = c + \sum_{i=1}^{p} \phi_i y_{t-i} + \sum_{j=1}^{q} \theta_j \epsilon_{t-j} + \epsilon_t$

Where:

- p = AR order
- d = differencing
- q = MA order

---

### Runtime

Let:

- nnn = number of observations

**Training**

- Best: $O(n)$
- Worst: $O(n^2)$

**Prediction**

- Best & Worst: $O(p + q)$

---

### Python-like pseudo code

```python
def arima_forecast(series, p, d, q):
     series = difference(series, d)
     model = fit_arima(series, p, q)
return model.predict()
```

---

### Step-by-step through the algorithm

1. Check if the time series is stationary.
2. Apply differencing (d) if needed.
3. Choose p and q.
4. Fit AR and MA coefficients.
5. Validate residuals.
6. Use model to forecast future values.