import streamlit as st
import numpy as np
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# chart_data=pd.DataFrame(
#     np.random.randn(10,20),columns=['a','b','c']
# )
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.write(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)

