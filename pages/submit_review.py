import streamlit as st

def submit_review():
    st.markdown("<h2 style='color:#4B8BBE;'>Submit a Review / Complaint</h2>", unsafe_allow_html=True)

    with st.form("review_form"):
        product_name = st.text_input("Product Name")
        vendor = st.text_input("Vendor / Brand")
        fssai_code = st.text_input("FSSAI License / Code (optional)")
        rating = st.slider("Rating (1-5)", 1, 5, 3)
        complaint_text = st.text_area("Complaint / Review")
        uploaded_file = st.file_uploader("Upload Image / Document", type=["png", "jpg", "jpeg", "pdf"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            new_entry = {
                "product_name": product_name,
                "vendor": vendor,
                "fssai_code": fssai_code if fssai_code else None,
                "rating": rating,
                "complaint_text": complaint_text,
                "file_name": uploaded_file.name if uploaded_file else None,
                "status": "Pending"
            }
            if "submissions" not in st.session_state:
                st.session_state["submissions"] = []
            st.session_state["submissions"].append(new_entry)
            st.success("Your complaint / review has been submitted!")
