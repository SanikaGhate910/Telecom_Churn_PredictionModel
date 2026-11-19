import pandas as pd
def data_ingestion():
 '''
 * Title : Telecom_Churn_Prediction Model
 * Independent Column [X]: 'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
 * Target Column [y]: 'Churn'
 * Problem Statement:
1. To predict the churn rate
2. Use clustering approach to predict and classify the cluster pattern such as {11,12,& 13}
 '''
 df=pd.read_csv(r'C:\Telecom_Churn_PredictionModel\data\raw\churn.csv')
 return df