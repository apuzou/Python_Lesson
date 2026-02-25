import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline

import lightgbm as lgb

st.title('Machine Learning Model')

features = pd.read_csv('practice/features.csv')
stores = pd.read_csv('practice/stores.csv')
df_test = pd.read_csv('practice/test.csv')
df_train = pd.read_csv('practice/train.csv')
submit = pd.read_csv('practice/sampleSubmission.csv')

plt.figure(figsize=(30, 6))
df_tmp = pd.merge(df_train.groupby('Store').sum()[['Weekly_Sales']].reset_index(), stores)

plt.figure(figsize=(30, 6))
df_tmp = df_train.groupby('Date').sum().reset_index()

plt.figure(figsize=(30, 6))
top10_date = df_train.groupby('Date').sum().reset_index()
top10_date = top10_date.sort_values('Weekly_Sales', ascending=False).head(10)

plt.figure(figsize=(30, 6))
df_tmp = df_train.groupby(['Date', 'Store']).sum().reset_index()

plt.figure(figsize=(30, 6))
df = pd.merge(pd.merge(df_train, stores), features)

def term_class(x):
    """日付を上旬(1-10日)、中旬(11-20日)、下旬(21日-)に分類する。"""
    day_str = x[8:10]
    day = int(day_str)
    if day <= 10:
        term = 1
    elif day <= 20:
        term = 2
    else:
        term = 3
    return term

def preprocess(df):
    df['Month'] = df['Date'].apply(lambda x:x[5:7])

    df["Term"] = df["Date"].apply(term_class)

    for col in ['Store', 'Dept', 'Type', 'Month', 'Term']:
        df[col] = df[col].astype('category')

    return df

df = preprocess(df)

df_val = df[df['Date'] >= '2012-07-13']
df_tr = df[df['Date'] < '2012-07-13']

df_val_x = df_val.drop(['Weekly_Sales', 'Date'], axis=1)
df_tr_x = df_tr.drop(['Weekly_Sales', 'Date'], axis=1)

df_val_y = df_val['Weekly_Sales']
df_tr_y = df_tr['Weekly_Sales']

trains = lgb.Dataset(df_tr_x, df_tr_y)
valids = lgb.Dataset(df_val_x, df_val_y)

params = {
    'objective': 'regression',
    'metric': 'mae',
}

model = lgb.train(params, trains, valid_sets=valids, num_boost_round=1000, callbacks=[lgb.early_stopping(stopping_rounds=100)])

df_te = pd.merge(pd.merge(df_test, stores), features)
df_te = preprocess(df_te)
preds = model.predict(df_te.drop('Date', axis=1))
df_te = pd.concat([df_te, pd.DataFrame(preds)], axis=1).rename(columns={0: 'Weekly_Sales'})

submit['Weekly_Sales'] = df_te.sort_values(['Store', 'Dept', 'Date'])['Weekly_Sales']
submit.to_csv('practice/submit.csv', index=False)