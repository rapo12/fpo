import streamlit as st
import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd

def display_missing_data(data):
    fig, ax = plt.subplots()
    msno.matrix(data, ax=ax)
    st.pyplot(fig)


# display summary of missing data using summarytools
def display_missing_data_summary(data):
    summary = pd.DataFrame(data(data, prop=False, numbers=True, plot=False))
    st.table(summary)
data = pd.read_csv("data/data_with_no_value_null.csv")
st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.title("Valeurs manquantes")
st.write("Au début, le jeu de données comporte 106 valeurs manquantes dans la colonne bmi remplacées par la médiane de la colonne en question.Le nombre de valeurs manquantes dans chaque colonnes:")
st.subheader('Number of Missing Values')
st.table(display_missing_data(data))
st.write('Number of Missing Values')
st.write(data.isna().sum())


