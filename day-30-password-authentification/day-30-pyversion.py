# %% [markdown]
# # Password Authentification using Python

# %%
import getpass
database = {"zeoui": "12345", "guest1": "54321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again :")
        break
print("Verified")


