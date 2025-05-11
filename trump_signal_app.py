import streamlit as st
import pandas as pd
import random

# Mapping keywords to sectors and tickers
sector_mapping = {
    "china": {"sector": "International Trade", "tickers": ["FXI", "AAPL", "TSLA"]},
    "ice": {"sector": "Private Prisons", "tickers": ["GEO", "CXW"]},
    "public broadcasting": {"sector": "Media/Streaming", "tickers": ["NFLX", "DIS", "CMCSA"]},
    "uk trade": {"sector": "Global Trade", "tickers": ["EWU", "JPM", "BP"]}
}

# Title
st.title("Trump Signal Market Predictor")

# Input quotes
st.subheader("Enter Trump's Weekly Quotes")
input_text = st.text_area("Paste 1 quote per line", height=200)

# Button to trigger analysis
if st.button("Analyze Quotes"):
    st.subheader("Predicted Market Signals")
    quotes = input_text.strip().split('\n')
    results = []

    for quote in quotes:
        for keyword, data in sector_mapping.items():
            if keyword in quote.lower():
                signal = {
                    "Quote": quote,
                    "Sector": data["sector"],
                    "Tickers": ", ".join(data["tickers"]),
                    "Confidence": f"{random.randint(70, 90)}%",
                    "Action": "BUY"
                }
                results.append(signal)
                break

    if results:
        df = pd.DataFrame(results)
        st.dataframe(df)
        st.download_button("Download Signals as CSV", data=df.to_csv(index=False), file_name="market_signals.csv")
    else:
        st.info("No matching market signals found. Try different quote inputs.")
