import pandas as pd
import descripstats as ds

# read data
url = 'https://raw.githubusercontent.com/Sid-149/Life-Expectancy-Predictor-Comparative-Analysis/main/Notebooks/Life%20Expectancy%20Data.csv'
df = pd.read_csv(url,index_col=False)

# display the descriptive statistic mesures in Pandas DataFrame
print(ds.Describe(df))