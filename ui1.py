from tkinter import *
import tkinter
import pygame
import mixer
from playsound import playsound



root = Tk()
root.title('LAALM foundation')
root.iconbitmap(r'C:\Users\saihr\Documents\project\.vscode\icon.ico')



frametop = Frame(root)
framebottom = Frame(root)
frameleft = Frame(framebottom)
frameright = Frame(framebottom)

pygame.mixer.init()

def play():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

# adding image in the text
def add_image():
    global my_image
    my_image=PhotoImage(file='pic.png')
    position=text.index(INSERT)
    text.image_create(position, image=my_image)
    my_label.config(text=position)

photo= PhotoImage(file='pic.png')
labelphoto= Label(root, image= photo)
labelphoto.pack(side=TOP, fill=BOTH, expand=1)



text = Text(frametop, foreground='white', background='black')

scroll = Scrollbar(frametop, command=text.yview)
play_btn = Button(frameleft, text="▶", command=play)
stop_btn = Button(frameright, text="⏹", command=stop)
image_btn=Button(framebottom,text="add image", command=add_image )



text['yscrollcommand'] = scroll.set

frametop.pack(side=TOP, fill=BOTH, expand=1)
framebottom.pack(side=BOTTOM, fill=BOTH, expand=1)
frameleft.pack(side=LEFT, fill=BOTH, expand=1)
frameright.pack(side=RIGHT, fill=BOTH, expand=1)

text.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
scroll.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)
play_btn.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
stop_btn.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
image_btn.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)


my_label=Label(root, text="")
my_label.pack()




root.mainloop()

