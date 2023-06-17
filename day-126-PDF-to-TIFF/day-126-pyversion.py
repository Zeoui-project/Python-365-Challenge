# %% [markdown]
# # PDF to TIFF using Python

# %%
%pip install aspose-words

# %%
import aspose.words as aw

# Load the PDF
doc = aw.Document("test.pdf")

# Save the doc
doc.save("test.tiff")