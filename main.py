from data.fetch import fetch_data
from data.strategy import buy_and_hold, moving_average, sharpe_ratio
import plotly.express as px

df = fetch_data("AAPL", "2020-01-01", "2024-01-01")

ergebnis_bah = buy_and_hold(df)
ergebnis_ma = moving_average(df)
ergebnis_sharpe = sharpe_ratio(df)

print(ergebnis_bah)
print(ergebnis_ma)
print(ergebnis_sharpe)

fig = px.line(df, title="AAPL Kursentwicklung 2020–2024")
fig.show()