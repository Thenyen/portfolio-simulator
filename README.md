# Portfolio Simulator
A Python-based backtesting tool to compare stock trading strategies on historical data.

<img width="721" height="721" alt="image" src="https://github.com/user-attachments/assets/7f2bda92-f0d4-40e2-a399-86485353ffe4" />
<img width="721" height="522" alt="image" src="https://github.com/user-attachments/assets/cf0be2de-9580-48bb-aad6-e4cf59948c2a" />





## Features
- Fetches real historical stock data via Yahoo Finance
- Implements and compares multiple trading strategies
- Interactive web dashboard built with Plotly Dash
- Calculates key performance metrics (return, moving averages, Sharpe Ratio, Max      Drawdown)
- Interactive ticker selection (AAPL, MSFT, SAP, AMZN)
- Date range selector in dashboard - customize the backtest period
- CAGR (Compound Annual Growth Rate) for annualized return comparison
- Monte Carlo simulation with 200 paths for 1-year price forecasting

## Quickstart

```bash
git clone https://github.com/Thenyen/portfolio-simulator.git
cd portfolio-simulator
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8050` in your browser.

## Strategies
**Buy and Hold** — buys at the start and holds until the end of the period. Simple but hard to beat.

**Moving Average (50/200)** — buys when the 50-day average crosses above the 200-day average (Golden Cross), sells on the reverse (Death Cross).

**Sharpe Ratio** — measures risk-adjusted return. Divides the average daily return by its standard deviation, annualized over 252 trading days. A ratio above 1.0 is considered good, above 2.0 excellent.

**Max Drawdown** - measures the largest peak-to-trough decline of a portfolio during the backtest period.
A lower drawdown indicates lower downside risk.

**CAGR** — measures the mean annual growth rate over the selected time period. More meaningful than total return alone as it accounts for the length of the investment.

**Monte Carlo Simulation** — uses historical daily return and volatility to simulate 200 possible price paths for the next trading year. Visualizes the range of possible outcomes based on past behavior.

## Project Structure

    portfolio-simulator/
    ├── data/
    │   ├── fetch.py       # Downloads stock data via yfinance
    │   └── strategy.py    # Trading strategy implementations
    ├── app.py             # Dash dashboard
    ├── main.py            # Quick CLI output
    └── requirements.txt

## Roadmap
- [x] Sharpe Ratio
- [x] Max Drawdown
- [x] Support for multiple tickers
- [x] Date range selector in dashboard
- [x] Benchmark comparison (S&P 500)
- [ ] Extend data range to 2026
- [ ] Multi-stock portfolio (combine multiple tickers)
- [x] Monte Carlo simulation
- [ ] Monte Carlo: Simulation vs. Reality
- [ ] Export results as CSV
- [ ] Improve dashboard UI (colors, layout)
- [x] Add more stocks (DAX, NASDAQ, global indices)
- [x] Annualized return (CAGR)
- [ ] Portfolio weight allocation
