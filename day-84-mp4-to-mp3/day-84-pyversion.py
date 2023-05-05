# %% [markdown]
# # Convert MP4 to MP3 using Python

# %%
from moviepy.editor import *

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

VIDEO_FILE_PATH = "hehe/bapak-kau-lah.mp4"
AUDIO_FILE_PATH = "hehe/bapak-kau-lah.mp3"

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)