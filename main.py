import pandas as pd

try:
    df = pd.read_csv('v:\Projects\Customer-Churn-Prediction\WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print("DataFrame loaded successfully.")

except FileNotFoundError:
    print("Error file not found. Please check the file path.")
    exit()

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())