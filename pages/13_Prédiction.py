import streamlit as st
import pickle
import time
import numpy as np

st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load a saved pickle model
loaded_pickle_model = pickle.load(open("model/Knn_save.pkl", "rb"))

def predict_result(loaded,age,hypertension,heart_disease ,avg_glucose_level,bmi):

    hyper = 1 if hypertension == "Oui" else 0
    heart = 1 if heart_disease == "Oui" else 0

    input_data = np.array([[age, hyper, heart, avg_glucose_level,bmi]])
    output = loaded.predict(input_data)
    mytext=""

    if output==1:
        mytext="Soyez prudent !!!! Vous présentez un risque plus élevé d'avoir un AVC."
        st.text_input("Prédiction", value=mytext, key="out", disabled=True)
        st.image("sick_brain.png",width=500)

    else:
        mytext = "Il n'y a pas de risque que vous ayez un AVC"
        st.text_input("Prédiction", value=mytext, key="out2", disabled=True)
        st.image("good_brain.png", width=500)




# Create two columns with a 2:1 ratio
st.title("Prédiction AVC")
st.subheader("choix du modéle:")
st.write("D'aprés l'étude précédente, on a:")
st.write("**1)** Le modèle KNN a une précision supérieure à celle du modèle SVC.")
st.write("**2)** Le score F1 de KNN est aussi grand que le score de SVC")
st.write("**3)** AUC (l'aire sous la courbe ROC de knn est plus grand que SVC")
left_column, right_column = st.columns([1, 1])


# In the left column, display the title, image, and more
with left_column:
    st.subheader("Résultat de prédiction : ")
    age = st.sidebar.slider("Age en années :", min_value=10, max_value=100, value=30)
    hypertension = st.sidebar.radio("Vous souffrez d'hypertension ?", ["Oui", "Non"])
    heart_disease = st.sidebar.radio("Vous souffrez d'une maladie cardiaque ?", ["Oui", "Non"])
    avg_gluc_lvl = st.sidebar.number_input("Niveau de glucose moyen :", min_value=80, max_value=500, value=90)
    bmi = st.sidebar.number_input("Indice de masse corporelle :", min_value=10, max_value=50, value=25)


# In the right column, display something else
with right_column:
    with st.spinner('Predicting...'):
        # Perform some long computation here
        time.sleep(4)
        predict_result(loaded_pickle_model, age, hypertension, heart_disease, avg_gluc_lvl, bmi)
        time.sleep(2)
