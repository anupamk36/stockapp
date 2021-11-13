import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App.

Shown are the stock **closing price** and ***volume*** of Google!
""")
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',start='2010-5-13',end='2020-5-13')
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)


# to run this application
# type "streamlit run 'file_directory'/myapp.py"