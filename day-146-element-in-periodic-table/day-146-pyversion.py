# %% [markdown]
# # Details of an element by Periodic Table

# %%
%pip install periodictable

# %%
import periodictable

# Get details of an element by atomic number
Atomic_No = int(input("Enter Element Atomic No : "))
element = periodictable.elements[Atomic_No]
print('Atomic Number: ', element.number)
print('Symbol: ', element.symbol)
print('Name: ', element.name)
print('Atomic Mass: ', element.mass)
print('Density: ', element.density)