# %% [markdown]
# # Get address detail using Python

# Using nominatiom API
geolocator = Nominatim(user_agent="geoapiExcercises")

# Zipcode Input
a = input("Enter the zipcode")
zipcode = a

# Using geocode()
location = geolocator.geocode(zipcode)

# Displaying address details
print("Zipcode:", zipcode)
print("Details of the Zipcode:")
print(location)


