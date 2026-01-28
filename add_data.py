import streamlit as st
import time
import csv

st.title("Add Data", text_alignment = "center")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Name:", placeholder = "Enter contact name")
    number = st.text_input("Number:", placeholder = "Enter contact number")
    email = st.text_input("Email:", placeholder = "Enter contact email")
    address = st.text_area("Address:", placeholder = "Enter contact address")
    
    submitted = st.form_submit_button("Add")

    if submitted:
        # Data processing happens here
        if not number.isdigit():
            st.error("Error: Phone number must contain digits only.")
        else:
            new_row_data = [name, number, email, address]

            # Open the file in append mode ('a') with newline=''
            with open('contacts.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_row_data)

            st.toast(f"{name} added successfully!", icon = "✅", duration = 1)
            success_placeholder = st.empty()
            success_placeholder.success("Contact added successfully")
            time.sleep(1)
            success_placeholder.empty()
            name = number = email = address = ""
