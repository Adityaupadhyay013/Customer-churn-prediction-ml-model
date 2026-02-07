import streamlit as st
import pandas as pd 
from Customer_churn_prediction_model import Predictor
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction App",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
# -----------------------------
# UI Header
# -----------------------------
st.title("🤖 Customer Churn Prediction App")
st.write("Enter details below to get predictions")

# -----------------------------
# Input Fields (Customize)
# -----------------------------
st.subheader("📌 Input Features")
gender = st.selectbox("gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("SeniorCitizen", ["Yes" , "No"])
partner = st.selectbox("Partner", ["Yes" , "No"])
Dependents = st.selectbox("Dependents" , ["Yes" , "No"])
tenure = st.number_input("how long (in months) the customer has been a subscriber" , min_value = 0)
phoneService = st.selectbox("Phone Service"  , ["Yes"  , "No"]) 
if phoneService == 'No':
    MultipleLines = 'No phone service'
    MultipleLines = st.selectbox("MultipleLines" , ['No phone service'] , disabled = True)
else:
    MultipleLines = st.selectbox("Multiple Lines" , ["Yes" , "No"])
InternetService = st.selectbox("Internet Service" , ["DSL" , "Fiber optic" , "No"])
if InternetService == 'No':
    OnlineSecurity = OnlineBackup = DeviceProtection = TechSupport = StreamingTV = StreamingMovies = 'No internet servive'
    OnlineSecurity = st.selectbox("OnlineSecurity" , ['No internet service'] , disabled = True)
    OnlineBackup = st.selectbox("OnlineBackup" , ['No internet service'] , disabled = True) 
    DeviceProtection =st.selectbox("DeviceProtection" , ['No internet service'] , disabled = True) 
    TechSupport = st.selectbox("TechSupport" , ['No internet service'] , disabled = True) 
    StreamingTV =  st.selectbox("StreamingTV" , ['No internet service'] , disabled = True) 
    StreamingMovies  = st.selectbox("StreamingMovies" , ['No internet service'] , disabled = True)
else:
    OnlineSecurity = st.selectbox("Online Security" , ["Yes" , "No"])
    OnlineBackup = st.selectbox("Online Backup" , ["Yes" , "No"])
    DeviceProtection = st.selectbox("Device Protection" , ["Yes" , "No"])
    TechSupport = st.selectbox("Tech Support" , ["Yes" , "No"])
    StreamingTV = st.selectbox("Streaming TV" , ["Yes" , "No"])
    StreamingMovies = st.selectbox("Streaming Movies" , ["Yes" , "No"])
Contract = st.selectbox("Contract" , ["Month-to-month" , "One year" , "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing" , ["Yes" , "No"])
PaymentMethod = st.selectbox("Payment Method" , ["Electronic check" , "Mailed check" , "Bank transfer (automatic)" , "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges" , min_value = 0)
TotalCharges = st.number_input("Total Charges" , min_value = 0)

# -----------------------------
# Convert Inputs
# -----------------------------
SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0
data = {
    "gender":gender , "SeniorCitizen":SeniorCitizen , "Partner":partner , 
    "Dependents":Dependents , "tenure":tenure , "PhoneService":phoneService , 
    "MultipleLines":MultipleLines , "InternetService":InternetService , "OnlineSecurity":OnlineSecurity , 
    "OnlineBackup":OnlineBackup , "DeviceProtection":DeviceProtection , "TechSupport":TechSupport , 
    "StreamingTV":StreamingTV , "StreamingMovies":StreamingMovies , "Contract":Contract ,
    "PaperlessBilling":PaperlessBilling , "PaymentMethod":PaymentMethod , "MonthlyCharges":MonthlyCharges ,
    "TotalCharges":TotalCharges
}
# Prediction
# -----------------------------
if st.button("🔮 Predict"):
    prediction =  Predictor(data)
    if prediction == "Churn":
        st.error("🔴 Customer will churn")
    else:
        st.success("✅ Customer will not churn")
