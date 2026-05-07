import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

st.title("📊 Interactive Sales Dashboard")
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

st.markdown(
    f"#### 🌍 Region Selected: {region_filter}\n"
    f"#### 🛒 Product Selected: {product_filter}"
)

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 Total Revenue", f"${filtered_df['Total Revenue'].sum():,.2f}")

with col2:
    st.metric("📈 Average Revenue", f"${filtered_df['Total Revenue'].mean():,.2f}")

tab1, tab2 = st.tabs(["🛒 Sales by Product", "🌍 Sales by Region"])

with tab1:
    st.subheader("Sales by Product")

    product_data = (
        filtered_df.groupby("Product Category")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        product_data,
        x="Product Category",
        y="Total Revenue",
        color="Product Category",
        text="Total Revenue",
        title="Sales by Product"
    )

    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Sales by Region")

    region_data = (
        filtered_df.groupby("Region")["Total Revenue"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        region_data,
        names="Region",
        values="Total Revenue",
        title="Sales by Region"
    )

    st.plotly_chart(fig2, use_container_width=True)
