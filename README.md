# Portfolio Simulator
A Python-based backtesting tool to compare stock trading strategies on historical data.

<img width="703" height="650" alt="image" src="https://github.com/user-attachments/assets/c13d4417-90b1-4560-8cda-25ffd56e185a" />



## Features
- Fetches real historical stock data via Yahoo Finance
- Implements and compares multiple trading strategies
- Interactive web dashboard built with Plotly Dash
- Calculates key performance metrics (return, moving averages, Sharpe Ratio)

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
- [ ] Max Drawdown
- [ ] Support for multiple tickers
- [ ] Date range selector in dashboard
- [ ] Monte Carlo simulation
