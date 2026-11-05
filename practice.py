import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

df = pd.read_csv("telco.csv")
print(df.head(5)) #display first 5 row 
print(df.shape)
print(df.info())

##finding missing values
print(df.isnull().sum())

#CUSTOMER CHURN ANALYSIS
print(df["Customer Status"].value_counts())
print(df["Churn Label"].value_counts())
print(df["Churn Category"].value_counts())

#checking columns
print(df.columns.tolist())

#Churn rate KPI 
total_customers = df.shape[0]
churned_customers = (df["Churn Label"] == "Yes").sum()
churn_rate = (churned_customers / total_customers) * 100
print(churn_rate)


# MONTHLY CHARGES ANALYSIS
print(df.groupby("Churn Label")["Monthly Charge"].mean())

# MONTHLY CHARGES BY CUSTOMER STATUS
print(df.groupby("Customer Status")["Monthly Charge"].mean())

# Contract -wise Churn Analysis
print(df.groupby("Contract")["Churn Label"].value_counts())

#Contract - wise Churn Rate
contract_churn  = df.groupby("Contract")["Churn Label"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(contract_churn)


#PAYMENTMETHOD  VS CUSTOMER CHURN
print(df.groupby("Payment Method")["Churn Label"].value_counts())
# HIGHEST CHURN COUNT != HIGHEST CHURN RATE

#for fair comparison
## we should to check percentage for each payment method
payment_method = df.groupby("Payment Method")["Churn Label"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(payment_method)

#internet service vs customer churn and rate
internet_service = df.groupby("Internet Service")["Churn Label"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(internet_service)

#Tenure vs Customer Churn
print(df.groupby("Churn Label")["Tenure in Months"].mean())

#Churn Reason Analysis
print(df["Churn Reason"].value_counts().head(10))

#identify the top 5 Churn reason 
churn_reason_percentage = (df["Churn Reason"].value_counts(normalize = True) * 100)
print(churn_reason_percentage.head(5))




#### SQL ####

#connect to SQLite database
connection = sqlite3.connect("telco_churn.db")

#Import dataframe into SQL table
df.to_sql("customers", connection, if_exists="replace", index=False)
print("Data Imported  successfully!")
connection.close()




