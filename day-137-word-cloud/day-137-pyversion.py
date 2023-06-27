# %% [markdown]
# # Word Cloud using Python

# %%
%pip install wordcloud

# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Open the text file
with open('test137.txt', 'r') as f:
    text = f.read()

# Genereate the word cloud
WordCloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(WordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()