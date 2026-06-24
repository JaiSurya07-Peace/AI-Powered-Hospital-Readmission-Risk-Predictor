import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("readmission_model.pkl")

# Age Mapping
age_map = {
    '[0-10)':0,
    '[10-20)':1,
    '[20-30)':2,
    '[30-40)':3,
    '[40-50)':4,
    '[50-60)':5,
    '[60-70)':6,
    '[70-80)':7,
    '[80-90)':8,
    '[90-100)':9
}

st.set_page_config(
    page_title="AI Hospital Readmission Predictor",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<div style="
background:#1F2937;
padding:20px;
border-radius:12px;
text-align:center;
margin-bottom:20px;
">
<h1 style="color:white;">
🏥 AI-Powered Hospital Readmission Risk Predictor
</h1>
<p style="color:#B0B0B0;">
Predict hospital readmission risk using Machine Learning
</p>
</div>
""", unsafe_allow_html=True)

st.write("Enter patient details below")

# Sidebar

with st.sidebar:

    st.header("ℹ️ Project Information")

    st.write("""
    Algorithm:
    Random Forest Classifier
    """)

    st.write("""
    Features Used:
    - Age
    - Number of Inpatient Visits
    - Number of Emergency Visits
    - Number of Outpatient Visits
    - Number of Diagnoses
    - Number of Medications
    - Number of Lab Procedures
    - Number of Procedures
    - Time in Hospital
    - Discharge Disposition ID
    """)

    st.divider()
    st.write("Developed by Midde Jai Surya")


# Inputs

col1, col2 = st.columns(2)

with col1:

    age = st.selectbox(
        "Age Group",
        list(age_map.keys())
    )

    number_inpatient = st.number_input(
        "Number of Previous Inpatient Visits",
        min_value=0,
        value=0
    )

    number_emergency = st.number_input(
        "Number of Emergency Visits",
        min_value=0,
        value=0
    )

    number_outpatient = st.number_input(
        "Number of Outpatient Visits",
        min_value=0,
        value=0
    )

    time_in_hospital = st.number_input(
        "Time in Hospital (Days)",
        min_value=1,
        value=3
    )

with col2:

    num_medications = st.number_input(
        "Number of Medications",
        min_value=0,
        value=10
    )

    number_diagnoses = st.number_input(
        "Number of Diagnoses",
        min_value=1,
        value=5
    )

    num_lab_procedures = st.number_input(
        "Number of Lab Procedures",
        min_value=0,
        value=40
    )

    num_procedures = st.number_input(
        "Number of Procedures",
        min_value=0,
        value=0
    )

    discharge_disposition_id = st.number_input(
        "Discharge Disposition ID",
        min_value=1,
        value=1
    )

st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([2,1,2])

with center:

    predict = st.button(
        "Predict Readmission Risk"
    )



if predict:
    input_df = pd.DataFrame([{
        "number_inpatient": number_inpatient,
        "discharge_disposition_id": discharge_disposition_id,
        "number_emergency": number_emergency,
        "num_medications": num_medications,
        "time_in_hospital": time_in_hospital,
        "number_diagnoses": number_diagnoses,
        "num_lab_procedures": num_lab_procedures,
        "age": age_map[age],
        "num_procedures": num_procedures,
        "number_outpatient": number_outpatient
    }])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if probability < 0.30:
        st.success("Low Risk of Readmission")
        st.markdown("""
        Recommendations:
        - Continue prescribed medications.
        - Maintain a healthy diet and lifestyle.
        - Attend regular follow-up appointments.
        - Monitor blood glucose levels periodically.
        """)
    elif probability < 0.60:
        st.warning("Moderate Risk of Readmission")
        st.markdown("""
        Recommendations:
        - Schedule follow-up visits with healthcare providers.
        - Ensure medication adherence.
        - Monitor symptoms closely.
        - Maintain proper diabetes management.
        - Seek medical attention if symptoms worsen.
        """)  
    else:
        st.error("High Risk of Readmission")
        st.markdown("""
        Recommendations:
        - Immediate post-discharge follow-up is advised.
        - Review medications with healthcare providers.
        - Monitor blood glucose and vital signs regularly.
        - Consider care coordination or home healthcare support.
        - Seek medical attention promptly if complications arise.
        """)

    st.write(
        f"Probability of Readmission: {probability:.2%}"
    )
    st.progress(probability)