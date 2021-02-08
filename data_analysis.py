import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('car_data.csv')
print (df)

#generate a report
profile = ProfileReport(df)
profile.to_file(output_file = "car_data_report.html")