import pandas as pd
import descripstats as ds

# example local DataFrame (stable example for tests and CI)
df = pd.DataFrame({
	"A": [1, 2, 3, 4, 5],
	"B": [10, 20, 30, 40, 50]
})

# display the descriptive statistic measures in Pandas DataFrame
print(ds.Describe(df))