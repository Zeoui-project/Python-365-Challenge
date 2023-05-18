# %% [markdown]
# # Word Art using Python

# %%
from PIL import Image
Image.open('photo.png')

# %%
import pywhatkit
pywhatkit.image_to_ascii_art('photo.png', 'WordArt')
read_file = open("WordArt.txt", "r")
print(read_file.read())