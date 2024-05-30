# Heart Disease Prediction Project

This repository contains the necessary files for predicting heart disease using a logistic regression model. The project includes data preprocessing, model training, and a Streamlit web application for making predictions.

## Repository Contents

1. **Heart.py**: The main Streamlit application file for predicting heart disease.
2. **Heart_prepro&model.ipynb**: A Jupyter notebook for data preprocessing and model training.
3. **heart_disease_data.csv**: The dataset used for training the logistic regression model.
4. **heart_disease_model.pkl**: The trained logistic regression model saved as a pickle file.

## Description

### Heart.py

This file contains the Streamlit app code, which includes:
- Loading the trained model.
- Collecting user input for various health metrics.
- Predicting the likelihood of heart disease based on the user input.
- Displaying the prediction result and probability.

### Heart_prepro&model.ipynb

This Jupyter notebook includes:
- Data loading and exploration.
- Data preprocessing steps such as handling missing values and encoding categorical variables.
- Training a logistic regression model.
- Saving the trained model to a pickle file.

### heart_disease_data.csv

The dataset includes various features such as age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise induced angina, ST depression induced by exercise, the slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy, and thalassemia. These features are used to predict the presence of heart disease.

### heart_disease_model.pkl

This file contains the trained logistic regression model, which is used by the Streamlit app to make predictions.

## How to Run the Streamlit App

To run the Streamlit app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run Heart.py
    ```

4. Open the provided URL in your web browser to interact with the app.
