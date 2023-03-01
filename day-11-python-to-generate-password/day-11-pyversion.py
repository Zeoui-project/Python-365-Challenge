# %% [markdown]
# # Python Program to Generate Password

# %%
import random

#User input for password length
passlen = int(input("Enter the length of password : "))

#storing letters, numbers and special characters
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#random sampling by joining the length of the password and the variable s
p = "".join(random.sample(s,passlen))
print(p)


