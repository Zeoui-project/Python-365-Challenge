# %% [markdown]
# # Language Detection using Python

# %%
%pip install langid

# %%
import langid
def detect_language(text):
    return langid.classify(text)[0]
text = input("Enter in any Language : ")
print(detect_language(text))