# %% [markdown]
# # Text to Handwriting Python

# %%
import pywhatkit as kit
import cv2

Handwritten = input("Enter your text to convert in Handwriting : ")
kit.text_to_handwriting(Handwritten, save_to="pythoncoding.png")
img = cv2.imread("pythoncoding.png")
cv2.imshow("Python Coding", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


