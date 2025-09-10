import streamlit as st
import pandas as pd
import altair as alt

def analytics_dashboard():
    st.markdown("<h2 style='color:#4B8BBE;'>Analytics Dashboard</h2>", unsafe_allow_html=True)

    submissions = st.session_state.get("submissions", [])
    df = pd.DataFrame(submissions)

    if df.empty:
        st.info("No data available yet.")
        return

    view_option = st.radio("Select view type:", ["Streamlit Charts", "Export for Power BI"])

    if view_option == "Streamlit Charts":
        st.subheader("Top Products by Complaints")
        top_products = df["product_name"].value_counts().reset_index()
        top_products.columns = ["Product Name", "Count"]
        st.bar_chart(top_products.set_index("Product Name").head(10))

        st.subheader("Ratings Distribution")
        rating_counts = df["rating"].value_counts().reset_index()
        rating_counts.columns = ["Rating", "Count"]
        chart = alt.Chart(rating_counts).mark_bar().encode(
            x="Rating:O",
            y="Count:Q"
        )
        st.altair_chart(chart, use_container_width=True)

        st.subheader("Complaint Trends")
        df["submission_index"] = range(len(df))
        line_chart = alt.Chart(df).mark_line(point=True).encode(
            x="submission_index",
            y="rating",
            tooltip=["product_name", "rating", "status"]
        )
        st.altair_chart(line_chart, use_container_width=True)

        # FSSAI compliance summary
        st.subheader("FSSAI Compliance Overview")
        fssai_count = df["fssai_code"].notna().sum()
        total_submissions = len(df)
        st.metric("Submissions with FSSAI code", f"{fssai_count}/{total_submissions}")

    elif view_option == "Export for Power BI":
        st.subheader("Export Submissions for Power BI")
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download CSV for Power BI",
            data=csv,
            file_name="submissions_powerbi.csv",
            mime="text/csv"
        )
        st.info(
            "Open Power BI Desktop → Get Data → CSV → select this file → build visualizations."
        )
