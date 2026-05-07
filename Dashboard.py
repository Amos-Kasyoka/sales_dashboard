import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Sales Dashboard")

# Sidebar
st.sidebar.header("Filter Data")

# Load data
df = pd.read_csv("Online_Sales_Data.csv")

# Filters
region_filter = st.sidebar.multiselect(
    "Select Region(s)",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product(s)",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

# Filter dataframe
filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product Category"].isin(product_filter))
]

# Display selected filters
st.markdown(
    f"#### Region Selected: {region_filter}\n"
    f"#### Product Selected: {product_filter}"
)

# Metrics
col1, col2 = st.columns(2)

with col1:
    total_sales = filtered_df["Total Revenue"].sum()
    st.metric("Total Revenue", f"${total_sales:,.2f}")

with col2:
    average_sales = filtered_df["Total Revenue"].mean()
    st.metric("Average Revenue", f"${average_sales:,.2f}")