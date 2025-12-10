
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("Data Science Portfolio – Analytics Dashboard")

@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=90, freq="D")
    revenue = np.cumsum(np.random.normal(0.0, 5.0, size=len(dates))) + 500
    cost = revenue * np.random.uniform(0.5, 0.8, size=len(dates))
    df = pd.DataFrame({"date": dates, "revenue": revenue, "cost": cost})
    df["profit"] = df["revenue"] - df["cost"]
    return df

df = load_data()
df.set_index("date", inplace=True)

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=df.index.min().to_pydatetime(),
    max_value=df.index.max().to_pydatetime(),
    value=(df.index.min().to_pydatetime(), df.index.max().to_pydatetime()),
)

mask = (df.index >= pd.to_datetime(date_range[0])) & (df.index <= pd.to_datetime(date_range[1]))
filtered = df.loc[mask]

# KPI row
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered['revenue'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered['profit'].sum():,.0f}")
col3.metric("Avg Margin", f"{(filtered['profit'].sum() / filtered['revenue'].sum() * 100):.1f}%")

# Charts
st.subheader("Revenue & Profit Over Time")
st.line_chart(filtered[["revenue", "profit"]])

st.subheader("Revenue Distribution")
st.bar_chart(filtered["revenue"])
