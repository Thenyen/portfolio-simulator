import yfinance as yf

def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    return df["Close"].squeeze()