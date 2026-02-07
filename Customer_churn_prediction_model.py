import joblib
import pandas as pd
Model = joblib.load(r"D:\ML Projects\Customer Churn Prediction model(GNB).joblib")
def Predictor(data):
    input_df = pd.DataFrame([data])
    prediction = Model.predict(input_df)
    if prediction[0] == 0:
        return "Not churn"
    else:
        return "Churn"
data = {
    "gender": 'Female', 
    'SeniorCitizen':0	 , 'Partner':'Yes' 	 , 'Dependents':'No' , 	'tenure':1 , 	'PhoneService':'No phone service' , 	'MultipleLines':'DSL' , 	'InternetService':'No' , 	'OnlineSecurity':'No' , 	'OnlineBackup':'No' ,	'DeviceProtection':'No' , 	'TechSupport':'No'	,'StreamingTV':'No' , 	'StreamingMovies':'No' , 'Contract':'Month-to-month' , 'PaperlessBilling':'Yes' , 'PaymentMethod':'Electronic check' , 'MonthlyCharges':24.80 , 'TotalCharges':24.80
}
print("Model loaded successfully..")
print(Predictor(data))