import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Gene Expression Dashboard",
    layout="wide"
)

# =========================
# Load Data
# =========================
df = pd.read_csv("gene_expression.csv")

# =========================
# Sidebar Navigation
# =========================
st.sidebar.title("🧬 Navigation")

section = st.sidebar.radio(
    "Go to:",
    ["Overview", "Dataset", "TFEB", "SQSTM1", "CLN6", "Correlation", "Summary"]
)

# =========================
# Overview
# =========================
if section == "Overview":
    st.title("🧬 Gene Expression Analysis Dashboard")

    st.markdown("""
    ### 📌 Project Overview
    This dashboard analyzes gene expression levels of key lysosomal pathway genes:
    TFEB, SQSTM1, and CLN6 in Control vs Disease samples.

    The goal is to identify biological differences using data visualization.
    """)

    st.success("Use the sidebar to explore different sections of the analysis.")

    st.metric("Total Samples", len(df))
    st.metric("Genes Analyzed", 3)

# =========================
# Dataset
# =========================
if section == "Dataset":
    st.header("📁 Dataset Preview")
    st.dataframe(df)

# =========================
# TFEB
# =========================
if section == "TFEB":
    st.header("1. TFEB Expression")

    fig, ax = plt.subplots()
    df.groupby("Group")["TFEB"].mean().plot(kind="bar", ax=ax, color=["green", "red"])
    ax.set_ylabel("Mean Expression")
    st.pyplot(fig)

    st.info("""
    📌 Insight:
    TFEB expression is lower in disease samples, suggesting reduced lysosomal function and impaired cellular clearance.
    """)

# =========================
# SQSTM1
# =========================
if section == "SQSTM1":
    st.header("2. SQSTM1 Expression")

    fig, ax = plt.subplots()
    df.groupby("Group")["SQSTM1"].mean().plot(kind="bar", ax=ax, color=["green", "red"])
    ax.set_ylabel("Mean Expression")
    st.pyplot(fig)

    st.info("""
    📌 Insight:
    SQSTM1 is increased in disease, indicating autophagy stress and accumulation of cellular waste.
    """)

# =========================
# CLN6
# =========================
if section == "CLN6":

    st.header("3. CLN6 Distribution")

    st.markdown("""
    ### 📌 What does this plot show?
    This boxplot shows how CLN6 values are distributed in Control vs Disease groups.
    It helps identify variability and abnormal expression levels.
    """)

    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Group", y="CLN6", ax=ax)
    st.pyplot(fig)

    st.info("""
    📌 Insight:
    CLN6 expression varies between groups, indicating possible disruption in lysosomal function and increased variability in disease samples.
    """)

if section == "Correlation":

    st.header("4. Gene Correlation Heatmap")

    st.markdown("""
    ### 📌 What does this mean?
    - Positive values (close to +1) → genes move together
    - Negative values (close to -1) → genes move in opposite directions
    - Zero → no relationship
    """)

    corr = df[["TFEB", "SQSTM1", "CLN6"]].corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

    st.info("""
    📌 Insight:
    This heatmap shows how genes are biologically connected.
    TFEB and SQSTM1 show opposite behavior, suggesting dysregulation in disease.
    """)

    st.info("""
    📌 Insight:
    Genes show correlated expression patterns, indicating coordinated disruption of lysosomal pathways in disease.
    """)

if section == "Summary":

    st.title("📌 Final Summary Report")

    st.markdown("""
    ## 🧬 Project Overview
    This project analyzed gene expression data for three lysosomal pathway genes:
    TFEB, SQSTM1, and CLN6 across Control and Disease samples.

    The goal was to identify biological differences using data visualization techniques.
    """)

    st.markdown("""
    ## 📊 Key Findings

    ### 🔹 TFEB
    - Decreased expression in disease samples
    - Suggests reduced lysosomal biogenesis

    ### 🔹 SQSTM1
    - Increased expression in disease
    - Indicates autophagy stress and waste accumulation

    ### 🔹 CLN6
    - Variable distribution between groups
    - Suggests lysosomal dysfunction and instability
    """)

    st.markdown("""
    ## 🔗 Correlation Insights
    - TFEB and SQSTM1 show an inverse relationship
    - Gene expression patterns are interconnected
    - Suggests coordinated disruption of lysosomal pathway
    """)

    st.markdown("""
    ## 🎯 Conclusion
    The analysis indicates that disease samples show clear dysregulation in lysosomal pathway genes,
    which may contribute to impaired cellular clearance and autophagy imbalance.
    """)

    st.success("✔ This dashboard successfully demonstrates basic bioinformatics data analysis using Python and Streamlit.")

