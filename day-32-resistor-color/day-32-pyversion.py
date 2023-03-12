# %% [markdown]
# # Resistor Color using Python

# %%
color = ["black", "brown", "red", "orange", "yellow",
         "green", "blue", "purple", "grey", "white"]

n = color.index((input("Enter the 1st color :").lower()))
m = color.index((input("Enter the 2nd color :").lower()))
p = color.index((input("Enter the 3rd color :").lower()))

q = int(((n*10)+(m))*(10**(p)))
z = q/1000
print("\nThe Resister Value Is :")
print(f"{q}Ω and in kiloOhm : {z}kΩ")


