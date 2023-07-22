import pandas as pd
import streamlit as st
import yfinance as yf

stocks: dict[str, str] = {
    "google": "GOOGL",
    "apple": "AAPL",
    "amazon": "AMZN",
    "nvidia": "NVDA",
    "meta": "META",
    "netflix": "NFLX"
}
stock_name: str = "google"

# Sidebar
with st.sidebar:
    stock_name = st.selectbox("Select Stock", stocks.keys())
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    dataframe = st.checkbox("Display Data?")

# Main
st.title("Simple Stock Price App")

st.write(
    f"Shown are the stock closing price and volume of {stock_name.title()}!")


tickerSymbol = stocks.get(stock_name)
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="1d", start=start_date, end=end_date)

st.header("Closing Price")
st.caption(f"This is the line chart for closing price of {stock_name.title()}")
st.line_chart(tickerDf.Close)


st.header("Volume Price")
st.caption(f"This is the line chart for volume {stock_name.title()} stocks")
st.line_chart(tickerDf.Volume)

if dataframe:
    st.header("Data")
    df = tickerDf.loc[:, ["Close", "Volume"]]
    st.dataframe(df.style.highlight_max(
        color='green').highlight_min(color='red'),  use_container_width=True)
