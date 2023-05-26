# %% [markdown]
# # Fetching PDF words using Python

# %%
%pip install pdfplumber

# %%
import pdfplumber as pdftool
def Fetch_Text(file_path):
    # Extract page by page
    with pdftool.open(file_path) as tool:
        for p_no, page in enumerate(tool.pages, 1):
            print('<--- page no', p_no, '--->')
            data = page.extract_text()
            print(data)
Fetch_Text("test.pdf")


