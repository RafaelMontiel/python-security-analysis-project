import pandas as pd

# Load the dataset
df = pd.read_csv('datasets/Security_Login_Attempts.csv')

# Detect Users with Multiple Failed Logins
failed_logins = df[df['Status'] == 'Failed']
high_risk_users = failed_logins['User_ID'].value_counts()[failed_logins['User_ID'].value_counts() > 5]

# Print Users with Multiple Failed Logins
print("Users with 5+ failed login attempts:")
print(high_risk_users)
