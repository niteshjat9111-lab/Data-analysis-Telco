import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#load dataset
df = pd.read_csv("telco.csv")

#count customers by churn status
churn_data = df["Churn Label"].value_counts().reset_index()

#Create interactive bar chart
sns.barplot(
    data = churn_data,
    x='Churn Label',
    y='count',
    color = "pink",  
)

plt.title("Customer Churn Analysis")
plt.xlabel("Churn Label")
plt.ylabel("Counting of Churn Label")
plt.tight_layout()
plt.show()
