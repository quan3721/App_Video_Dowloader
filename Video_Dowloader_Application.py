# ------- Build a video downloader -------- #

# -- Import libraries -- #
from tkinter import *
from tkinter import filedialog # -- can save file on local directories on your computer
from pytube import YouTube
from moviepy.editor import *
import shutil

# -- Create some functions -- #
def get_path():
    path = filedialog.askdirectory() # -- path of local directories
    path_label.config(text=path) # -- fix content of label into path

def download():
    video_path = url_entry.get() # -- get path of video from entry
    file_path = path_label.cget('text') # -- get path of local directories for downloading
    print("Downloading...........")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download() # download video on Youtube base on URL, streams : download with high quality, get_highest_resolutiom : combine with audio
    video_clip = VideoFileClip(mp4)
    # video_clip.close()

    # ----- code for mp3 ------------ #
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', file_path)
    # ------------------------------- #

    shutil.move(mp4, file_path) # move video to the path
    print('Download Complete')

# -- Create a new window -- #
root = Tk()

# -- Create title for app -- #
root.title('Video Downloader')

# -- Create a canvas -- #
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# -- Create label for app -- #
app_label = Label(root, text="Video Dowloader", fg='blue', font=('Arial', 20))
canvas.create_window(200, 20, window=app_label) # the position of label

# -- Create an entry to entering data intput -- #
url_label = Label(root, text="Enter video URL") # -- label for entry
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# -- Create a button to browse path of local directories to download -- #
path_label = Label(root, text="Select path to download") # -- label for button
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 145, window=path_label)
canvas.create_window(200, 170, window=path_button)

# -- Create a button for downloading -- #
download_button = Button(root, text="Download", command=download)
canvas.create_window(200, 250, window=download_button)


# -- Create a loop to show the window -- #
root.mainloop()