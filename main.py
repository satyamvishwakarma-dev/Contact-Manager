import streamlit as st

st.title(f"Welcome, Mr. {st.session_state.username}!", text_alignment="center")
st.toast('Select an option from the sidebar to continue', icon='ℹ️', duration = 5)
st.toast('You are now logged in', icon='✅', duration = 1)