# %% [markdown]
# # Track phone number using Python

# %%
%pip install phonenumbers

# %%
import phonenumbers

# Import geocoder
from phonenumbers import geocoder

# specify then phone number
a = input("Enter the Phone Number: ")
phonenumber = phonenumbers.parse(a)

# Display the location of phone number
print(geocoder.description_for_number(phonenumber, "en"))


