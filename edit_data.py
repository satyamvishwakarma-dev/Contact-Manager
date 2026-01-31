import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(
    page_title="Contact Manager",
    layout="wide",                  # Options: "centered" (default) or "wide"
    initial_sidebar_state="expanded" # Options: "auto", "expanded", "collapsed"
)

st.title("Edit Data", text_alignment = "center")

FILE_PATH = "contacts.csv"

if os.path.exists(FILE_PATH):
    st.warning("**Be Careful:** Changes are **PERMANENT**. Download a backup below if you are unsure.", icon="⚠️")

    st.header("Instructions:")
    st.text("1. Double click on the cell to edit the data in the table.\n2. Click the 'Save Changes' button to save the data." + 
    "\n3. For adding data visit Add Data page.")
    st.markdown("---")

    df = pd.read_csv(FILE_PATH)

    edited_df = st.data_editor(
        df, 
        num_rows="dynamic", 
        use_container_width=True, 
        key="editor"
    )

    # Create two columns for the buttons so they sit side-by-side
    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("Save Changes", type="primary"):
            if edited_df["Name"].replace('', pd.NA).isna().any():
                st.toast("Error: Name cannot be empty!", icon="🚫")
            else:
                try:
                    edited_df.to_csv(FILE_PATH, index=False)
                    st.toast("✅ Saved successfully!", icon="💾")
                    time.sleep(1.5)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error saving file: {e}")

    with col2:
        # Convert the current DataFrame to CSV for downloading
        csv = df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Download Backup",
            data=csv,
            file_name="contacts_backup.csv",
            mime="text/csv",
            help="Click this to save a copy of the current list before editing."
        )

else:
    st.info("No data found. Please add data first.")