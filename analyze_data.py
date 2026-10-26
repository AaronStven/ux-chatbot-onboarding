import pandas as pd

# Load the data
df = pd.read_csv('data/usability_metrics.csv')

# Group by Prototype and calculate the averages
summary = df.groupby('Prototype').agg({
    'Task_Success_Time_sec': 'mean',
    'Errors': 'mean',
    'SUS_Score': 'mean',
    'NASA_TLX_Score': 'mean'
}).round(1)

print("--- USABILITY STUDY RESULTS ---")
print(summary)