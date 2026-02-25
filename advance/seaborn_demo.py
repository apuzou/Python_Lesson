import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()

st.title('Seaborn Demo')

df = sns.load_dataset('titanic')

st.write(df.head())

# sns.displot(df['age'])
# plt.show()
# st.pyplot(plt)

# sns.countplot(x='pclass', data=df)
# plt.show()
# st.pyplot(plt)

# sns.catplot(x='pclass', data=df, kind='count')
# plt.show()
# st.pyplot(plt)

# sns.barplot(x='survived', y='age', hue='sex', data=df)
# plt.show()
# st.pyplot(plt)

# sns.boxplot(x='survived', y='age', hue='sex', data=df)
# plt.show()
# st.pyplot(plt)

# sns.violinplot(x='survived', y='age', hue='sex', data=df)
# plt.show()
# st.pyplot(plt)

# sns.jointplot(x='age', y='fare', data=df)
# plt.show()
# st.pyplot(plt)

# df = sns.load_dataset('iris')

# sns.pairplot(df)
# plt.show()
# st.pyplot(plt)

