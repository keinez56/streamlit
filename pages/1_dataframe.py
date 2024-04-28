import streamlit as st
import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/keinez56/streamlit/main/pages/8.xlsx")
st.dataframe(df)