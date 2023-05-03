# %% [markdown]
# # PDF to DOCS using Python

# %%
from pdf2docx import Converter
pdf_file = 'test.pdf'
docx_file = 'test.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()