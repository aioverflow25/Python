import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

@st.cache_data  # it is use to cache this data as every time we don't have to load the data 
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species'] = iris.target
    return df,iris.target_names

df,target_names = load_data()


model = RandomForestClassifier() # df.iloc[row_start:row_end, col_start:col_end]
model.fit(df.iloc[:,:-1],df['species']) 

st.sidebar.title("Input Features")

# Sidebar Sliders for each feature
sepal_length = st.sidebar.slider(
    "Sepal length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max()),
    float(df['sepal length (cm)'].mean())  # default = mean
)

sepal_width = st.sidebar.slider(
    "Sepal width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max()),
    float(df['sepal width (cm)'].mean())
)

petal_length = st.sidebar.slider(
    "Petal length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max()),
    float(df['petal length (cm)'].mean())
)

petal_width = st.sidebar.slider(
    "Petal width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max()),
    float(df['petal width (cm)'].mean())
)

# Combine all sidebar inputs into a dataframe
input_data = pd.DataFrame({
    'sepal length (cm)': [sepal_length],
    'sepal width (cm)': [sepal_width],
    'petal length (cm)': [petal_length],
    'petal width (cm)': [petal_width]
})

# prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")