import streamlit as st
import pandas as pd

def vendor_dashboard():
    st.markdown("<h2 style='color:#4B8BBE;'>Vendor / Product Dashboard</h2>", unsafe_allow_html=True)

    submissions = st.session_state.get("submissions", [])
    df = pd.DataFrame(submissions)

    if df.empty:
        st.info("No data available yet.")
        return

    vendors = df["vendor"].dropna().unique().tolist()
    vendor = st.selectbox("Select Vendor", vendors)

    vendor_data = df[df["vendor"] == vendor]

    if vendor_data.empty:
        st.warning("No data for this vendor.")
        return

    avg_rating = vendor_data["rating"].mean()
    resolved = (vendor_data["status"] == "Resolved").mean() * 100
    trust_score = (avg_rating / 5 * 0.6 + resolved / 100 * 0.4) * 100

    st.metric("Average Rating", f"{avg_rating:.2f}")
    st.metric("Resolved Complaints (%)", f"{resolved:.1f}%")
    st.metric("Trust Score", f"{trust_score:.1f}")

    # Display FSSAI codes
    fssai_codes = vendor_data["fssai_code"].dropna().unique().tolist()
    if fssai_codes:
        st.subheader("FSSAI License(s)")
        for code in fssai_codes:
            st.write(code)
    else:
        st.info("No FSSAI codes provided for this vendor.")

    st.subheader("All Complaints for this Vendor")
    st.dataframe(vendor_data)
