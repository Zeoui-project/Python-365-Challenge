# %% [markdown]
# # Cloud Sharing using Python

# %%
%pip install gofile

# %%
# File Storage
import gofile as go
def Store_Files(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
Store_Files("test.jpg")