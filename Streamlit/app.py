import pandas as pd
import streamlit as st
import numpy as np

# Title Of The Web Page

st.title("Hello World")

# Create a simple Data frame

df = pd.DataFrame({
    'first_col': [1,2,3,4],
    'second_col': [10,20,30,40]
})

## Display the Data Frame

st.write("Here is Our Data Frame")
st.write(df)

## Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
st.line_chart(df)