import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Function to select a music file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        play_music(file_path)

# Function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Create GUI elements
open_button = tk.Button(root, text="Open Music File", command=open_file)
play_button = tk.Button(root, text="Play", command=lambda: pygame.mixer.music.unpause())
pause_button = tk.Button(root, text="Pause", command=pygame.mixer.music.pause())
stop_button = tk.Button(root, text="Stop", command=pygame.mixer.music.stop)

open_button.pack()
play_button.pack()
pause_button.pack()
stop_button.pack()

# Start the main loop
root.mainloop()

