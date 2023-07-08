# %% [markdown]
# # Image Color Extraction using Python

# %%
from PIL import Image
Image.open('test.jpg')

# %%
%pip install scikit-learn

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('test.jpg')
w, h, d = tuple(image.shape)
pixels = np.reshape(image, (w * h, d))

from sklearn.cluster import KMeans
n_colors = 10 # Change this to get or more fewer colors
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(model.cluster_centers_)
plt.imshow([palette])
plt.show()