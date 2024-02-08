import streamlit as st
from PIL import Image
import os
# Open the image file
#image = Image.open("umi_logo.png")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load image from file
image = Image.open(os.path.join(BASE_DIR, 'FP-Ouarzazat.png'))
# Display the image
st.image(image, caption='Sunrise over mountains', use_column_width=True)


st.title("Mini-Projet en Machine Learning")
st.header("Prédiction d'AVC (Accident vasculaire cérébral)")

st.subheader("Réalisé par : ")
st.subheader("Najat AIT AHMED - Ayoub FACH - Rayhan EL HOUCHET")
st.subheader("Encadré par :")
st.subheader("Abd Elkarim Mouatasim")


