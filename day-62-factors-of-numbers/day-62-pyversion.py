# %% [markdown]
# # Find the Factors of a Number using Python

# %%
# Python program to find the factors of a number
# This function computes the factor of the argument passed
def print_factors(x):
    print("The factors of", x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = int(input("Enter a Number to find the Factors : "))
print_factors(num)


