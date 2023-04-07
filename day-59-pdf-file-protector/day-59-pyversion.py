# %% [markdown]
# # PDF file protection using password

# %%
from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwriter = PdfWriter()
pdf = PdfReader('E:\Python\Project-365-Challenge\day-59-pdf-file-protector\PDF_document.pdf')
for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])
password = getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(password)
with open('E:\Python\Project-365-Challenge\day-59-pdf-file-protector\PDF_document.pdf', 'wb') as f:
    pdfwriter.write(f)

print("Now file is password protected")


