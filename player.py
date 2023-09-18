import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry("490x700+290+10")
root.configure(background='white')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# Custom button styles
button_style = {
    "font": ("Arial", 12),
    "bg": "#FFFFFF",
    "fg": "white",
    "bd": 0,
    "activebackground": "#555555",
    "compound": "center",
}

# Replace the image file paths with your own
play_image = PhotoImage(file="play.png").subsample(2, 2)
stop_image = PhotoImage(file="stop.png").subsample(2, 2)
pause_image = PhotoImage(file="pause.png").subsample(2, 2)

# icon
lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

frameCnt = 30
# Use subsample to resize the musicplayer.gif
frames = [PhotoImage(file='music1.gif', format='gif -index %i' % i).subsample(2, 2) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=90, y=150)  # Adjust position to center the gif
root.after(0, update, 0)

# Button Play (Smaller)
play_button = Button(root, image=play_image, **button_style, command=PlayMusic, height=40, width=40)
play_button.place(x=215, y=487)

# Button Stop (Smaller)
stop_button = Button(root, image=stop_image, **button_style, command=mixer.music.stop, height=40, width=40)
stop_button.place(x=130, y=487)

# Button Pause (Smaller)
pause_button = Button(root, image=pause_image, **button_style, command=mixer.music.pause, height=40, width=40)
pause_button.place(x=300, y=487)

# Label
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter
root.mainloop()
