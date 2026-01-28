import streamlit as st
import commands  # Assuming this is your local module

# 1. Initialize Session State
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# 2. Define the Login Page (Local function)
def login_page():
    st.title("Login", text_alignment = "center")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        if commands.login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in!")
            st.rerun()
        else:
            st.error("Incorrect username or password")

# 3. Define the Navigation Logic (The "Logged In" View)
def run_dashboard():
    # Define your pages here
    # Note: These files (main.py, view_data.py) must exist in your folder
    pages = [
        st.Page("main.py", title="Main Page"),
        st.Page("add_data.py", title="Add Data"),
        st.Page("view_data.py", title="View Data"),
        st.Page("edit_data.py", title="Edit Data")
    ]
    
    # Create the navigation object
    pg = st.navigation(pages)
    
    # Optional: Add a logout button in the sidebar
    with st.sidebar:
        st.write(f"User: {st.session_state.username}")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()

    # Run the selected page
    pg.run()

# 4. Traffic Control
if st.session_state.logged_in:
    run_dashboard()
else:
    login_page()