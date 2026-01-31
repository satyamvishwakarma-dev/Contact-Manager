# 📞 Contact Manager App

A clean, efficient Contact Management System built with **Python** and **Streamlit**. This application allows users to securely log in, add new contacts, view them in an interactive table, and edit or delete records directly from the UI. Data is persisted locally using CSV files.

## 🚀 Features

* **🔐 Secure Authentication:** Simple login system to protect your data.
* **➕ Add Contacts:** distinct form with validation (ensures phone numbers are digits).
* **👀 View Data:** Interactive table with per-row "Delete" functionality.
* **✏️ Edit Data:** Excel-like editor to modify records, add new rows, or delete them in bulk.
* **💾 Data Safety:** * Validation to prevent saving empty names.
    * "Download Backup" button to save a copy of your CSV before editing.
    * Permanent change warnings.
* **🎨 Modern UI:** Custom sidebar with a dynamic profile card, sticky footer, and wide-layout support.

## 🛠️ Tech Stack

* **Python** (Core Logic)
* **Streamlit** (Frontend UI & Navigation)
* **Pandas** (Data Manipulation & CSV Handling)

## 📂 Project Structure

```text
├── app.py              # Main entry point (Login & Navigation logic)
├── commands.py         # Helper module for authentication
├── add_data.py         # Page: Form to add new contacts
├── view_data.py        # Page: Read & Delete contacts
├── edit_data.py        # Page: Excel-style editor with Backup
├── main.py             # Page: Dashboard landing page
├── contacts.csv        # Database file (Auto-generated)
└── requirements.txt    # Python dependencies
```

## ⚙️ Installation & Setup
* Clone the repository:
git clone [https://github.com/satyamvishwakarma-dev/Contact-Manager.git](https://github.com/satyamvishwakarma-dev/Contact-Manager.git)
* cd contact-manager
* Install dependencies:
pip install -r requirements.txt
* Run the App:
* streamlit run app.py

## 📸 Usage Guide
* Login: Enter your credentials (configured in commands.py) to access the dashboard.
* Add Data: Navigate to "Add Data" and fill in the contact details.
* Manage: Use "View Data" for quick lookups or deletions. Use "Edit Data" for bulk changes.
* Backup: Always click "Download Backup" in the Edit tab before making major changes!

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 👤 Author
* Satyam Vishwakarma
* GitHub: [satyamvishwakarma-dev](https://github.com/satyamvishwakarma-dev)
* LinkedIn: [Satyam Vishwakarma](https://www.linkedin.com/in/satyamvishwakarma-cse/)