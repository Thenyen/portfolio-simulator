import pandas as pd


def buy_and_hold(df):
    start_price = df.iloc[0].item()
    end_price = df.iloc[-1].item()
    total_return = (end_price - start_price) / start_price * 100

    return {
        "strategie": "Buy and Hold",
        "startkurs": round(start_price, 2),
        "endkurs": round(end_price, 2),
        "rendite": round(total_return, 2)
    }


def moving_average(df, short=50, long=200):
    prices = df.squeeze().astype(float)

    data = pd.DataFrame()
    data["close"] = prices
    data["short_ma"] = prices.rolling(window=short).mean()
    data["long_ma"] = prices.rolling(window=long).mean()

    data["signal"] = 0
    data.loc[data["short_ma"] > data["long_ma"], "signal"] = 1

    data["rendite"] = data["close"].pct_change()
    data["strategie_rendite"] = data["signal"].shift(1) * data["rendite"]

    total_return = float((1 + data["strategie_rendite"]).prod() - 1)
    return {
        "strategie": "Moving Average (50/200)",
        "rendite": round(total_return * 100, 2)
    }


def sharpe_ratio(df):
    prices = df.squeeze().astype(float)
    daily_returns = prices.pct_change().dropna()

    mean_return = daily_returns.mean()
    std_return = daily_returns.std()

    sharpe = (mean_return / std_return) * (252 ** 0.5)

    return {
        "strategie": "Sharpe Ratio",
        "sharpe": round(float(sharpe), 2)
    }


def max_drawdown(df):
    prices = df.squeeze().astype(float)

    rolling_max = prices.cummax()
    drawdown = (prices - rolling_max) / rolling_max * 100

    max_dd = drawdown.min()

    return {
        "strategie": "Max Drawdown",
        "max_drawdown": round(float(max_dd), 2)
    }


def cagr(df, start, end):
    prices = df.squeeze().astype(float)

    start_price = prices.iloc[0]
    end_price = prices.iloc[-1]

    years = (pd.to_datetime(end) - pd.to_datetime(start)).days / 365.25

    cagr_value = ((end_price / start_price) ** (1 / years) - 1) * 100

    return {
        "strategie": "CAGR",
        "cagr": round(float(cagr_value), 2)
    }