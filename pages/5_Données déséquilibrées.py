import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import RandomOverSampler

import pandas as pd

data = pd.read_csv("data/data_with_no_value_null.csv")

stroke_imbalance = data["stroke_c"]
counts = stroke_imbalance.value_counts()
no_stroke_count = counts["no_stroke"]
strock_count=counts["stroke"]

st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.title("Problème de données déséquilibrées")
st.write("Le jeu de données est déséquilibrées comme suit:")



# Create a dictionary of value counts for the stroke_imbalance variable
stroke_imbalance = {'stroke': strock_count, 'no stroke': no_stroke_count}

# Convert the dictionary to arrays of keys and values
keys = np.array(list(stroke_imbalance.keys()))
values = np.array(list(stroke_imbalance.values()))
plt.figure(figsize=(8,4))
# Create a bar plot
plt.bar(keys, values, color=['aquamarine', 'orange'])
plt.title('Stroke')
plt.ylabel('Effectifs')
plt.ylim(0, 2000)
# Set the size of the plot


# Display the plot in Streamlit
st.pyplot(plt.gcf())

valuewithpercent=data["stroke_c"].value_counts(normalize=True)
st.text(valuewithpercent)
st.text("On remarque bien qu'on a 87 % de no_stroke et que 12% de stroke .")
##############################  Make data balanced #########################

# Instantiate the RandomOverSampler with random state of 1969
ros = RandomOverSampler(random_state=1969)

# Define the features and target variables
X = data.drop(columns=['stroke_c'])
y = data['stroke_c']

# Apply the RandomOverSampler to the features and target
X_ros, y_ros = ros.fit_resample(X, y)

# Merge the resampled features and target into a new dataframe
data_balanced = X_ros.join(y_ros)

# Print the count of the balanced target variable
stroke_balanced=data_balanced['stroke_c'].value_counts()
no_stroke_balanced_count = stroke_balanced["no_stroke"]
stroke_balanced_count=stroke_balanced["stroke"]

st.subheader("Solution:")
st.write("Pour remédier à ce problème, j'utilise la méthode de rééchantillonnage qui consiste à modifier l'ensemble de données avant d'entraîner mon modèle de prédiction. Cette technique permet d'avoir des données plus équilibrées, ce qui améliore les performances de la prédiction.")
st.write("j'ai effectueéun suréchantillonnage (oversampling) à l'aide de la classe RandomOverSampler de la bibliothèque imbalanced-learn en Python.")
st.write("Étant donné que je dispose de peu de données, je vais privilégier l'Oversampling qui consiste à augmenter le nombre d'observations de la classe minoritaire afin d'obtenir un ratio satisfaisant entre la classe minoritaire et la classe majoritaire.")

### now i will show the plot balanced data
# Create a dictionary of value counts for the stroke_imbalance variable

stroke_balanced = {'stroke': stroke_balanced_count, 'no stroke': no_stroke_balanced_count}

# Convert the dictionary to arrays of keys and values
keys = np.array(list(stroke_balanced.keys()))
values = np.array(list(stroke_balanced.values()))
#for size
plt.figure(figsize=(8,4))

# Create a bar plot
plt.bar(keys, values, color=['aquamarine', 'orange'])
plt.title('stroke')
plt.ylabel('Effectifs')
plt.ylim(0, 2000)


# Display the plot in Streamlit
st.pyplot(plt.gcf())
