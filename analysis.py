import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# STAGE 1 & 2: DATA PREPARATION, CLEANING, AND MERGING
# ==============================================================================

# --- 1. Load Data ---
try:
    df_sentiment = pd.read_csv('fear_greed_index.csv')
    df_trades = pd.read_csv('historical_data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: Make sure 'fear_greed_index.csv' and 'historical_data.csv' are in the same folder as this script.")
    exit()

# --- 2. Clean Sentiment Data ---
# Convert the 'date' column to a proper datetime format
df_sentiment['date'] = pd.to_datetime(df_sentiment['date'], format='%Y-%m-%d')

# --- 3. Clean Trading Data ---
# Convert 'Timestamp IST' to datetime object, specifying the format
df_trades['Timestamp IST'] = pd.to_datetime(
    df_trades['Timestamp IST'],
    format='%d-%m-%Y %H:%M',
    errors='coerce'
)

# Extract only the date part for merging with daily sentiment data
df_trades['date'] = df_trades['Timestamp IST'].dt.normalize()

# Filter for trades where PnL is non-zero (realized performance)
df_trades_closed = df_trades[df_trades['Closed PnL'] != 0].copy()


# --- 4. Merge Data ---
# Join trades with the daily sentiment
df_merged = pd.merge(
    df_trades_closed,
    df_sentiment[['date', 'classification', 'value']],
    on='date',
    how='left'
)

# Drop rows where classification (sentiment) is missing after the merge
df_merged.dropna(subset=['classification'], inplace=True)
print(f"Data merged successfully. Total closed trades for analysis: {len(df_merged)}")

# ==============================================================================
# STAGE 3: PERFORMANCE ANALYSIS (CALCULATING METRICS)
# ==============================================================================

# --- 5. Calculate Performance Metrics ---
# Create a column to identify winning trades
df_merged['Winning Trade'] = np.where(df_merged['Closed PnL'] > 0, 1, 0)

# Group by sentiment classification and calculate aggregates
performance_summary = df_merged.groupby('classification').agg(
    Total_PnL=('Closed PnL', 'sum'),
    Average_PnL=('Closed PnL', 'mean'),
    Trade_Count=('Closed PnL', 'count'),
    Win_Rate=('Winning Trade', 'mean')
).reset_index()

# Format the results
performance_summary['Win_Rate'] = (performance_summary['Win_Rate'] * 100).round(2)
performance_summary['Average_PnL'] = performance_summary['Average_PnL'].round(2)
performance_summary['Total_PnL'] = performance_summary['Total_PnL'].round(2)

# --- 6. Ordering for Visualization ---
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
performance_summary['classification'] = pd.Categorical(
    performance_summary['classification'],
    categories=sentiment_order,
    ordered=True
)
performance_summary = performance_summary.sort_values('classification')

# Display the final summary table
print("\n" + "="*60)
print("PERFORMANCE SUMMARY BY MARKET SENTIMENT CLASSIFICATION")
print(performance_summary.to_string(index=False))
print("="*60)

# ==============================================================================
# STAGE 4: VISUALIZATION
# ==============================================================================

# --- 7. Visualization: Average PnL by Sentiment ---
plt.figure(figsize=(10, 6))
# Colors based on PnL (though all are positive in this dataset)
bar_colors = ['green' if pnl > 0 else 'red' for pnl in performance_summary['Average_PnL']]

plt.bar(
    performance_summary['classification'],
    performance_summary['Average_PnL'],
    color=bar_colors
)

plt.title('Average Closed PnL per Trade by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Average Closed PnL (USD)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('average_pnl_by_sentiment.png')
plt.close()

# --- 8. Visualization: Win Rate by Sentiment ---
plt.figure(figsize=(10, 6))
plt.bar(
    performance_summary['classification'],
    performance_summary['Win_Rate'],
    color='skyblue'
)

plt.title('Win Rate by Market Sentiment Classification')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Win Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('win_rate_by_sentiment.png')
plt.close()

print("\nAnalysis Complete! Two charts ('average_pnl_by_sentiment.png' and 'win_rate_by_sentiment.png') have been saved to your project folder.")