# %% [markdown]
# # Remove Punctuations From a String

# %%
# Define Punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter Your String : ")

# To take input from the user
# my_str = input("Enter a string: ")

# Remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# Display the unpunctuated string
print(no_punct)


