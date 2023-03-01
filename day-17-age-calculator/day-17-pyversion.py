# %% [markdown]
# # Age Calculator using Python

# %%
#y=year, m=month, d=day
y = int(input("Enter your birth year"))
m = int(input("Enter your birth month"))
d = int(input("Enter your birth day"))

def AgeCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

AgeCalculator(y, m, d)


