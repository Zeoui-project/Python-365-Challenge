# %% [markdown]
# # Magic Method Invocation using Python

# %%
num = 50
result1 = num + 10
result2 = num.__add__(10)
print(result1)
print(result2)

# %%
num = 50
result1 = num * 10
result2 = num.__mul__(10)
print(result1)
print(result2)

# %%
num = 50
result1 = num - 10
result2 = num.__sub__(10)
print(result1)
print(result2)

# %%
num = 50
result1 = num / 10
result2 = num.__truediv__(10)
print(result1)
print(result2)


