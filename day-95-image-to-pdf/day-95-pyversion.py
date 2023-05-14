# %% [markdown]
# # Image to PDF conversion using Python

# %%
from PIL import Image

def Image_Pdf(filename, output):
    images = []

    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all=True, append_images=images[1:])

# Image path, output pdf
Image_Pdf(["mirror.png",  "photo.png"], "output.pdf")


