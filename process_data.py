import pandas as pd

# Load the dataset
df = pd.read_csv('mock_leads_data.csv')

# Calculate basic statistics for the Business Analyst report
top_performers = df[df['conversion_rate'] > 0.10]

print("High Conversion Leads:")
print(top_performers)

# Calculate total opportunity value
total_value = df['opportunity_value'].sum()
print(f"\nTotal Pipeline Value: ${total_value}")
