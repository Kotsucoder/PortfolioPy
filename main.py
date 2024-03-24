import streamlit as st

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