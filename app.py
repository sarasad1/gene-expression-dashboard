
app_code = """
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gene_expression.csv")

st.title("Gene Expression Dashboard")

st.dataframe(df)

fig, ax = plt.subplots()
df.groupby("Group")["TFEB"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)
st.success("TFEB lower in disease")

fig, ax = plt.subplots()
df.groupby("Group")["SQSTM1"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)
st.success("SQSTM1 higher in disease")

fig, ax = plt.subplots()
sns.boxplot(data=df, x="Group", y="CLN6", ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="TFEB", y="SQSTM1", hue="Group", ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, ax=ax)
st.pyplot(fig)
"""

with open("app.py", "w") as f:
    f.write(app_code)

from google.colab import files
files.download("app.py")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Load Data
# =========================
df = pd.read_csv("gene_expression.csv")

# =========================
# Title + Overview
# =========================
st.title("🧬 Gene Expression Analysis Dashboard")

st.markdown("""
### 📌 Project Overview
This dashboard analyzes gene expression levels of key lysosomal pathway genes:
TFEB, SQSTM1, and CLN6 in Control vs Disease samples.

The goal is to identify biological differences using data visualization.
""")

# =========================
# Instructions
# =========================
st.markdown("""
### 📊 How to Use This Dashboard
- Scroll down to explore all visualizations
- Compare Control vs Disease groups
- Read insights under each chart
""")

# =========================
# Dataset
# =========================
st.header("📁 Dataset Preview")
st.dataframe(df)

# =========================
# TFEB
# =========================
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
st.header("3. CLN6 Distribution")

fig, ax = plt.subplots()
sns.boxplot(data=df, x="Group", y="CLN6", ax=ax)
st.pyplot(fig)

st.info("""
📌 Insight:
CLN6 shows variation between groups, suggesting involvement in lysosomal dysfunction in disease.
""")

# =========================
# TFEB vs SQSTM1
# =========================
st.header("4. TFEB vs SQSTM1")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="TFEB", y="SQSTM1", hue="Group", ax=ax)
st.pyplot(fig)

st.info("""
📌 Insight:
An inverse relationship is observed between TFEB and SQSTM1, indicating opposite regulation in disease conditions.
""")

# =========================
# Heatmap
# =========================
st.header("5. Gene Correlation Heatmap")

fig, ax = plt.subplots()
sns.heatmap(df[["TFEB", "SQSTM1", "CLN6"]].corr(), annot=True, ax=ax)
st.pyplot(fig)

st.info("""
📌 Insight:
Genes show correlated expression patterns, suggesting coordinated disruption of lysosomal pathways in disease.
""")

