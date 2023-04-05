# %% [markdown]
# # Number Guessing game in Python

# %%
import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
# Generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # Taking guessing number as input
    guess = int(input("Guess a number:- "))
    # Condition testing
    if x == guess:
        print("\n\tCongrats! You guessed the number in", count, "guesses!\n")
        break
    elif x > guess:
        print("\n\tYou guessed too small!\n")
    elif x < guess:
        print("\n\tYou guess too high!\n")

# Shows this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")



