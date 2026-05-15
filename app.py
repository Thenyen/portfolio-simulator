from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objects as go
from data.fetch import fetch_data, fetch_benchmark
from data.strategy import buy_and_hold, moving_average, sharpe_ratio, max_drawdown, cagr, monte_carlo
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Portfolio Simulator"),
    html.Div([
        dcc.Dropdown(
            id="ticker-dropdown",
options=[
    # US Tech
    {"label": "Apple (AAPL)", "value": "AAPL"},
    {"label": "Microsoft (MSFT)", "value": "MSFT"},
    {"label": "Amazon (AMZN)", "value": "AMZN"},
    {"label": "Google (GOOGL)", "value": "GOOGL"},
    {"label": "Meta (META)", "value": "META"},
    {"label": "NVIDIA (NVDA)", "value": "NVDA"},
    {"label": "Tesla (TSLA)", "value": "TSLA"},
    # German DAX
    {"label": "SAP (SAP.DE)", "value": "SAP.DE"},
    {"label": "Siemens (SIE.DE)", "value": "SIE.DE"},
    {"label": "Volkswagen (VOW3.DE)", "value": "VOW3.DE"},
    {"label": "Allianz (ALV.DE)", "value": "ALV.DE"},
    {"label": "Deutsche Bank (DBK.DE)", "value": "DBK.DE"},
    {"label": "BMW (BMW.DE)", "value": "BMW.DE"},
    # Indices
    {"label": "S&P 500 ETF (SPY)", "value": "SPY"},
    {"label": "NASDAQ ETF (QQQ)", "value": "QQQ"},
    {"label": "DAX ETF (EXS1.DE)", "value": "EXS1.DE"},
],
            value="AAPL",
            style={"width": "300px"}
        ),
        dcc.Dropdown(
            id="start-year",
            options=[{"label": str(y), "value": str(y)} for y in range(2015, 2024)],
            value="2020",
            style={"width": "120px"}
        ),
        dcc.Dropdown(
            id="end-year",
            options=[{"label": str(y), "value": str(y)} for y in range(2016, 2025)],
            value="2024",
            style={"width": "120px"}
        ),
    ], style={"display": "flex", "gap": "20px", "margin": "20px 0", "align-items": "center"}),
    html.Div(id="metrics", style={"display": "flex", "gap": "20px", "margin": "20px 0"}),
    dcc.Graph(id="price-chart"),
    html.H2("Monte Carlo Simulation (1 Year Forecast)"),
    dcc.Graph(id="monte-carlo-chart")
])

@callback(
    Output("metrics", "children"),
    Output("price-chart", "figure"),
    Input("ticker-dropdown", "value"),
    Input("start-year", "value"),
    Input("end-year", "value")
)
def update_dashboard(ticker, start_year, end_year):
    start = f"{start_year}-01-01"
    end = f"{end_year}-01-01"

    df = fetch_data(ticker, start, end)
    prices = df.squeeze().astype(float)
    benchmark = fetch_benchmark(start, end)
    prices_normalized = prices / prices.iloc[0] * 100

    bah = buy_and_hold(df)
    ma = moving_average(df)
    sharpe = sharpe_ratio(df)
    dd = max_drawdown(df)
    cagr_result = cagr(df, start, end)

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
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"}),
        html.Div([
            html.H3("CAGR"),
            html.P(f"Annual: {cagr_result['cagr']} %")
        ], style={"border": "1px solid #ccc", "padding": "20px", "width": "200px"})
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices_normalized.index, y=prices_normalized.values, name=f"{ticker}"))
    fig.add_trace(go.Scatter(x=benchmark.index, y=benchmark.values, name="S&P 500", line=dict(dash="dash", color="gray")))
    fig.add_trace(go.Scatter(x=prices_normalized.index, y=prices_normalized.rolling(50).mean(), name="50-Tage MA", visible="legendonly"))
    fig.add_trace(go.Scatter(x=prices_normalized.index, y=prices_normalized.rolling(200).mean(), name="200-Tage MA", visible="legendonly"))
    fig.update_layout(title=f"{ticker} vs S&P 500 (normalized to 100)", xaxis_title="Date", yaxis_title="Value (normalized)")

    return metrics, fig


@callback(
    Output("monte-carlo-chart", "figure"),
    Input("ticker-dropdown", "value"),
    Input("start-year", "value"),
    Input("end-year", "value")
)
def update_monte_carlo(ticker, start_year, end_year):
    start = f"{start_year}-01-01"
    end = f"{end_year}-01-01"

    df = fetch_data(ticker, start, end)
    paths, last_price = monte_carlo(df)

    fig = go.Figure()
    for path in paths:
        fig.add_trace(go.Scatter(
            y=path,
            mode="lines",
            line=dict(width=0.5, color="blue"),
            opacity=0.1,
            showlegend=False
        ))

    fig.add_hline(y=last_price, line_dash="dash", line_color="red", annotation_text="Current Price")
    fig.update_layout(
        title=f"{ticker} — Monte Carlo Simulation (200 paths, 1 year)",
        xaxis_title="Days",
        yaxis_title="Price ($)"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)