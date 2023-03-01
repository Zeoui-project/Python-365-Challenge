# %% [markdown]
# # Dice Roll Simulator

# %%
import random

#range of the dice
min_val = 1
max_val = 6

#command to loop
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dices...")
    print("The Values are :")

    #generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))

    #Asking user to roll the dice again
    #Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices again?")



