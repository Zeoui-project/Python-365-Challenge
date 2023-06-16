# %% [markdown]
# # Convert JPG to PNG using Python

# %%
%pip install pillow

# %%
#PNG to JPG
from PIL import Image
im = Image.open("test.png")
rgb_im = im.convert('RGB')
rgb_im.save('PNGtoJPGtest.jpg')

# %%
#JPG to PNG
im2 = Image.open("test.jpg")
im2.save("JPGtoPNGtest.png")