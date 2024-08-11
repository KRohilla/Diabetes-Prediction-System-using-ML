import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open('C:/Users/91863/OneDrive/Desktop/Nptel/Projects/diabetes/diabetes_model.sav', 'rb'))


# making the sidebar for navigate
with st.sidebar:
    selected = option_menu("Disase System",
                           ["Diabetes Prediction"], 
                           icons=['activity'],
                           default_index=0)

# Diabets prediction page
if (selected=="Diabetes Prediction"):
    # creating a title
    st.title("Diabetes Prediction using Machine Learning")

    # taking the input from the user
    # columns for input fields --> means input field in one row
    # making 3 columns for rows 
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("Body Mass Index Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age Value")
    
    # code for prediction
    diab_result = ""

    # creating the button for the result of prediction
    if st.button("Diabetes Test"):
        # diabetes prediction model using here to check if the person is diabetic or not
        # giving a list of list to tell that we are predicting for the single data point
        diab_prediction = diabetes_model.predict(
            [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        )

        if diab_prediction[0] == 1:
            diab_result = "Person is Diabetic"
        else:
            diab_result = "Person Is NOT Diabetic"

    st.success(diab_result)
