import pandas as pd

df = pd.read_csv('tips.csv', index_col=0)
print(df)