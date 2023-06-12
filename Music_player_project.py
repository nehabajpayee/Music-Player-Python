from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk
import os

mixer.init()

directory_path = "C:/Users/nehab/Music"

def previous_song():
    prev = songs_list.curselection()
    prev = prev[0]-1
    temp = songs_list.get(prev)
    songpath = os.path.join(directory_path,temp)
    mixer.music.load(songpath)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(prev)
    songs_list.selection_set(prev)
    current_song_label.config(text="Currently Playing:  " + temp)

def addmusic():
    temp_song=filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 Files",".mp3"),))
    
    if temp_song:
         directory_path = os.path.dirname(temp_song[0])
    
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        song = os.path.basename(s)
        songs_list.insert(END,song)

def removesong():
    selected_song = songs_list.curselection()
    if selected_song:
            songs_list.delete(int(selected_song[0]))

def play():
    songname = songs_list.get(ACTIVE)
    songpath = os.path.join(directory_path,songname)
    mixer.music.load(songpath)
    mixer.music.play()
    current_song_label.config(text="Currently Playing: " + songname)
  
def pause():
     mixer.music.pause()
     
def resume():
    mixer.music.unpause()
    
def next_song():
    nextsong = songs_list.curselection()
    nextsong = nextsong[0]+1
    temp = songs_list.get(nextsong)
    songpath = os.path.join(directory_path,temp)
    mixer.music.load(songpath)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(nextsong)
    songs_list.selection_set(nextsong)
    current_song_label.config(text="Currently Playing:  " + temp)

window = Tk()
window.geometry("600x500+290+10")
window.title("Music Player using Python (c) Neha Bajpayee")
window.configure(background="black")

menu = Menu(window)
window.config(menu=menu)

select_menu = Menu(menu)
select_menu.add_command(label="Add songs", command=addmusic)
select_menu.add_command(label="Remove song", command=removesong)
menu.add_cascade(label="Menu", menu=select_menu)

listbox_frame = Frame(window, bg="black")
listbox_frame.pack(side=TOP, pady=10)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
songs_list = Listbox(listbox_frame, bg="black", fg="white", font=("Times New Roman", 12), selectbackground="#d65170",selectforeground= "black", width=74, yscrollcommand=scrollbar.set)
scrollbar.config(command=songs_list.yview)
scrollbar.pack(side=RIGHT, fill=Y)
songs_list.pack(side=LEFT)

current_song_label = Label(window, text="Currently Playing:    - - - - - - ", bg="orange", fg="black", font=("Arial", 13))
current_song_label.place(x=170, y=250)

image_path = "Music-Player-Python\music.jpg"  
image = Image.open(image_path)
image = image.resize((480, 250), Image.ANTIALIAS)  # Resize the image if needed
photo = ImageTk.PhotoImage(image)
image_label = Label(window, image=photo, bg="black")
image_label.place(x =50,y=280)

prevbutton = Button(window, text="Prev", width=7, height=3, bg = "#C7EA46",command = previous_song)
playbutton = Button(window, text="Play", width=7, height=3,bg = "#C7EA46", command=play)
pausebutton = Button(window, text="Pause", width=7, height=3,bg = "#C7EA46", command=pause)
resumebutton = Button(window, text="Resume", width=7, height=3,bg = "#C7EA46", command=resume)
nextbutton = Button(window, text="Next", width=7, height=3, bg = "#C7EA46",command = next_song)

prevbutton.place(relx=0.3, rely=0.98 ,anchor=S)
playbutton.place(relx=0.4, rely=0.98, anchor=S) 
pausebutton.place(relx=0.5, rely=0.98, anchor=S)
resumebutton.place(relx=0.6, rely=0.98, anchor=S)
nextbutton.place(relx=0.7, rely=0.98, anchor=S)

window.mainloop()




