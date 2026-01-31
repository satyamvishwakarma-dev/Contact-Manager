import streamlit as st

st.set_page_config(
    page_title="Contact Manager",
    layout="wide",                  # Options: "centered" (default) or "wide"
    initial_sidebar_state="expanded" # Options: "auto", "expanded", "collapsed"
)
st.title(f"Welcome, Mr. {st.session_state.username}!", text_alignment="center")
# st.toast('Select an option from the sidebar to continue', icon='ℹ️', duration = 5)
st.toast('You are now logged in', icon='✅', duration = 1)
st.markdown("---")
st.header("Instructions:")
st.text("1. Select an option from the sidebar to continue.")
st.text("2. You can add, view, and edit contacts.")
st.text("3. You can delete contacts in view data page.")
st.text("4. You can log out from the sidebar.")
