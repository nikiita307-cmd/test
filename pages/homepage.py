import streamlit as st
import pandas as pd

def homepage():
    st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>Product Quality Review Platform</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#306998;'>Submit and track product complaints and view analytics.</p>", unsafe_allow_html=True)

    submissions = st.session_state.get("submissions", [])
    df = pd.DataFrame(submissions)

    left, right = st.columns([3, 1])

    with left:
        st.subheader("Trending Products")
        if df.empty:
            st.info("No submissions yet — please submit a review or complaint.")
        else:
            top = df["product_name"].value_counts().reset_index()
            top.columns = ["Product Name", "Count"]
            st.table(top.head(10))

        st.subheader("Most Common Complaints")
        if not df.empty and "complaint_text" in df.columns:
            complaints = df["complaint_text"].value_counts().head(20)
            st.table(complaints)

    with right:
        st.subheader("Quick Stats")
        st.metric("Total Submissions", len(submissions))
