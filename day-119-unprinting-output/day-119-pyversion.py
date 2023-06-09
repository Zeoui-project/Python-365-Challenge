# %% [markdown]
# # Unprinting Output using Python

# %%
a = "\033[1A"  #Escape character moves our cursor up by 1 line
b = "\x1b[2K"  #Clears th entire current line
print(a)
print(b)