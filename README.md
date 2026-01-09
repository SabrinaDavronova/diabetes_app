Diabetes Risk Prediction Web Application

Project Overview

This project implements a machine learning–based web application that estimates the risk of diabetes using clinical and anthropometric data.
The application covers the complete workflow from data preprocessing and model training to deployment with a web interface.
The goal of the project is twofold:
- To build an interpretable medical risk prediction model
- To demonstrate an end-to-end ML pipeline suitable for deployment

Dataset and Feature Preparation

The dataset contains demographic, clinical, and body measurement features commonly used in diabetes risk assessment.
Raw Features:
- Age
- Sex
- Fasting blood glucose
- HbA1c
- HDL cholesterol
- Systolic blood pressure
- Diastolic blood pressure
- Height
- Weight
- Waist circumference
- Hip circumference

Engineered Features
Two medically relevant features were calculated:
- Body Mass Index (BMI)(Calculated using height and weight)
- Waist-to-Hip Ratio (WHR)(Calculated using waist and hip circumference)
These features were added to improve predictive performance and align the model with clinical practice.

Target Variable Construction

The dataset did not include a predefined diabetes label.
The target variable was created based on established clinical thresholds and risk factors.
An individual was labeled as high risk if one or more of the following conditions were met:
- HbA1c ≥ 6.5%
- Fasting glucose ≥ 126 mg/dL
- Combination of metabolic risk indicators such as obesity, hypertension, low HDL cholesterol, and elevated waist-to-hip ratio
This approach reflects screening logic used in medical practice rather than arbitrary labeling.

Preprocessing and Machine Learning Pipeline
A scikit-learn Pipeline was used to ensure consistent preprocessing during training and inference.
Pipeline steps:
- Feature scaling using StandardScaler
- Logistic Regression classifier
Using a pipeline prevents data leakage and simplifies deployment by encapsulating preprocessing and modeling in a single object.
The trained pipeline was serialized using joblib and reused in the web application.

Model Selection and Training

Logistic Regression was selected for this project due to:
- Its suitability for binary classification
- Interpretability of coefficients
Common use in medical risk prediction tasks
The model outputs probabilities, allowing the application to present risk as a percentage rather than a binary decision.

Model Evaluation
The model was evaluated on a held-out test set.
Performance metrics:
Accuracy: approximately 94%
ROC AUC: approximately 0.97
The learned coefficients aligned with medical expectations: Higher HbA1c, blood pressure, BMI, and WHR increased predicted risk
Higher HDL cholesterol reduced predicted risk

Web Application Architecture

Backend
Framework: FastAPI
Responsibilities:
Load the trained ML pipeline
Validate user input
Perform inference
Return risk probability and interpretation
Frontend
Technologies: HTML, CSS, Jinja2 templates
Features:
Structured form for user input
Automatic calculation of BMI and waist-to-hip ratio
Clear explanations for medical terms
Display of predicted risk and guidance message
The interface is designed to be usable by non-technical users while maintaining medical clarity.

Deployment

The application is deployed using Render.
Deployment steps:
Source code hosted on GitHub
Dependencies specified in requirements.txt
FastAPI application served using Uvicorn
Model pipeline loaded at runtime
The deployed application is accessible via a public URL and can be updated by pushing changes to the repository.

Limitations

The model is trained on a limited dataset and may not generalize to all populations
The prediction represents risk estimation, not a medical diagnosis
External clinical validation was not performed

Disclaimer

This project is intended for educational and demonstration purposes only.
It does not provide medical advice or diagnosis.
Users should consult qualified healthcare professionals for medical decisions.
