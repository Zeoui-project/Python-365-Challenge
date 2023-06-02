# %% [markdown]
# # Create Progress Bar with other libary using Python

# %%
%pip install tqdm

# %%
import time
from tqdm import tqdm

import time
for i in tqdm(range(10)):
    time.sleep(1)