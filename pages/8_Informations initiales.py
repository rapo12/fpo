import streamlit as st
st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.title("Informations initiales")
st.subheader("On dispose des deux types de variables (quantitative et qualitative):")
st.write("**1) Quantitatives discrètes/continues :** age, avg_glucose_level, bmi")
st.write("**2) Quantitative binéaires:**  hypertension,heart_disease, stroke --> convertis en variables catégorielles pour simplifier l'analyse descriptive.")
st.write("**3) Qualitatives nominales:**  gender, ever_married, work_type, Residence_type, smoking_status.")


st.subheader("Les premiéres insights tirées de la visualisation des données vs stroke:")
st.write("**1)** L'AVC dépend fortement de l'âge du patient")
st.write("**2)** Les patients ayant un indice de masse corporelle (IMC) compris entre 20 et 35 kg/m² sont sujets à l'apparition d'un AVC")
st.write("**3)** Les travailleurs indépendants ont un risque accru de faire un AVC par rapport à d'autres types de travail")
st.write("**4)** Les personnes souffrant d'hypertension encourent un risque élevé d'AVC, avec plus de 15% d'entre elles qui en font l'expérience.")
st.write("**5)** Le risque d'avoir un AVC pour les personnes qui ont des maladies cardiaques est trés élevé, plus de 20% de personnes font un AVC quand elles sont atteintes d'une maladie cardiaque,")
st.write("**6)** Environ la moitié des personnes mariées sont susceptibles de subir un AVC.")
st.write("**7)** Les personnes ayant arrêté de fumer ont un risque plus élevé de subir un AVC.")
st.write("**8)** La survenue d'un AVC ne dépend pas nécessairement du sexe, du type de résidence ou du niveau moyen de glucose dans le corps.")