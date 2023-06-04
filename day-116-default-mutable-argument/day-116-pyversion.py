# %% [markdown]
# # Default Argument using Python

# %%
def func(default_arg=[]):
    default_arg.append("python")
    return default_arg
print(func())
print(func())
print(func())