# %% [markdown]
# # Web Browsing using Python

# %%
import webbrowser
Url = input("Enter a url : ")
webbrowser.open(Url)

# Open the page in a new browser window.
webbrowser.open_new('Url')

# Open the page in a new browser tab
webbrowser.open_new_tab('Url')


