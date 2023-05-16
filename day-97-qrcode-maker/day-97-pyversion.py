# %% [markdown]
# # QR Code Maker using Python

# %%
import pyqrcode
from PIL import Image
link = input("Enter anything to generate QR : ")
qr_code = pyqrcode.create(link)
qr_code.png('qr.png', scale=5)
Image.open('qr.png')