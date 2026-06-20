
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
