# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:50:11 2023

@author: MohammadRasoulSahibz
"""

import streamlit as st
import pandas as pd


df = pd.read_csv('C:/Users/MohammadRasoulSahibz/Desktop/penguins_cleaned.csv')

target = 'species'
encode = ['sex', 'island']

# encode my sex and island columns
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

# encod my target column
target_mapper = {'Adelie' : 0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# Seperating X and y
X = df.drop('species', axis = 1)
y = df['species']

# I would like to use random forest for this model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X,y)

# I would like to save my model
import pickle 
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))


