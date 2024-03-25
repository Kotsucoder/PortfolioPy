import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/kotsu.jpg")

with col2:
    st.title("Marcus Kotsu「骨マルカス」")
    content = """
    二十四才。アメリカ人。Amateur Programmer. WaniKani Level 2. Lion. DoorDasher.
    """
    st.info(content)

introText = """
Below you can find some of the apps I have built in Python. These were created 
while following the Python Mega Course on Udemy.
"""
st.write(introText)

col3, col4 = st.columns(2)


data = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])