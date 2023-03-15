# %% [markdown]
# # Remove Cuss Words using Python

# %%
from better_profanity import profanity
text = input("Enter your sentence to check : ")
censored = profanity.censor(text)
print(censored)


