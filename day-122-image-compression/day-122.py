# %% [markdown]
# # Image Compression using Python

# %%
import PIL
from PIL import Image
from tkinter.filedialog import *
fl = askopenfilenames()
img = Image.open(fl[0])
img.save("test.jpg", "JPEG", optimize=True, quality=10)
Image.open('test.jpg')