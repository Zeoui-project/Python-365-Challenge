# %% [markdown]
# # Country Info using Python

# %%
from countryinfo import CountryInfo
count = input("Entery your country : ")
country = CountryInfo(count)
print("Capital is : ", country.capital())
print("Currencies is : ", country.currencies())
print("Language is : ", country.languages())
print("Borders are : ", country.borders())
print("Other names : ", country.alt_spellings())


