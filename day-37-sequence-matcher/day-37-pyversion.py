# %% [markdown]
# # Sequence Matcher using Python

# %%
from difflib import SequenceMatcher
text1 = input("Enter 1st sentence : ")
text2 = input("Enter 2nd sentence : ")
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")


