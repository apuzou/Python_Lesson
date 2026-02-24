import pandas as pd
import seaborn as sns

import streamlit as st

df = sns.load_dataset('titanic')

st.title('Titanic Dataset')

st.dataframe(df)

st.write(df.head())

st.write(df.shape)

st.write(df.info())

st.write(df.columns)

st.write(df['pclass'])
st.write(df['pclass'].unique())

st.write(df.iloc[0:3])

st.write(df.describe())

st.write(df.select_dtypes(include=['number']).groupby(df['survived']).mean()['age'])

st.write(df.sort_values(by='age', ascending=False))

df = df.reset_index()

df_a = df[["index", "survived"]]
df_b = df[["index", "pclass"]]

df_merged = pd.merge(df_a, df_b, on="index", how="inner")

st.write(df_merged)

df_concat = pd.concat([df_a, df_b], axis=0)

st.write(df_concat)

df_sample = pd.read_csv('advance/sample.csv')

st.write(df_sample)

new_column = pd.Series(["man", "woman"])

df_sample['gender'] = new_column
df_sample.to_csv('advance/df_sample2.csv')

df_sample2 = pd.read_csv('advance/df_sample2.csv')

st.write(df_sample2)
