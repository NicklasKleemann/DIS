# Exponential Smoothing

## Exponential Smoothing

### Term definition table

| Term | Definition |
| --- | --- |
| Exponential Smoothing | A time-series forecasting method that gives **more weight to recent observations**. |
| Smoothing Parameter (α) | Controls how fast weights decay (0–1). |
| Level | Smoothed value of the series. |
| Trend | Direction of change over time. |
| Seasonality | Repeating pattern in time series. |
| Simple Exponential Smoothing | For data without trend or seasonality. |
| Holt’s Method | Adds trend. |
| Holt–Winters | Adds trend and seasonality. |

---

### Definition about the algorithm

**Exponential Smoothing** forecasts future values by combining past observations using **exponentially decreasing weights**, meaning recent values influence the prediction more than older ones.

---

### Advantages / disadvantages

**Advantages**

- Simple and fast.
- Works well for short-term forecasting.
- Handles noise effectively.
- Can be extended for trend and seasonality.

**Disadvantages**

- Poor for long-term forecasts.
- Requires tuning smoothing parameters.
- Not suitable for complex patterns.

---

### Math equation

### Simple Exponential Smoothing

$S_t = \alpha y_t + (1 - \alpha) S_{t-1}$

### Forecast

$\hat{y}_{t+1} = S_t$

---

### Runtime

Let:

- n = number of observations

**Training & Prediction**

- Best & Worst: $O(n)$

---

### Python-like pseudo code

```python
def exponential_smoothing(series, alpha):
     S = series[0]
 for tinrange(1,len(series)):
         S = alpha * series[t] + (1 - alpha) * S
return S
```

---

### Step-by-step through the algorithm

1. Choose smoothing parameter α.
2. Initialize the smoothed value.
3. For each new observation:
4. Update the smoothed value using the formula.
5. Use the final smoothed value as the forecast.