# %% [markdown]
# # Empty Recycle Bin using Python

# %%
%pip install winshell

# %%
import winshell
try:
    winshell.recycle_bin().empty(confirm=False,
                                 show_progress=True, sound=True)
    print("Recycle bin is emptied Now")
except:
    print("Recycle bin already empty")