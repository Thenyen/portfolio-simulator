from data.fetch import fetch_data

df = fetch_data("AAPL", "2020-01-01", "2024-01-01")

# Buy-and-Hold Rendite
start_price = df.iloc[0].item()
end_price = df.iloc[-1].item()
total_return = (end_price - start_price) / start_price * 100

print(f"Startkurs:  {start_price:.2f} $")
print(f"Endkurs:    {end_price:.2f} $")
print(f"Rendite:    {total_return:.2f} %")