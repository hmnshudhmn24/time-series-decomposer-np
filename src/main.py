import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def moving_average(series, window):
    return np.convolve(series, np.ones(window)/window, mode='same')

def decompose(series, period):
    trend = moving_average(series, window=period)
    detrended = series - trend
    seasonal = np.array([np.nanmean(detrended[i::period]) for i in range(period)])
    seasonal = np.tile(seasonal, len(series) // period + 1)[:len(series)]
    residual = series - trend - seasonal
    return trend, seasonal, residual

def main():
    st.title("📉 High-Performance Time Series Decomposer")

    uploaded_file = st.file_uploader("Upload CSV with time series column", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("🗃️ Dataset Preview:")
        st.dataframe(df.head())

        column = st.selectbox("Select column for decomposition", df.select_dtypes(include=np.number).columns)
        period = st.slider("Set Seasonality Period", 2, 60, 12)

        series = df[column].values
        trend, seasonal, residual = decompose(series, period)

        st.write("🔍 Decomposition Components:")
        fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
        axs[0].plot(series, label="Original")
        axs[0].legend()
        axs[1].plot(trend, label="Trend", color="orange")
        axs[1].legend()
        axs[2].plot(seasonal, label="Seasonal", color="green")
        axs[2].legend()
        axs[3].plot(residual, label="Residual", color="red")
        axs[3].legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()