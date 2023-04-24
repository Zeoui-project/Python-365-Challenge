# %% [markdown]
# # Generate Image Captcha using Python

# %%
from captcha.image import ImageCaptcha
# Specify the image size
image = ImageCaptcha(width = 300, height = 100)
# Specify the text to be displayed
captcha_text = input("Enter Captcha text :")
# Generate the image of the given text
data = image.generate(captcha_text)
# Write the image on the given file and save it
image.write(captcha_text, 'E:\Python\Project-365-Challenge\day-76-generate-image-captcha\CAPTCHA.png')
from PIL import Image
Image.open('E:\Python\Project-365-Challenge\day-76-generate-image-captcha\CAPTCHA.png')



# %%
