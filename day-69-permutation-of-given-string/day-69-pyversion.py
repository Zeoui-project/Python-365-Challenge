# %% [markdown]
# # Permutation of Given String using Python

# %%
# Function to find permutations of a given string

from itertools import permutations
def allPermutation(str):
    # Get all permuations of string 'ABC'
    permList = permutations(str)

    # Print all permutations
    for perm in list(permList):
        print(''.join(perm))

# Driver program
if __name__ == "__main__":
    str = input("Enter your string : ")
    allPermutation(str)


