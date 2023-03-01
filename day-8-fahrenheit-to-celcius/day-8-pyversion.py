# %% [markdown]
# # Fahrenheit to Celcius Python

# %%
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
celcius = input("Enter Values in Fahrenheit : ")
convert(celcius)


