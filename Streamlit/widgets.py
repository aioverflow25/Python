import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("ENter your name")

age = st.slider("Select your age:",0,100,25) # 25 is default value 0 is min 100 is max
choice = st.selectbox("Choose your favorite language",["Python","C++","Java","R"])
if choice:
    st.write(f"Your favorite language is {choice}")
st.write(f"Your age is {age}")

if name:
    st.write(f"Hello {name}")

# Uploader

df = pd.DataFrame({
    "Name": ["Raman","Akash","Anshuman"],
    "Age": [28,27,25],
    "City": ['Bareilly','Lucknow','Tiri']
})
df.to_csv("Samples.csv")

uploaded_files = st.file_uploader("Choose a csv file",type='csv')

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)