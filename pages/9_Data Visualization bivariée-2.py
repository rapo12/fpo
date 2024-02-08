import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly as pltoy
import pandas as pd
import numpy as np


st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
data_balanced = pd.read_csv("data/data_balanced.csv")


def render_nuage_points(column3, column4):
    x_var = column3
    y_var = column4

    # __Correlation Level #####
    fig = px.scatter(data_balanced, x=x_var, y=y_var, trendline='ols',
                     title='Correlation Level',
                     labels={x_var: column3, y_var: column4})
    fig.update_layout(plot_bgcolor='white', margin=dict(t=50, b=50, l=50, r=50))
    #return fig
    st.plotly_chart(fig)
def render_correlation(column3, column4):
    x_var = column3
    y_var = column4
    coeff_value = np.corrcoef(data_balanced[x_var], data_balanced[y_var])[0,1]
    return st.write(f"Coefficient de correlation lineaire = {coeff_value:.2f}")

def plot_distribution(x,y):
    #plt.figure(figsize=(8,6))
    plt.rcParams['figure.figsize'] = [5, 3]
    sns.countplot(x=x, hue=y, data=data_balanced)
    #plt.title(y.title()+" distribution")
    plt.legend(loc="lower center")
    st.pyplot()

def update_barplotBi(col1, col2):
    # Diagramme en barres entre les variables 'Level' et 'Sex'
    fig = px.histogram(data_balanced, x=col1, color=col2, barmode='group')
    fig.update_layout(
        title='Barplot',
        xaxis_title=col1,
        yaxis_title='Count'
    )
    st.plotly_chart(fig)

def plot_box_for_qunti_qualit(x,y):
    title=y.title()+' Box Plot with  '+x.title()
    fig3 = px.box(data_balanced, x=x, y=y, color=x,
                  title=title, points='all')
    st.plotly_chart(fig3)

var=st.sidebar.selectbox("Select an option", ["BiVariables quantitatives", "BiVariables qualitatives","BiVariables qualitative quantitative"])
if var == "BiVariables quantitatives":
    ##Streamlit code:
    st.title("Analyse bivarariée entre deux variables quantitatives")
    st.write("En observant le graphique des densités conditionnelles des variables quantitatives, il est clair que l'âge a une forte influence sur la survenue d'un AVC. Dans cette section, nous calculons la corrélation entre les différentes paires de variables quantitatives suivantes : âge, taux moyen de glucose dans le sang et indice de masse corporelle (IMC).")
    variable_x =st.sidebar.selectbox("Veuillez choisir deux variables quantitatives différentes:", ["age", "bmi","avg_glucose_level"])
    variable_y =st.sidebar.selectbox("Sélectionner la deuxième", ["age", "bmi","avg_glucose_level"])
    render_nuage_points(variable_x,variable_y)
    render_correlation(variable_x,variable_y)
    st.write("En se basant sur les valeurs de chaque coefficient de corrélation linéaire, on peut conclure que la corrélation entre les différentes variables quantitatives est faible. Par conséquent, il n'existe pas de relation linéaire significative entre ces variables")

elif var =="BiVariables qualitatives":
    ##Streamlit code:
    st.title("Analyse bivariée entre deux variables qualitatives")
    st.write("D'aprés l'analyse exploratoire des variables qualitatives vs notre variable cible stroke, on a constaté que les variables qualitatives contribuants à l'AVC sont: hypertension, heart_desease, ever_married et work_type. Etudions alors la relations entre ces variables significatives: hypertension vs ever_married, heart_disease vs ever_married et work_type vs ever_married.")
    column_name_x=st.sidebar.selectbox("Veuillez choisir deux variables qualitatives différentes:", ["hypertension","heart_disease","ever_married","work_type"])
    column_name_y = st.sidebar.selectbox("Sélectionner la deuxième :",
                                         ["hypertension", "heart_disease", "ever_married", "work_type"])
    update_barplotBi(column_name_x,column_name_y)
    st.subheader("Les résultats obtenus grâce à cette étude :")
    st.write("**1):** Les personnes mariées sont plus sujettes à l'hypertension et aux maladies cardiaques.")
    st.write("**2):** Les personnes mariés travaillent plus en indépendance et en privé.")
else:
    st.title("Représentation graphique de Variables quantitatives")
    column_name_y = st.sidebar.selectbox("Sélectionner la Variable Y :",
                                         ["age", "bmi", "avg_glucose_level"])
    title=column_name_y.title()
    st.subheader("Y = "+title)
    plot_box_for_qunti_qualit("hypertension",column_name_y)
    plot_box_for_qunti_qualit("heart_disease", column_name_y)
    plot_box_for_qunti_qualit("ever_married", column_name_y)
    plot_box_for_qunti_qualit("work_type", column_name_y)