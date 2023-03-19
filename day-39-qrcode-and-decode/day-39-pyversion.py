# %% [markdown]
# # QR Code using Python

# %%
import pyqrcode
import png

link = "https://github.com/Zeoui-project"
qr_code = pyqrcode.create(link)
qr_code.png("github.png", scale=5)

# %% [markdown]
# # Decode a QR Code using Python

# %%
from pyzbar.pyzbar import decode
from PIL import Image
decodeQR = decode(Image.open('github.png'))
print(decodeQR[0].data.decode('ascii'))


