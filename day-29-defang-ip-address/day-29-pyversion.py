# %% [markdown]
# # Defang IP Address using Python

# %%
def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

IPad = input("Enter your IP Address : ")
ipaddress = ip_address(IPad)
print(ipaddress)


