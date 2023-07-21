# %% [markdown]
# # Get address and zip code using Python

# %%
%pip install geopy

# %%
from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="testingGeoPy")

# Get the city name from the user
place = input("Enter City Name: ")

# Geocode the Location
location = geolocator.geocode(place)

# Print the geolocation details
print(location)