# %% [markdown]
# # Making QR Code 2nd way using Python

# %%
%pip install qrcode

# %%

import qrcode
from PIL import Image

# Link to the website you want to encode in the QR Code
data = "https://github.com/Zeoui-project"

# Generate the QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
image = qr.make_image(fill="black", back_color="red")

# Save the image
image.save("qr_code.png")
Image.open("qr_code.png")