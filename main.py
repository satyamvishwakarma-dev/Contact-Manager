import streamlit as st

st.title(f"Welcome, {st.session_state.username}!", text_alignment="center")
st.write("You are now logged in")
st.write("Select an option from the sidebar to continue")