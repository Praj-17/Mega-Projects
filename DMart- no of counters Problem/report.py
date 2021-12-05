from pandas_profiling import profile_report
import pandas as pd
#Loading the dataset
df = pd.read_csv("dmart_unprocessed.csv")
#Generate a report
profile = profile_report.ProfileReport(df) #minimal == true can be used to reduce the output data stream
profile.to_file(output_file = "dmart_unprocessed.html")