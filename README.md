# AI-Powered Hospital Readmission Risk Predictor

## Overview

Hospital readmission within 30 days is a major healthcare challenge that increases treatment costs and negatively impacts patient outcomes. This project uses Machine Learning to predict whether a diabetic patient is at risk of early hospital readmission, enabling healthcare providers to take preventive measures and improve patient care.

The solution was developed using the Diabetes 130-US Hospitals Dataset and deployed as an interactive Streamlit web application.

---

## Problem Statement

Predict the likelihood of hospital readmission for diabetic patients using historical healthcare data and identify high-risk patients before discharge.

---

## Dataset

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008

**Source:** UCI Machine Learning Repository

* 101,766 patient encounters
* 50 original features
* Healthcare domain
* Binary classification problem

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* Joblib
* Git & GitHub

---

## Machine Learning Models Evaluated

### Logistic Regression

* Class Weight Balancing
* Threshold Tuning
* Regularization Tuning

### Decision Tree

* Baseline Decision Tree Classifier

### Random Forest

* Hyperparameter Tuning
* Feature Importance Analysis
* Top 10 Feature Selection

---

## Final Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 65.1% |
| Precision | 18%   |
| Recall    | 60%   |
| F1-Score  | 28%   |

The Random Forest Classifier was selected as the final model due to its superior ability to identify high-risk patients in an imbalanced healthcare dataset.

---

## Top Predictive Features

1. Number Inpatient Visits
2. Discharge Disposition ID
3. Number Emergency Visits
4. Number Medications
5. Time in Hospital
6. Number Diagnoses
7. Number Lab Procedures
8. Age
9. Number Procedures
10. Number Outpatient Visits

---

## Application Features

* Interactive Patient Input Form
* Real-Time Risk Prediction
* Probability Score Display
* Low, Moderate, and High Risk Classification
* Healthcare Recommendations
* Responsive User Interface

---

## Project Structure

```text
AI-Hospital-Readmission-Predictor/
│
├── app.py
├── readmission_model.pkl
├── requirements.txt
├── README.md
├── data/
├── notebook/
├── screenshots/
└── report/
```

---

## Application Screenshots

### Home Page


### Low Risk Prediction

### Moderate Risk Prediction

### High Risk Prediction

---

## Live Application

Public URL of the app : https://ai-powered-hospital-readmission-risk-predictor-07.streamlit.app

---

## Project Report

The complete project report and presentation are available in the **report** folder.

---

## Author

**Midde Jai Surya**

B.Tech – Artificial Intelligence and Machine Learning

GitHub: https://github.com/JaiSurya07-Peace

LinkedIn Post: https://www.linkedin.com/feed/update/urn:li:activity:7476164390795321344/
