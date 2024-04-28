import streamlit as st
import pandas as pd

df = pd.read_excel("8.xlsx")
st.dataframe(df)