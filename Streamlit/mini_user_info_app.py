import streamlit as st
st.title("Mini User Info App")
name = st.text_input("Enter Your Name")
age = st.slider("Select age",0,100,10)
hobby = st.selectbox("Enter your hobby",['reading','watching_movies','playing_cricket'])
# Only show output when all inputs are filled
if name and hobby != '':
    st.write(f"Hello {name}! You are {age} years old and your hobby is {hobby}.")

    if age < 18:
        st.success("You are a minor! 😊")
    else:
        st.info("You are an adult! 🎉")
