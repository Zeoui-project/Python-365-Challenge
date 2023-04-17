# %% [markdown]
# # Program to Find compound interest

# %%
# Python program to find compound interest

def compound_interest(principle, rate, time):
    # Calculate compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)

P = float(input("Enter Principle Value : "))
R = float (input("Enter Rate Value : "))
T = float(input("Enter Time Value : "))
compound_interest(P,R,T)


