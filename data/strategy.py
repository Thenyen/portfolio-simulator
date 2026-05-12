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