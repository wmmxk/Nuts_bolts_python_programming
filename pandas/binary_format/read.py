import pandas as pd

df1 = pd.read_csv("merge_bcp.txt")
print(df1.head())

df2 = pd.read_csv("merge_ascii.txt")
print(df2.head())
