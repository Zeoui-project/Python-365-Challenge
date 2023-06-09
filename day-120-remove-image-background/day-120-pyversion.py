# %% [markdown]
# # Remove Image Background using Python

# %%
%pip install rembg

# %%
from rembg import remove
from PIL import Image
input_path = 'test.jpg'
output_path = 'no-bg-test.jpg'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)