import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", page_icon="📊")

st.title("📊 Sales Dashboard")
st.sidebar.header("🔍 Filter Data")

df = pd.read_csv("Online_Sales_Data.csv")

region_filter = st.sidebar.multiselect(
    "🌍 Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "🛒 Select Product",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product Category"].isin(product_filter))
]

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 Total Revenue", f"${filtered_df['Total Revenue'].sum():,.2f}")

with col2:
    st.metric("📈 Average Revenue", f"${filtered_df['Total Revenue'].mean():,.2f}")
