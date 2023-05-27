# %% [markdown]
# # Detect Python errors within code

# %%
import re
for i in dir(__builtins__):
    if re.match(r'^[A-Z]', i):
        print(i)