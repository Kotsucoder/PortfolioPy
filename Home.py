import streamlit as st
import pandas


def repo(name):
    return f"https://www.github.com/Kotsucoder/{name}"


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
while following the 
[Python Mega Course on Udemy](https://www.udemy.com/course/the-python-mega-course).
"""
st.write(introText)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


data = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({repo(row['url'])})")


with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({repo(row['url'])})")


st.header("Other works:")
st.write(f"[Company Website]({repo('pycompanysiteproject')})")
st.write(f"[Text to PDF]({repo('Text-to-PDF')})")