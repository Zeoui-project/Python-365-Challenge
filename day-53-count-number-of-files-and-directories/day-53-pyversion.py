# %% [markdown]
# # Count Number of Files and Directories

# %%
import os

# Path IN which we have to count files and directories
PATH = 'E:\Python\Project-365-Challenge'

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    # print('Looking in: ', root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of Files ', fileCount)
print('Number of Directories ', dirCount)
print('Total : ', (dirCount + fileCount))




