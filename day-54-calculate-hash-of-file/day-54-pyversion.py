# %% [markdown]
# # Calculate Hash of a File

# %%
import hashlib
BLOCKSIZE = 65536
# Block read size if size is big enough
fileToOpen = 'E:\\Python\\Project-365-Challenge\\day-54-calculate-hash-of-file\\new_doc.txt'
hasher = hashlib.md5()
with open(fileToOpen, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())


