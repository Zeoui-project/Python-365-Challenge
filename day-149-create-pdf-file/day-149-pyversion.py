# %% [markdown]
# # Create PDF file from blank using Python

# %%
%pip install reportlab

# %%
from reportlab.pdfgen import canvas

pdf_file = canvas.Canvas("Test.pdf")

# Add text
pdf_file.drawString(72, 720, "Hello World")
pdf_file.drawString(72, 720, "PDF Document")
pdf_file.drawString(72, 720, "Feel free to use!")
pdf_file.drawString(72, 720, "Tested by Zeoui-project")

# Save
pdf_file.save()