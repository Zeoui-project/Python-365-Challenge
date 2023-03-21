# %% [markdown]
# # Image to Pencil Sketch in Python

# %%
import cv2

# Specify the path to image
image1 = cv2.imread('python.png')
window_name = 'Original Image'

# Displaying the original image
cv2.imshow(window_name, image1)

# Convert the image from one color space to another
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

# Image smoothing
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Save the converted image to specified path
cv2.imwrite('sketch.png', sketch)

# Reading an image in default mode
image2 = cv2.imread('sketch.png')

# Window name in which image is displayed
window_name = 'Sketch Image'

# Displaying the sketch image
cv2.imshow(window_name, image2)

# Waits for user to press any key
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()



# %%
