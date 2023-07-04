# %% [markdown]
# # Joy Plot Graph using Python

# %%
%pip install joypy

# %%
import joypy
import pandas as pd
from matplotlib import pyplot as plt

# Create a dataset of random numbers
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Create the joy plot
fig, axes = joypy.joyplot(data, ylim='own')

# Add labels and title
plt.xlabel("Value")
plt.ylabel("Variable")
plt.title("Joy Plot of two Variables")

# Show Figure
plt.show()