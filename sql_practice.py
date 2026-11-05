import sqlite3
import pandas as pd
#step 1: Connect to SQlite database
connection = sqlite3.connect("telco_churn.db")
#Step 2: Write SQL query
query = """
SELECT "Customer ID", Age, Gender
FROM customers
WHERE "Under 30" = 'Yes' AND Gender = 'Male'
LIMIT 5;
"""
#Step 3: Execute SQL query using pandas
result_df = pd.read_sql_query(query, connection)

#step 4: Display output
print(result_df)

#step 5: Close connection
connection.close()
