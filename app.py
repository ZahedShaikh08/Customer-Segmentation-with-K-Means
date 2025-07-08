import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("🛍️ Customer Segmentation with K-Means")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
else:
    if os.path.exists("Mall_Customers.csv"):
        df = pd.read_csv("Mall_Customers.csv")
        st.info("Using default Mall Customers dataset")
    else:
        st.error("Default dataset not found. Please upload a CSV file.")
        st.stop()

st.subheader("Raw Data Preview")
st.dataframe(df.head())

st.sidebar.header("Configuration")
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
non_id_columns = [col for col in numeric_columns if 'id' not in col.lower() and 'customer' not in col.lower()]

if uploaded_file:
    default_features = non_id_columns[:2] if len(non_id_columns) >= 2 else numeric_columns[:2]
else:
    mall_defaults = ["Annual Income (k$)", "Spending Score (1-100)"]
    default_features = [col for col in mall_defaults if col in numeric_columns] or non_id_columns[:2]

features = st.sidebar.multiselect(
    "Select features for clustering", 
    options=numeric_columns,
    default=default_features
)
k = st.sidebar.slider("Number of clusters (k)", min_value=2, max_value=10, value=5)

analyze = st.sidebar.button("Analyze Clustering")

if not analyze:
    st.sidebar.write("Click 'Analyze Clustering' to run segmentation")
    st.stop()

if len(features) < 2:
    st.warning("Select at least two features for meaningful clustering.")
    st.stop()

X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

km = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = km.fit_predict(X_scaled)
df["Segment"] = labels

centers = scaler.inverse_transform(km.cluster_centers_)
centers_df = pd.DataFrame(centers, columns=features)
centers_df.index.name = "Segment"

st.subheader("Segment Profiles")
st.dataframe(
    df.groupby("Segment")[features]
      .mean()
      .round(2)
      .rename(columns={col: f"Mean {col}" for col in features})
)

st.subheader("Cluster Centers")
st.dataframe(centers_df)

st.subheader("Cluster Visualization")
if len(features) > 2:
    st.info(f"Visualizing first two features: **{features[0]}** and **{features[1]}**")

fig, ax = plt.subplots(figsize=(10, 6))
for seg in np.unique(labels):
    mask = df["Segment"] == seg
    ax.scatter(
        df.loc[mask, features[0]],
        df.loc[mask, features[1]],
        label=f"Segment {seg}",
        s=50,
        alpha=0.7
    )
ax.scatter(
    centers_df[features[0]],
    centers_df[features[1]],
    s=200,
    marker="X",
    c="black",
    label="Centers"
)
ax.set_xlabel(features[0])
ax.set_ylabel(features[1])
ax.set_title("Customer Segmentation")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.3)
st.pyplot(fig)

st.subheader("Download Segmented Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="segmented_customers.csv",
    mime="text/csv"
)
