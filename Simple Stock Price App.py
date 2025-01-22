#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")
# Get data on this ticker
tickerSymbol = 'GOOGL'
# Get the historical prices for this ticker
ticherData = yf.Ticker(tickerSymbol)
ticherDF = ticherData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High  Low Close  Volume  Dividends  Stock Splits

st.line_chart(ticherDF.Close)
st.line_chart(ticherDF.Volume)
