# %% [markdown]
# # Email Slicer using Python

# %%
# Ask to enter any email
email = input("Enter Your Email: ")

# Remove any unnecessary white spaces
email = email.strip()

# Get the index of @
slicer_index = email.index("@")

# fetch the user name by string slicing
username = email[:slicer_index]

# fetch the domain name by string slicing
domain_name =  email[slicer_index+1:]

# Print the result separately
print("Your user name is ", username, " and your domain is ", domain_name)


