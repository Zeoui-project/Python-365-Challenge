# %% [markdown]
# # Mirroring Image using Python

# %%
from PIL import Image

Image.open('photo.png')

# %%
img = Image.open('photo.png')
Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r'mirror.png')
Image.open('mirror.png')


