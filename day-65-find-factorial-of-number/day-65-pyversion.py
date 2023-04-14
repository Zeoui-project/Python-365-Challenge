# %% [markdown]
# # Find Factorial of a Number using Python

# %%
# To take input from the user
num = int(input("Enter a number : "))

factorial = 1

# Check if the number is negative, positive or zero

if num < 0:
    print("Sorry, Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of zero is one")
else:
    # Calculate the factorial of the number
    for i in range(1, num + 1):
        #factorial *= i (other way)
        factorial = factorial*i
    print("Factorial of ", num, " is ", factorial)


