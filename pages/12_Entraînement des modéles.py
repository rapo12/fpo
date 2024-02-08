import streamlit as st
import pandas as pd
import pickle
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score ,f1_score, roc_auc_score, confusion_matrix,ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve

svc = SVC(probability=True)
knn = KNeighborsClassifier()

st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
data_balanced = pd.read_csv("data/data_balanced.csv")
def split_data(data=data_balanced):
    X = data_balanced[['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi']]
    Y = data_balanced['stroke']
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        Y,
                                                        test_size=0.2)  # you can change the test size

    #X_train.shape, X_test.shape, y_train.shape, y_test.shape
    # feature Scaling
    #st_x = StandardScaler()
    #X_train = st_x.fit_transform(X_train)
    #X_test = st_x.transform(X_test)
    return X_train, X_test, y_train, y_test


def plot_roc_curve(model ,X_test,y_test):
    modelname = model.__class__.__name__
    st.write("Visualisation de la courbe ROC")
    # Make predictions with probabilities
    y_probs = model.predict_proba(X_test)

    # Keep the probabilites of the positive class only
    y_probs = y_probs[:, 1]

    # Calculate fpr, tpr and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, y_probs)
    # Clear the previous plot
    plt.clf()
    # Plot ROC curve
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label='Guessing')
    # Customize the plot
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    if modelname == "svc":

        # Save the plot as a PNG file
        plt.savefig("roc_svc.png")
        # Display the plot in the Streamlit app
        st.image("roc_knn.png")

    else:

        # Save the plot as a PNG file
        plt.savefig("confusion_matrix_knn.png")
        # Display the plot in the Streamlit app
        st.image("confusion_matrix_knn.png")



def train_model_and_show_matrix(model):
    modelname=model.__class__.__name__
    X_train, X_test, y_train, y_test = split_data()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    fsc = f1_score(y_test, y_pred, average='weighted')


    accuracy_label="%.2f" %accuracy
    fsc_label="%.2f" %fsc

    # Generate a confusion matrix
    cm = confusion_matrix(y_true=y_test, y_pred=y_pred)

    # Create a ConfusionMatrixDisplay object
    cmd = ConfusionMatrixDisplay(confusion_matrix=cm)

    # Plot the confusion matrix using matplotlib
    fig, ax = plt.subplots()
    cmd.plot(ax=ax)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted labels")
    plt.ylabel("True labels")
    if modelname=="svc":

        # Save the plot as a PNG file
        plt.savefig("confusion_matrix_svc.png")
        # Display the plot in the Streamlit app
        st.image("confusion_matrix_svc.png")


    else:

        # Save the plot as a PNG file
        plt.savefig("confusion_matrix_knn.png")
        # Display the plot in the Streamlit app
        st.image("confusion_matrix_knn.png")
        # Saving a model with pickle


        # Save an existing model to file
        pickle.dump(model, open("model/Knn_save.pkl", "wb"))
    #####################################
    st.text_input("accuracy_"+modelname, value=accuracy_label, key="accuracy_"+accuracy_label, disabled=True)
    st.text_input("fsc_"+modelname, value=fsc_label, key="fsc_"+accuracy_label, disabled=True)
    ################ROC#####################
    plot_roc_curve(model,X_test,y_test)


st.set_option('deprecation.showPyplotGlobalUse', False)
# Create two columns with a 2:1 ratio
st.title("KNeighborsClassifier (KNN) vs SVC")
st.write("La prédiction de la probabilité d'un AVC chez un patient implique l'utilisation de variables explicatives comprenant des variables quantitatives et qualitatives nominales et binaires. En conséquence, la variable cible est de nature catégorique binaire.")
st.write("KNN est un excellent choix de modèle, mais dans notre jeu de données, il y a plus de variables qualitatives que quantitatives. Dans de tels cas, SVC peuvent également être performantes.")
st.write("À partir des diverses analyses et explorations de données effectuées, il est possible de conclure que les variables qui expliquent le mieux la variable cible **stroke** sont l'âge, l'hypertension, les maladies cardiaques, le niveau moyen de glucose et l'indice de masse corporelle (IMC). Ces variables seront utilisées pour entraîner deux modèles de classification : KNN et  SVC, afin de déterminer le plus performant.")
left_column, right_column = st.columns([1, 1])

# In the left column, display the title, image, and more
with left_column:
    st.write("# KNN")
    st.write("Matrice de confusion de test KNN:")
    train_model_and_show_matrix(knn)

# In the right column, display something else
with right_column:
    st.write("# SVC")
    st.write("Matrice de confusion de test SVC:")
    train_model_and_show_matrix(svc)
