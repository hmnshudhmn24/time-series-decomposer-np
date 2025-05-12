# 📉 High-Performance Time Series Decomposer (NumPy)

This project implements a vectorized time series decomposition algorithm using **NumPy only** — breaking down a signal into **trend**, **seasonality**, and **residuals** without external statistical libraries.

## 🚀 Features

- Efficient moving average trend estimation
- Seasonal component extraction using grouped mean
- Residual calculation
- Fully interactive visualization with Streamlit

## 🔍 Why It's Unique

Unlike libraries like STL or Prophet, this tool:
- Uses pure NumPy for blazing-fast vectorized performance
- Works in real-time for small to mid-sized time series
- Offers simplicity + transparency of every calculation

## 📊 Sample Input Format

Upload a CSV like:

```
month,value
Jan,112
Feb,118
Mar,132
...
```

Make sure the column with numeric values (like `value`) is selected.

## 🧮 How It Works

- **Trend**: Smoothed using a simple moving average
- **Seasonality**: Calculated from average residuals for each cycle
- **Residuals**: Original - Trend - Seasonality

## 🛠️ How to Run

1. Install dependencies:

```bash
pip install numpy pandas matplotlib streamlit
```

2. Launch the app:

```bash
streamlit run src/main.py
```

## 📂 Project Structure

```
time_series_decomposer_np/
├── src/
│   └── main.py         # Streamlit app
├── README.md           # Project documentation
```

---

📉 Ideal for real-time analytics, ML preprocessing, and teaching signal decomposition!