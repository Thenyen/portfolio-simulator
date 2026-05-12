from data.fetch import fetch_data

df = fetch_data("AAPL", "2020-01-01", "2024-01-01")
print(df)
