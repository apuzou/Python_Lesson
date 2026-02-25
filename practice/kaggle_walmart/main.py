import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline

st.title('Walmart Sales Prediction')

features = pd.read_csv('practice/Kaggle_Walmart/features.csv')
stores = pd.read_csv('practice/Kaggle_Walmart/stores.csv')
df_test = pd.read_csv('practice/Kaggle_Walmart/test.csv')
df_train = pd.read_csv('practice/Kaggle_Walmart/train.csv')
submit = pd.read_csv('practice/Kaggle_Walmart/sampleSubmission.csv')

st.write(features.head())
st.write(stores.head())
st.write(df_test.head())
st.write(df_train.head())
st.write(submit.head())

"""
###学習データ
- 店舗データに関しては1~45の45店舗分
- カテゴリデータに関しては1〜99の81カテゴリ分
- 2012-02-05~2012-10-26の143週分
"""
"""
###テストデータ
- 2012-11-02~2013-07-26の39週分
"""

# Store 1
plt.figure(figsize=(30, 6))
sns.countplot(x='Dept', data=df_train[df_train['Store'] == 1])
plt.show()
st.pyplot(plt)

# Store 32
plt.figure(figsize=(30, 6))
sns.countplot(x='Dept', data=df_train[df_train['Store'] == 32])
plt.show()
st.pyplot(plt)

# Dept 1
plt.figure(figsize=(30, 6))
sns.countplot(x='Store', data=df_train[df_train['Dept'] == 1])
plt.show()
st.pyplot(plt)

# Dept 45
plt.figure(figsize=(30, 6))
sns.countplot(x='Store', data=df_train[df_train['Dept'] == 45])
plt.show()
st.pyplot(plt)

"""
カテゴリ45の各店舗の各日付の売上をヒートマップで表示し、売上の推移を見る
"""
plt.figure(figsize=(30, 6))
sns.heatmap(pd.pivot_table(df_train[df_train['Dept'] == 45], index='Store', columns='Date', values='Weekly_Sales'))
plt.title('Dept 45_Sales_Heatmap')
plt.show()
st.pyplot(plt)

"""
カテゴリごとの週間売上平均を棒グラフで表示
"""
plt.figure(figsize=(30, 6))
sns.barplot(x='Dept', y='Weekly_Sales', data=df_train)
plt.title('Dept_Sales_Average')
plt.show()
st.pyplot(plt)

"""
練習:店舗特性と売上の相関関係を分析する
"""
"""
Storeごとの週間売上平均を棒グラフで表示
"""
plt.figure(figsize=(30, 6))
sns.barplot(x='Store', y='Weekly_Sales', data=df_train)
plt.title('Store_Sales_Average')
plt.show()
st.pyplot(plt)

"""
店舗のストアタイプごとの週間売上平均を棒グラフで表示
"""
plt.figure(figsize=(30, 6))
df_tmp = pd.merge(df_train.groupby('Store').sum()[['Weekly_Sales']].reset_index(), stores)
sns.barplot(x='Type', y='Weekly_Sales', data=df_tmp)
plt.title('Store_Type_Sales_Average')
plt.show()
st.pyplot(plt)

"""
店舗のサイズと売上の相関関係を散布図で表示
"""
sns.jointplot(x='Size', y='Weekly_Sales', data=df_tmp)
plt.title('Store_Size_Sales_Correlation')
plt.show()
st.pyplot(plt)

"""
店舗のサイズと売上の相関関係を相関係数で表示
"""
st.write(df_tmp.select_dtypes(include=[np.number]).corr())

"""
結論：店舗のサイズが大きいほど売上が高い相関関係があることがわかった
"""

st.write('\n')

"""
練習:売上の推移をグラフなどで可視化して、最も売上が高くなる日付を探す
"""
"""
売上の推移を線グラフで表示
"""
plt.figure(figsize=(30, 6))
df_tmp = df_train.groupby('Date').sum().reset_index()
sns.lineplot(x='Date', y='Weekly_Sales', data=df_tmp)
plt.title('Weekly_Sales_Trend')
plt.show()
st.pyplot(plt)

"""
売上が高い日付の上位10件を表示
"""
plt.figure(figsize=(30, 6))
top10_date = df_train.groupby('Date').sum().reset_index()
top10_date = top10_date.sort_values('Weekly_Sales', ascending=False).head(10)
st.write(top10_date)

"""
店舗ごとの売上の推移を見て、類似性を探す
"""
plt.figure(figsize=(30, 6))
df_tmp = df_train.groupby(['Date', 'Store']).sum().reset_index()
sns.lineplot(x='Date', y='Weekly_Sales', data=df_tmp[df_tmp['Store'] == 1])
sns.lineplot(x='Date', y='Weekly_Sales', data=df_tmp[df_tmp['Store'] == 20])
sns.lineplot(x='Date', y='Weekly_Sales', data=df_tmp[df_tmp['Store'] == 40])
plt.title('Stores_Weekly_Sales_Trend')
plt.show()
st.pyplot(plt)

"""
結論：年末に向かって月末の売上が高くなることがわかった
"""