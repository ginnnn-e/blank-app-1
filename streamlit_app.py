import streamlit as st

st.title("🎈 My first Streamlit app")
st.write(
    "hello streamlit world!"
)
name = st.text_input('Enter your name')
if name:
    st.write(f'Hello, {name}')

button = st.button("Click me")
if button:
    st.write(f"You're amazing!")
else:
    st.write("waiting to be clicked")

st.checkbox("Check me")


# URL
# http://localhost:8501
# https://urban-orbit-pjr647grr5q736x4g-8501.app.github.dev/
