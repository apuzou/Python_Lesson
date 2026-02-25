import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Matplotlib Demo')

df = sns.load_dataset('titanic')

st.write(df.head())

# plt.hist(df['fare'], bins=40, range=(0, 100))
# plt.show()
# st.pyplot()

# plt.figure(figsize=(20, 10))
# plt.plot(df['fare'])
# plt.title('titanic data')
# plt.xlabel('data_index')
# plt.ylabel('fare')
# plt.show()
# st.pyplot(plt)

# df['fare'].hist(by=df['sex'])
# plt.show()
# st.pyplot(plt)

# # 複数のグラフを表示
# fig, axes = plt.subplots(2, 2, figsize=(20, 10))
# axes[0][0].hist(df['age'], bins=20)
# axes[0][1].hist(df['fare'], bins=20)
# axes[1][0].hist(df['sex'], bins=20)
# axes[1][1].hist(df['pclass'], bins=20)
# plt.show()
# st.pyplot(plt)

# plt.bar(df.groupby('pclass').count()['survived'].index, df.groupby('pclass').count()['survived'].values)
# plt.title('Survival by Pclass')
# plt.xlabel('Pclass')
# plt.ylabel('Count')
# plt.show()
# st.pyplot(plt)

# plt.scatter(df['fare'], df['age'], alpha=0.5)
# plt.show()
# st.pyplot(plt)