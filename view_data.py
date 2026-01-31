import streamlit as st
import pandas as pd
import os

st.title("View Data", text_alignment = "center")

# File path
FILE_PATH = "contacts.csv"

if os.path.exists(FILE_PATH):
    col_ratios = [1.5, 1.5, 4, 5, 1.5]
    # Read the CSV
    df = pd.read_csv(FILE_PATH)
    
    # Check if the dataframe is empty
    if df.empty:
        st.info("No data found. Go to 'Add Data' to create some entries.")
    else:
        # Display headers (optional, for clarity)
        cols = st.columns(col_ratios) # The last column is for the Delete button
        headers = ["Name", "Number", "Email", "Address", "Action"]
        for col, header in zip(cols, headers):
            col.markdown(f"**{header}**")

        st.markdown("---")
            
        # Iterate through the DataFrame to display rows
        # We use .iterrows() to get the index and row data
        for index, row in df.iterrows():
            cols = st.columns(col_ratios)
            
            # Display data in the first 4 columns
            cols[0].write(row['Name']) # Adjust 'Name' if your CSV header is different
            cols[1].write(str(row['Number']))
            cols[2].write(row['Email'])
            cols[3].write(row['Address'])
            
            # Add a Delete button in the 5th column
            # We use a unique key for each button using the index
            if cols[4].button("Delete", key=f"delete_{index}", use_container_width=True):
                # 1. Drop the row from the dataframe
                df = df.drop(index)
                
                # 2. Save the updated dataframe back to the CSV
                # index=False prevents pandas from adding a new numbering column
                df.to_csv(FILE_PATH, index=False)
                
                # 3. Show success message and rerun to update the list
                st.toast(f"Deleted {row['Name']}!", icon="🗑️")
                st.rerun()

            st.divider()

else:
    st.info("No data found. Go to 'Add Data' to create some entries.")