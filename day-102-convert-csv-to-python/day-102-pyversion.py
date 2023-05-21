# %% [markdown]
# # Convert CSV to Python

# %%
import pandas as pd
import csv, json
data = pd.read_csv("Instagram.csv")
print(data)
print("Converted JSON file below :")
print(json.dumps(list(csv.reader(open('Instagram.csv')))))