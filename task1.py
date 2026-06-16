import pandas as pd

# -----------------------------------
# 1. Load Dataset
# -----------------------------------
df = pd.read_csv("netflix_titles.csv")
print(df.duplicated().sum())
