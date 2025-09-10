import streamlit as st
from pages.homepage import homepage
from pages.submit_review import submit_review
from pages.complaint_tracker import complaint_tracker
from pages.vendor_dashboard import vendor_dashboard
from pages.analytics_dashboard import analytics_dashboard

# Streamlit page config
st.set_page_config(page_title="Product Quality Review Platform", layout="wide")

# ------------------------------
# Initialize session_state with dummy data
# ------------------------------
if "submissions" not in st.session_state:
    st.session_state["submissions"] = [
        {"product_name": "Soap", "vendor": "Dove", "fssai_code": "FSSAI12345", "rating": 4, "complaint_text": "Skin irritation", "file_name": None, "status": "Resolved"},
        {"product_name": "Toothpaste", "vendor": "Colgate", "fssai_code": "FSSAI54321", "rating": 5, "complaint_text": "No complaints", "file_name": None, "status": "Resolved"},
        {"product_name": "Shampoo", "vendor": "Pantene", "fssai_code": None, "rating": 3, "complaint_text": "Hair fall issue", "file_name": None, "status": "Pending"},
        {"product_name": "Soap", "vendor": "Lifebuoy", "fssai_code": "FSSAI11223", "rating": 2, "complaint_text": "Redness and itching", "file_name": None, "status": "Pending"},
        {"product_name": "Facewash", "vendor": "Nivea", "fssai_code": "FSSAI99887", "rating": 5, "complaint_text": "Very satisfied", "file_name": None, "status": "Resolved"},
        {"product_name": "Shampoo", "vendor": "Head & Shoulders", "fssai_code": None, "rating": 3, "complaint_text": "Dandruff not reduced", "file_name": None, "status": "Resolved"},
    ]

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Select Page", [
    "Homepage",
    "Submit Review/Complaint",
    "Complaint Tracker",
    "Vendor Dashboard",
    "Analytics Dashboard"
])

# ------------------------------
# Render selected page
# ------------------------------
if selection == "Homepage":
    homepage()
elif selection == "Submit Review/Complaint":
    submit_review()
elif selection == "Complaint Tracker":
    complaint_tracker()
elif selection == "Vendor Dashboard":
    vendor_dashboard()
elif selection == "Analytics Dashboard":
    analytics_dashboard()
