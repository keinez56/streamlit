import streamlit as st
import pandas as pd

df = pd.read_excel("C:/Users/User/PycharmProjects/streamlit/pages/8.xlsx")
st.dataframe(df)