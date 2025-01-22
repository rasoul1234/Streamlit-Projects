# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:31:31 2023

@author: MohammadRasoulSahibz
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Inserting Title 
st.title('NBA Player Stats Explorer')

st.markdown("""
            This app performs simple webscraping of NBA player Stats data!
            * **Python LIbraries:** Base64, pandas, streamlit
           *  **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
            """)
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year **?**', list(reversed(range(1950, 2020))))

# Web scarping of NBA player stats
@st.cache_data
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis = 1)
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# sidebar - Position selection
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos) 

#Filtering data
df_slected_team = playerstats[(playerstats.Tm.isin(selected_team)) & playerstats.Pos.isin(selected_pos)]  

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimenstion:' + str(df_slected_team.shape[0]) + 'rows and ' + str(df_slected_team.shape[1]) + 'columns' )
st.dataframe(df_slected_team)

# Download NA player stats data
# https://discuss.streamlit.io/t/how-todownload-file-in-streamlit/1906
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href= "data:file/csv;base64,{b64}" download="playerstats.csv">download CSV File</a>'
    return href

st.markdown(filedownload(df_slected_team), unsafe_allow_html =True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_slected_teamto_csv('output.csv', index=False)
    df = pd.read_csv(ouput.csv)
    
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_form(mask)] = True
    with sns.axes_style('white'):
        f, ax = plt.subplots(figsize = (7, 5))
        ax = sns.heatmap(corr, mask = mask, vmax=1, square=True)