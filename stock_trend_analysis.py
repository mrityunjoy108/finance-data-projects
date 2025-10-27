# Stock Market Trend Analysis - Project 2
# Author: Mrityunjoy
# Description: Analyze NIFTY 50 stock trend using Python (pandas, yfinance, matplotlib)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download NIFTY 50 data
ticker = "^NSEI"  # NIFTY 50 Index
data = yf.download(ticker, start="2024-01-01", end="2025-01-01")

# Step 2: Calculate moving averages
data["MA20"] = data["Close"].rolling(window=20).mean()   # 20-day moving average
data["MA50"] = data["Close"].rolling(window=50).mean()   # 50-day moving average

# Step 3: Plot the closing price and moving averages
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="NIFTY 50 Closing Price", linewidth=2, color="blue")
plt.plot(data["MA20"], label="20-Day Moving Average", linestyle="--", color="orange")
plt.plot(data["MA50"], label="50-Day Moving Average", linestyle="--", color="green")
plt.title("NIFTY 50 Stock Market Trend (2024)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)

# Step 4: Save the chart as an image
plt.savefig("nifty50_trend_chart.png", dpi=300)
plt.show()
