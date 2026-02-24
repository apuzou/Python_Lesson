import numpy as np
import streamlit as st

st.title('Numpy Demo')

# numpy array
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

st.write(a + b)
st.write(a * 2)

# list
a = [1, 2, 3]
b = [10, 20, 30]

st.write(a + b)
st.write(a * 2)

arr = np.array([1, 2, 3, 4, 5])
st.write(arr.sum()) # 合計
st.write(arr.mean()) # 平均
st.write(arr.std()) # 標準偏差
st.write(arr.var()) # 分散
st.write(arr.max()) # 最大値
st.write(arr.min()) # 最小値
st.write(np.median(arr)) # 中央値

# 多次元配列
A = np.array([[1, 2, 3], [4, 5, 6]])
st.write(A)

st.write(A.shape)

# example
scores = np.array([[80, 60, 100], [80, 60, 90], [60, 50, 40]])

mean = np.mean(scores, axis=0)
mean_floor = np.floor(mean) # 平均点を切り捨て
st.write(mean_floor)
st.write(f"平均点との差: {scores - mean_floor}")

# 配列の作成
st.write(np.random.rand(3, 2))
st.write(np.zeros((3, 2)))
st.write(np.arange(0, 101, 2))