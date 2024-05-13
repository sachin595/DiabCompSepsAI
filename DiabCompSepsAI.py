import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load the pretrained RandomForest model
model = load('diabapp.joblib')

def predict(inputs):
    # Mapping dictionaries
    sex_map = {'Male': 0, 'Female': 1}
    inout_map = {'Inpatient': 0, 'Outpatient': 1}
    transt_map = {
        'Not transferred (admitted from home)': 0, 
        'From acute care hospital inpatient': 1, 
        'Outside emergency department': 2, 
        'Other': 3
    }
    dischdest_map = {
        'Home': 0, 'Other': 1, 'Rehab': 2, 
        'Skilled Care, Not Home': 3, 'Unknown': 4
    }
    anesthes_map = {'General': 0, 'MAC/IV Sedation': 1, 'Spinal': 2, 'Other': 3}
    surgspec_map = {
        'Urology': 0, 'Orthopedics': 1, 'General Surgery': 2, 'Neurosurgery': 3, 'Thoracic': 4,
        'Otolaryngology (ENT)': 5, 'Vascular': 6, 'Plastics': 7, 'Cardiac Surgery': 8, 'Gynecology': 9
    }
    electsurg_map = {"No": 0, "Yes": 1}
    diabetes_map = {'NO': 0, 'NON-INSULIN': 1, 'INSULIN': 2}
    smoke_map = {"No": 0, "Yes": 1}
    dyspnea_map = {'No': 0, 'MODERATE EXERTION': 1, 'AT REST': 2}
    discancr_map = {"No": 0, "Yes": 1}
    emergncy_map = {"No": 0, "Yes": 1}
    asaclas_map = {"No": 0, "Yes": 1}
    steroid_map = {"No": 0, "Yes": 1}
    wndclas_map = {
        'Clean/Contaminated': 0, 'Clean': 1, 'Dirty/Infected': 2, 'Contaminated': 3
    }
    
    # Apply mappings
    inputs['sex'] = sex_map[inputs['sex']]
    inputs['inout'] = inout_map[inputs['inout']]
    inputs['transt'] = transt_map[inputs['transt']]
    inputs['dischdest'] = dischdest_map[inputs['dischdest']]
    inputs['anesthes'] = anesthes_map[inputs['anesthes']]
    inputs['surgspec'] = surgspec_map[inputs['surgspec']]
    inputs['electsurg'] = electsurg_map[inputs['electsurg']]
    inputs['diabetes'] = diabetes_map[inputs['diabetes']]
    inputs['smoke'] = smoke_map[inputs['smoke']]
    inputs['dyspnea'] = dyspnea_map[inputs['dyspnea']]
    inputs['discancr'] = discancr_map[inputs['discancr']]
    inputs['emergncy'] = emergncy_map[inputs['emergncy']]
    inputs['asaclas'] = asaclas_map[inputs['asaclas']]
    inputs['steroid'] = steroid_map[inputs['steroid']]
    inputs['wndclas'] = wndclas_map[inputs['wndclas']]
    
    # Assuming the model expects a DataFrame with the same structure as during training
    input_df = pd.DataFrame([inputs])
    prediction = model.predict(input_df)
    return prediction

def decode_predictions(y_pred):
    # Assuming y_pred is a list or an array with two elements
    sepis_mapping = {0: "No", 1: "Yes"}
    wound_infection_mapping = {0: "No", 1: "Yes"}

    # Decode each prediction assuming y_pred is structured correctly
    decoded_predictions = {
        "Presence of sepsis": sepis_mapping[y_pred[0]],
        "Presence of wound infection": wound_infection_mapping[y_pred[1]],
    }
    
    return decoded_predictions


# Streamlit user interface
st.title(' 🧑‍⚕️ DiabCompSepsAI: Prediction of Postoperative Complications in Diabetic Patients ')

# Creating form for input
with st.form(key='prediction_form'):
    sex = st.selectbox('Sex', options=['Male', 'Female'])
    inout = st.selectbox('In/Out Patient', options=['Inpatient', 'Outpatient'])
    transt = st.selectbox('Transfer Status', options=[
        'Not transferred (admitted from home)', 'From acute care hospital inpatient', 
        'Outside emergency department', 'Other'
    ])
    age = st.number_input('Age', min_value=0, max_value=120)
    dischdest = st.selectbox('Discharge Destination', options=[
        'Home', 'Other', 'Rehab', 'Skilled Care, Not Home', 'Unknown'
    ])
    anesthes = st.selectbox('Anesthesia Type', options=['General', 'MAC/IV Sedation', 'Spinal', 'Other'])
    surgspec = st.selectbox('Surgical Specialty', options=[
        'Urology', 'Orthopedics', 'General Surgery', 'Neurosurgery', 'Thoracic', 
        'Otolaryngology (ENT)', 'Vascular', 'Plastics', 'Cardiac Surgery', 'Gynecology'
    ])
    electsurg = st.selectbox('Elective Surgery', options=["No", "Yes"])
    height = st.number_input('Height (inches)', min_value=0)
    weight = st.number_input('Weight (lbs)', min_value=0)
    diabetes = st.selectbox('Diabetes Status', options=['NO', 'NON-INSULIN', 'INSULIN'])
    smoke = st.selectbox('Smoking Status', options=["No", "Yes"])
    dyspnea = st.selectbox('Difficulty in breathing', options=['No', 'MODERATE EXERTION', 'AT REST'])
    discancr = st.selectbox('Diagnosis of cancer', options=["No", "Yes"])
    dprna = st.number_input('dprna', min_value=0)
    dpralbum = st.number_input('Postoperative Albumin Level', min_value=0 )
    dprhct = st.number_input('Postoperative Hematocrit', min_value=0)
    emergncy = st.selectbox('Emergency Status', options=["No", "Yes"])
    optime = st.number_input('Operation Time (minutes)', min_value=0)
    drenainsf = st.number_input('Deep renal insufficiency', min_value=0)
    asaclas = st.selectbox('asaclass', options=["No", "Yes"])
    steroid = st.selectbox('Steroid Use', options=["No", "Yes"])
    wndclas = st.selectbox('Wound Class', options=[
        'Clean/Contaminated', 'Clean', 'Dirty/Infected', 'Contaminated'
    ])
    
    submit_button = st.form_submit_button(label='Predict')

# Processing prediction
if submit_button:
    input_data = {
        'sex': sex,
        'inout': inout,
        'transt': transt,
        'age': age,
        'dischdest': dischdest,
        'anesthes': anesthes,
        'surgspec': surgspec,
        'electsurg': electsurg,
        'height': height,
        'weight': weight,
        'diabetes': diabetes,
        'smoke': smoke,
        'dyspnea': dyspnea,
        'discancr': discancr,
        'dprna':dprna,
        'dpralbum': dpralbum,
        'dprhct': dprhct,
        'emergncy': emergncy,
        'optime': optime,
        'drenainsf': drenainsf,
        'asaclas': asaclas,
        'steroid': steroid,
        'wndclas': wndclas
    }
    # Predict and decode
    y_pred = predict(input_data)  # Ensure predict() returns the appropriate numeric predictions
    decoded_predictions = decode_predictions(y_pred.flatten())
    st.write('Prediction:', decoded_predictions)
  