# %% [markdown]
# # Extract Text from Image using Python

# %%
%pip install pytesseract

# %%
%pip install pillow

# %%
from PIL import Image
from pytesseract import pytesseract

# Define path tesseract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image
path_to_image = 'texttoimage.png'

# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)

print(text)


