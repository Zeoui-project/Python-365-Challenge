# %% [markdown]
# # A music player using Python

# %%
%pip install pygame

# %%
import pygame
import tkinter as tk
from tkinter import filedialog
def play_music():
    # Open a file dialog to select the music file
    filename = filedialog.askopenfilename()
    pygame.init()
    pygame.mixer.init
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

# Create a GUI using tkinter
root = tk.Tk()
root.title("Music Player")
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()
root.mainloop()