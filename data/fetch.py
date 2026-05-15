import yfinance as yf

def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    return df["Close"].squeeze()

def fetch_benchmark(start, end):
    df = yf.download("^GSPC", start=start, end=end, auto_adjust=True)
    benchmark = df["Close"].squeeze()
    # Normalize to 100 so it's comparable to any stock
    return benchmark / benchmark.iloc[0] * 100