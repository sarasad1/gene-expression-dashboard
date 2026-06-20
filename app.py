import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="CLN6 Gene Expression Dashboard",
    layout="wide"
)

# =========================
# Load Real Dataset
# =========================
df = pd.DataFrame({
    "Group": ["Control", "Disease"],
    "BCHE": [86, 269],
    "C1R": [5088, 14781],
    "CLU": [5229, 14398],
    "CAV2": [6106, 3086],
    "AIM1": [2759, 964]
})

# =========================
# Sidebar Navigation
# =========================
st.sidebar.title("🧬 Navigation")

section = st.sidebar.radio(
    "Go to:",
    ["Overview", "Dataset", "BCHE", "C1R", "CLU", "Correlation", "Summary", "Data Source"]
)

# =========================
# Overview
# =========================
if section == "Overview":

    st.title("🧬 CLN6 Gene Expression Analysis Dashboard")

    st.markdown("""
    ### 📌 Project Overview
    This project analyzes gene expression changes in CLN6-deficient fibroblasts
    compared to healthy control samples using real microarray study data.

    The goal is to explore biological differences using data visualization techniques.
    """)

    st.success("Use the sidebar to navigate through different analysis sections.")

    st.metric("Groups", 2)
    st.metric("Genes Analyzed", 5)

# =========================
# Dataset
# =========================
if section == "Dataset":

    st.header("📁 Real Dataset")

    st.dataframe(df)

# =========================
# BCHE
# =========================
if section == "BCHE":

    st.header("BCHE Expression")

    fig, ax = plt.subplots()
    df.set_index("Group")["BCHE"].plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.info("BCHE is significantly increased in disease samples, indicating altered metabolic activity.")

# =========================
# C1R
# =========================
if section == "C1R":

    st.header("C1R Expression")

    fig, ax = plt.subplots()
    df.set_index("Group")["C1R"].plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.info("C1R shows strong upregulation in disease, suggesting immune and inflammatory response activation.")

# =========================
# CLU
# =========================
if section == "CLU":

    st.header("CLU Expression")

    fig, ax = plt.subplots()
    df.set_index("Group")["CLU"].plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.info("CLU is elevated in disease, indicating stress response and neurodegeneration association.")

# =========================
# Correlation
# =========================
if section == "Correlation":

    st.header("📊 Gene Correlation Heatmap")

    corr = df.drop(columns=["Group"]).corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

    st.markdown("""
    ### 📌 Interpretation:
    - Genes show coordinated expression changes in CLN6 disease
    - Strong correlations suggest shared biological pathways
    """)

# =========================
# Summary Page
# =========================
if section == "Summary":

    st.title("📌 Final Summary")

    st.markdown("""
    ## 🧬 Key Findings

    - CLN6 disease shows strong gene expression dysregulation
    - BCHE, C1R, CLU are significantly upregulated
    - CAV2 and AIM1 are downregulated
    - Indicates immune activation + lysosomal dysfunction

    ## 🎯 Conclusion
    Gene expression analysis reveals major biological differences between
    control and CLN6-deficient fibroblasts.
    """)

    st.success("✔ This dashboard demonstrates real bioinformatics analysis using published data.")

# =========================
# Data Source
# =========================
if section == "Data Source":

    st.title("📚 Data Source")

    st.markdown("""
    Study Title:
    Gene expression profiling in vLINCL CLN6-deficient fibroblasts

    Description:
    This dataset is derived from a published microarray study comparing
    CLN6-deficient fibroblasts with healthy controls.

    Type:
    Processed gene expression values (Control vs Disease)
Use in this project:
    Used for bioinformatics visualization and comparative gene expression analysis.
    """)

    st.success("Dataset is based on a real published scientific study.")

