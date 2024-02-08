import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
data_balanced = pd.read_csv("data/data_balanced.csv")

def plot_dencity(var):
    #plt.figure(figsize=(4, 4))
    plt.rcParams['figure.figsize'] = [5, 3]
    sns.distplot(a=data_balanced[var], hist=False)
    # Set the plot title and axis labels
    plt.title('Density Plot of '+var)
    plt.xlabel(var)
    plt.ylabel('Density')
    # Display the plot in Streamlit
    st.pyplot()
def plot_count(var):
    plot_dencity(var)
    # Plot the histogram using sns.distplot()
    sns.distplot(a=data_balanced[var], kde=False)
    #plt.figure(figsize=(4, 4))
    plt.rcParams['figure.figsize'] = [5, 3]
    # Set the plot title and axis labels
    plt.title('Histogram of '+var)
    plt.xlabel(var)
    plt.ylabel('Count')
    # Display the plot in Streamlit
    st.pyplot()

def plot_histogram2(column_name):
    value_counts = data_balanced[column_name].value_counts()
    plt.bar(value_counts.index, value_counts.values, color=['aquamarine'])
    plt.title('Hist_' + column_name)
    plt.ylabel('Effectifs')
    plt.ylim(0, 3500)
    plt.xticks(list(value_counts.index), rotation=0, ha='right', fontsize=10)
    st.pyplot()
    plot_pie(column_name)




def plot_histogram(column_name):
    plt.bar(data_balanced[column_name].value_counts().index, data_balanced[column_name].value_counts().values, color=['aquamarine'])
    plt.title('Hist_' + column_name)
    plt.ylabel('Effectifs')
    plt.ylim(0, 3500)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    st.pyplot()
    plot_pie(column_name)

def plot_pie(column_name):
    plt.figure(figsize=(2, 10))
    plt.pie(data_balanced[column_name].value_counts().values, labels=data_balanced[column_name].value_counts().index, startangle=90, counterclock=False)
    plt.title('Pie_' + column_name)
    st.pyplot()

if st.sidebar.selectbox("Select an option", ["Variables quantitatives", "Variables qualitatives"]) == "Variables quantitatives":
    ##Streamlit code:
    st.title("Représentation graphique de Variables quantitatives")
    st.subheader("Interprétation:")
    st.write("Il est observé que certaines valeurs d'âge sont inférieures à 1, ce qui s'explique par l'interprétation des mois en tant que valeurs réelles positives. En ce qui concerne la répartition de chaque variable, il semble que le niveau moyen de glucose et l'indice de masse corporelle (IMC) suivent une distribution normale, contrairement à l'âge des patients qui ne semble pas suivre cette distribution.")
    variable =st.sidebar.selectbox("Veuillez parcourir les variables une par une:", ["age", "bmi","avg_glucose_level"])
    plot_count(variable)
else:
    ##Streamlit code:
    st.title("Représentation graphique de variables qualitatives")
    column_name=st.sidebar.selectbox("Veuillez parcourir les variables une par une", ["gender", "hypertension","heart_disease","ever_married","work_type","Residence_type","smoking_status","stroke"])
    plot_histogram2(column_name)
