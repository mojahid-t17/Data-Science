import streamlit as st
import numpy as np
import pandas as pd
# Add a slider
x=st.slider('x')
st.write(x ,"square",x*x)

age=st.slider('enter your age',10,100,25)
st.write('your age is',age)

# Add user input
name=st.text_input('enter your name')
if st.button('submit'):
    st.write('welcome',name)
    
    
#checkbox to display something
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    chart_data


st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "About"])

if choice == "Home":
    st.write("Welcome to the Home Page!")
else:
    st.write("This is the About Page")

st.form('student form')

option = st.selectbox("Choose one:", ["Python", "Java", "C++"])
st.write("You selected:", option)
df=''
#file uploader

file=st.file_uploader('upload a csv file',type='csv')
if file is not None:
    df=pd.read_csv(file)

st.write(df)