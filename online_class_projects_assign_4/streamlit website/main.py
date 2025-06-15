import streamlit as st

st.set_page_config(page_title="First Streamlite Website", page_icon="🌍", layout="centered")
st.title("Welcome to my first python website.")

st.sidebar.title("Navigation")
page= st.sidebar.radio("GO to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home Page")
    st.write("This is a simple home page built with python and streamlit ")
    name = st.text_input("What\'s your name? ")
    if name:
        st.success(f'Hallo {name}! Thank you for Visiting. ')

elif page == "About":
    st.header("About")
    st.write("This Website is built entirely using python and streamlit in under 15 minutes!")

elif page == "Contact":
    st.header("Contact Us")
    email = st.text_input("Your email ")
    message = st.text_input("your Message ")
    if st.button("Submit"):
        st.success("Thank you! we have received your message.")