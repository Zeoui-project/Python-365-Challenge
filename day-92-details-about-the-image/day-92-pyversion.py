# %% [markdown]
# # Details about the Image using Python

# %%
from PIL import Image
Image.open('photo.png')

# %%
img = Image.open('photo.png')
# The file format of the source file.
print(img.format) #Output: PNG

print(img.mode) #Output: RGB

print(img.size) #Output: size

print(img.palette)


