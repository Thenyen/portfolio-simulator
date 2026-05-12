from data.fetch import fetch_data
import plotly.express as px

df = fetch_data("AAPL", "2020-01-01", "2024-01-01")

fig = px.line(df, title="AAPL Kursentwicklung 2020–2024")
fig.show()