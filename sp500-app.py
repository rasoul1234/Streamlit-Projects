# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:20:59 2023

@author: MohammadRasoulSahibz
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
# We use base64 for encoding and decoding 
import base64

st.title('S&P 500 App')
st.markdown("""
            This app retrives the list of the **S&P 500** (from Vikipedia) and its the corresponding **stock closing price** (year-to-date!)
            * **Python libraries:** base64, pandas, streamlit, matplotlib, seaborn, yfinance
            * **Data source:** [Wikipedia.](https://www.wikipedia.org/) 
            * **Developer:** Muhammad Rasoul Sahibzadah
            """)
            

st.sidebar.header('User Input Features')

# Web Scraping of S&P 500 data

# In the new version of streamlit, we must use st.cach_resouce
@st.cache_resource
# This is used for webscripting 
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    # I have used 0 because in this website there are two tables, and I want to select the first one.
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - sectore selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('**Sector:**', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

st.header('Display Companies in Selected Sectore')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)


# Download S&P500 Data
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download = "SP500.csv">Download CSV File </a>'
    return href
st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)


# Download S&P500 data
data = yf.download(
    tickers=list(df_selected_sector[:10].Symbol),
    period= "ytd",
    interval= "1d",
    group_by= 'ticker',
    auto_adjust= True,
    prepost= True,
    proxy= None
    )

# Plot Closing Price of Query Symbol
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    plt.fill_between(df.Date, df.Close, color='skyblue', alpha = 0.3)
    plt.plot(df.Date, df.Close, color = 'skyblue', alpha = 0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight = 'bold')
    plt.ylabel('Closing Price', fontweight = 'bold')
    return st.pyplot()

num_company = st.sidebar.slider('Number of Companies', 1, 5)
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)