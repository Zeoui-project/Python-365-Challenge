# %% [markdown]
# # Extract Text to PDF using Python

# %%
from PyPDF2 import PdfReader

reader = PdfReader("pytest.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)


