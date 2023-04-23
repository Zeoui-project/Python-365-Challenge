# %% [markdown]
# # Convert Video Files to GIF using Python

# %%
from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("Tjueek.MOV")

videoClip.write_gif("Tjueek.gif")


