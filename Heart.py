import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title('Heart Disease Prediction')

# Input features
age = st.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.selectbox('Sex', ['Male', 'Female'])

# Chest pain type
cp = st.selectbox('Chest Pain Type', [
    'Typical Angina (Type 0)',
    'Atypical Angina (Type 1)',
    'Non-anginal Pain (Type 2)',
    'Asymptomatic (Type 3)'
])

# Map chest pain type to numerical values
cp_mapping = {
    'Typical Angina (Type 0)': 0,
    'Atypical Angina (Type 1)': 1,
    'Non-anginal Pain (Type 2)': 2,
    'Asymptomatic (Type 3)': 3
}
cp_value = cp_mapping[cp]

trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol in mg/dl', min_value=100, max_value=600, value=200)

# Fasting blood sugar
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes (1)', 'No (0)'])
fbs_value = 1 if fbs == 'Yes (1)' else 0

# Resting electrocardiographic results
restecg = st.selectbox('Resting Electrocardiographic Results', [
    'Normal (0)',
    'Having ST-T wave abnormality (1)',
    'Showing probable or definite left ventricular hypertrophy (2)'
])

# Map restecg to numerical values
restecg_mapping = {
    'Normal (0)': 0,
    'Having ST-T wave abnormality (1)': 1,
    'Showing probable or definite left ventricular hypertrophy (2)': 2
}
restecg_value = restecg_mapping[restecg]

thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)

# Exercise induced angina
exang = st.selectbox('Exercise Induced Angina', ['Yes (1)', 'No (0)'])
exang_value = 1 if exang == 'Yes (1)' else 0

oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0)

# Slope of the peak exercise ST segment
slope = st.selectbox('Slope of the Peak Exercise ST Segment', [
    'Upsloping (0)',
    'Flat (1)',
    'Downsloping (2)'
])

# Map slope to numerical values
slope_mapping = {
    'Upsloping (0)': 0,
    'Flat (1)': 1,
    'Downsloping (2)': 2
}
slope_value = slope_mapping[slope]

# Number of major vessels colored by fluoroscopy
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3, 4])

# Thalassemia
thal = st.selectbox('Thalassemia', [
    'Normal (0)',
    'Fixed Defect (1)',
    'Reversible Defect (2)'
])

# Map thal to numerical values
thal_mapping = {
    'Normal (0)': 0,
    'Fixed Defect (1)': 1,
    'Reversible Defect (2)': 2
}
thal_value = thal_mapping[thal]

# Predict button
if st.button('Predict'):
    sex_value = 1 if sex == 'Male' else 0
    features = np.array([[age, sex_value, cp_value, trestbps, chol, fbs_value, restecg_value, thalach, exang_value,
                          oldpeak, slope_value, ca, thal_value]])
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.write('The model predicts that the patient has heart disease.')
    else:
        st.write('The model predicts that the patient does not have heart disease.')

    st.write(f'Prediction probability: {probability:.2f}')