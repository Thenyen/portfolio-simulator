from dash import Dash, dcc, html
import plotly.graph_objects as go
import pandas as pd
from data.fetch import fetch_data
from data.strategy import buy_and_hold, moving_average

app = Dash(__name__)

df = fetch_data("AAPL", "2020-01-01", "2024-01-01")
prices = df.squeeze().astype(float)

bah = buy_and_hold(df)
ma = moving_average(df)

fig = go.Figure()
fig.add_trace(go.Scatter(x=prices.index, y=prices.values, name="AAPL Kurs"))
fig.add_trace(go.Scatter(x=prices.index, y=prices.rolling(50).mean(), name="50-Tage MA"))
fig.add_trace(go.Scatter(x=prices.index, y=prices.rolling(200).mean(), name="200-Tage MA"))
fig.update_layout(title="AAPL Portfolio Simulator", xaxis_title="Datum", yaxis_title="Kurs ($)")

app.layout = html.Div([
    html.H1("Portfolio Simulator"),
    html.Div([
        html.Div([
            html.H3("Buy and Hold"),
            html.P(f"Rendite: {bah['rendite']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"}),
        html.Div([
            html.H3("Moving Average"),
            html.P(f"Rendite: {ma['rendite']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"})
    ], style={"display": "flex", "gap": "20px", "margin": "20px 0"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)