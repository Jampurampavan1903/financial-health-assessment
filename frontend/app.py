import streamlit as st
import pandas as pd
import requests

# ---------------- CONFIG ----------------
BACKEND_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="Financial Health Analyzer",
    layout="wide"
)

# ---------------- UI HEADER ----------------
st.title("💰 Financial Health Assessment")
st.write(
    "Upload your monthly cashflow CSV to analyze savings, expenses, "
    "overall financial health, and predict next month income."
)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file:
    with st.spinner("Analyzing your financial data..."):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "text/csv"
            )
        }

        try:
            response = requests.post(BACKEND_URL, files=files)
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            st.error("❌ Backend connection failed.")
            st.code(str(e))
            st.stop()

    # ---------------- SUMMARY ----------------
    summary = data["summary"]

    st.subheader("📊 Overall Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Savings Rate",
        f"{summary['average_savings_rate']:.2f}"
    )

    col2.metric(
        "Trend",
        summary["trend"]
    )

    col3.metric(
        "Overall Health",
        summary["overall_health"]
    )

    # ---------------- FORECAST ----------------
    st.subheader("📈 Forecast")

    st.metric(
        "Next Month Income Prediction",
        f"{data['forecast_next_month_income']:,.0f}"
    )

    # ---------------- MONTHLY DATA ----------------
    st.subheader("📅 Monthly Breakdown")

    df = pd.DataFrame(data["monthly_analysis"])
    df["month"] = pd.to_datetime(df["month"])

    st.dataframe(
        df,
        use_container_width=True
    )

    # ---------------- CHARTS ----------------
    st.subheader("📉 Income vs Expenses")

    chart_df = df.set_index("month")[["income", "expenses"]]
    st.line_chart(chart_df)

    st.subheader("💾 Savings Over Time")
    st.bar_chart(df.set_index("month")["savings"])

    st.subheader("📊 Savings Rate")
    st.line_chart(df.set_index("month")["savings_rate"])

else:
    st.info("⬆️ Upload a CSV file to begin analysis.")