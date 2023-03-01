# %% [markdown]
# # Polindrome Words using Python

# %%
def polindrome(sentence):
    for i in (",.'?/<>}{{}}'"):
        sentence = sentence.replace(i, "")
    polindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            polindrome.append(word)
    return polindrome
sentence = input("Enter a sentence : ")
print(polindrome(sentence))


