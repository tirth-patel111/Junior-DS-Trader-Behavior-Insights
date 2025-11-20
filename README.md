📘 Trader Performance & Bitcoin Market Sentiment: A Quantitative Research Study
A Data-Driven Examination of Behavioral Patterns in Crypto Derivatives Trading


🔍 Abstract:-
This study investigates the impact of Bitcoin market sentiment, measured using the Fear & Greed Index, on trader performance and behavioral patterns within the Hyperliquid derivatives ecosystem.
By integrating sentiment metrics with granular trade execution data, the analysis explores correlations between emotional market states and trading outcomes such as PnL, leverage usage, position sizing, and directional bias.
The results contribute to understanding how psychological indicators influence market microstructure dynamics and trader decision-making.


📁 Dataset Description
1. Bitcoin Fear & Greed Index
File: fear_greed_index.csv
Features:
Date
Classification (Fear / Greed)
Represents daily market sentiment driven by volatility, volume, social signals, and dominance metrics.


2. Hyperliquid Trader Historical Dataset
File: historical_trader_data.csv
Key Features Include:-
account
symbol
side (long/short)
execution price
size
start position
event (open/close)
closedPnL
leverage
timestamp
Offers granular visibility into derivatives trading activity, risk behavior, and trade outcomes.



🎯 Research Objectives:-
Quantify the relationship between market sentiment and trader PnL performance.
Analyze behavioral shifts in trading activity during Fear vs. Greed states.
Identify predictive indicators of performance linked to sentiment-driven volatility.
Examine micro-level features, including:
Leverage behavior
Long/Short distribution
Position sizing dynamics
Execution timing patterns
The overarching goal is to map emotional market cycles to measurable market participant behavior.


🧬 Methodology
1. Data Preprocessing
Timestamp normalization
Handling missing & anomalous values
Categorizing sentiment windows
Mapping trades to sentiment periods via temporal merging

2. Feature Engineering
PnL-to-size normalization
Leverage buckets (low / medium / high risk)
Sentiment-adjusted trade outcome labels
Volatility-adjusted performance metrics

3. Analytical Framework
Time-series decomposition
Distribution analysis
Hypothesis testing (e.g., PnL in Greed > PnL in Fear?)
Correlation matrices
Behavioral clustering
Sentiment-conditioned performance curves

4. Visualization
Multi-index time-series plots
Profitability heatmaps
Sentiment-classified violin plots
Trader behavior radar charts


📊 Key Research Questions:-
Do traders perform significantly better during Greed market conditions?
Does leverage increase when market sentiment turns greedy?
Is trader activity more aggressive (larger size / more frequent trades) during high-emotion periods?
How does sentiment affect long vs. short bias?
Can sentiment metrics be used predictively for trading models?


📈 Preliminary Findings (Summary):-
Fear periods exhibit higher volatility and wider PnL dispersion.
Leverage usage spikes during Greed, often resulting in amplified losses.
Traders show a stronger long bias during Greed phases.
Certain accounts consistently perform better in Fear environments — indicating contrarian strategies.
Sentiment windows correlate with statistically significant differences in performance distributions.


🛠️ Tech Stack:-
Python: Pandas, NumPy, Matplotlib, Altair, Scikit-learn
Data Engineering: Temporal joining, feature engineering
Visualization: PDF report (ReportLab), charts, analytical dashboards
Version Control: Git / GitHub


📄 Project Deliverables:-
analysis.ipynb — Full exploratory notebook
merged_data.csv — Final dataset after preprocessing
visuals/ — Plots, heatmaps, charts
final_report.pdf — Executive summary and insights
README.md — Documentation


🚀 Reproducibility Instructions:-
Install Dependencies
pip install -r requirements.txt

Run Analysis
jupyter notebook analysis.ipynb

Generate PDF Report
python generate_report.py


🧠 Future Work:-
Sentiment-aware predictive modeling (LSTM / Gradient Boosted Trees)
Reinforcement-learning-based trading strategy simulation
Regime detection using Hidden Markov Models
Real-time inference pipeline with streaming sentiment data
