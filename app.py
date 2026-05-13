from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objects as go
from data.fetch import fetch_data
from data.strategy import buy_and_hold, moving_average, sharpe_ratio, max_drawdown

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Portfolio Simulator"),
    dcc.Dropdown(
        id="ticker-dropdown",
        options=[
            {"label": "Apple (AAPL)", "value": "AAPL"},
            {"label": "Microsoft (MSFT)", "value": "MSFT"},
            {"label": "SAP (SAP.DE)", "value": "SAP.DE"},
            {"label": "Amazon (AMZN)", "value": "AMZN"},
        ],
        value="AAPL",
        style={"width": "300px", "margin": "20px 0"}
    ),
    html.Div(id="metrics", style={"display": "flex", "gap": "20px", "margin": "20px 0"}),
    dcc.Graph(id="price-chart")
])

@callback(
    Output("metrics", "children"),
    Output("price-chart", "figure"),
    Input("ticker-dropdown", "value")
)
def update_dashboard(ticker):
    df = fetch_data(ticker, "2020-01-01", "2024-01-01")
    prices = df.squeeze().astype(float)

    bah = buy_and_hold(df)
    ma = moving_average(df)
    sharpe = sharpe_ratio(df)
    dd = max_drawdown(df)

    metrics = [
        html.Div([
            html.H3("Buy and Hold"),
            html.P(f"Return: {bah['rendite']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"}),
        html.Div([
            html.H3("Moving Average"),
            html.P(f"Return: {ma['rendite']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"}),
        html.Div([
            html.H3("Sharpe Ratio"),
            html.P(f"Sharpe: {sharpe['sharpe']}")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"}),
        html.Div([
            html.H3("Max Drawdown"),
            html.P(f"Drawdown: {dd['max_drawdown']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"})
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices.index, y=prices.values, name=f"{ticker} Kurs"))
    fig.add_trace(go.Scatter(x=prices.index, y=prices.rolling(50).mean(), name="50-Tage MA"))
    fig.add_trace(go.Scatter(x=prices.index, y=prices.rolling(200).mean(), name="200-Tage MA"))
    fig.update_layout(title=f"{ticker} Portfolio Simulator", xaxis_title="Date", yaxis_title="Price ($)")

    return metrics, fig

if __name__ == "__main__":
    app.run(debug=True)