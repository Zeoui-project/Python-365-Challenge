# %% [markdown]
# # Get Zip Code with GeoPy using Python

# %%
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

place = input("Enter City name : ")
location = geolocator.geocode(place)
print(location)