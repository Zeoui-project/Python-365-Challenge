# %% [markdown]
# # Scrape Table from Website using Python

# %%
import urllib.request
import pandas as pd

#List of publicly listed ITES companies of India
url = "https://en.wikipedia.org/wiki/List_of_publicly_listed_ITES_companies_of_India"

with urllib.request.urlopen(url) as i:
    html = i.read().decode('utf-8')

data = pd.read_html(html)[0]
print(data.head())
# %%