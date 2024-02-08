import streamlit as st
import dtale
import missingno as msno
from tableone import TableOne
import matplotlib.pyplot as plt
import pandas as pd

def display_missing_data(data):
    figure, ax = plt.subplots()
    #msno.matrix(data, ax=ax)
    msno.bar(data)
    st.pyplot(figure)

st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.title("Dataset")
data = pd.read_csv("data/healthcare-dataset-stroke-data.csv")
# Add a search bar

# Display data with search bar
search = st.sidebar.text_input("Search", "")
if search:
    data = data[data.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]

st.dataframe(data)
st.subheader("Missing Values Matrix Plot:")
display_missing_data(data)

dtale_app = dtale.show(data.head(10))
table_one = TableOne(data)
table_one