import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Employee Dashboard", page_icon=":bar_chart:", layout="wide")


df = pd.read_excel(
    io="teams1.xlsx",
    engine="openpyxl",
    usecols="A:K",
    nrows=10500,
)


st.sidebar.header("Please Filter Here:")
User = st.sidebar.multiselect(
    "Select the Employee name:",
    options=df["User"].unique()
    #default=df["City"].unique()
)
df_selection = df.query("User == @User")
print(df)
st.dataframe(df_selection)
