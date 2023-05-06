# %% [markdown]
# # Program to find edges of a coins using Python

# %%
# The 'skimage' package comes with data built-in that
# you can run computer vision algorithms
from skimage import data, io, filters
image = data.coins()
edges = filters.sobel(image)
io.imshow(edges)



