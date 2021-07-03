import random
import time
from tkinter import *
import math
from PIL import ImageTk, Image
import base64
import urllib
import urllib.request
import os

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10, bg="SlateGray1")

LIVES_URL = ["https://i.ibb.co/h9gYVLq/Drawing-4.png", "https://i.ibb.co/d02Q6Nw/Drawing-3.png", "https://i.ibb.co/j6t62c5/Drawing-2.png",\
             "https://i.ibb.co/qrkbDGT/Drawing-1.png"] # Order of lives: 0, 1, 2, 3
LIVES_PNG = ["die.png", "oneHeart.png", "twoHearts.png", "threeHearts.png"]
ICONS_URL = ["https://i.ibb.co/pPRbw8q/OinkOink.png", "https://i.ibb.co/ggg6g8C/MooMoo.png", "https://i.ibb.co/K0H5J3H/BeeIcon.png", \
             "https://i.ibb.co/tHMckNz/BakBak.png", "https://i.ibb.co/b15XgKd/BarkBark.png"]
ICONS_PNG = ["pig.png", "cow.png", "bee.png", "chicken.png", "dog.png"]

# ============================================================= METHODS =============================================================

def requestURLs():
    for idx in range(0, 4):
        urllib.request.urlretrieve(LIVES_URL[idx], LIVES_PNG[idx])
    for idx in range(0, 5):
        urllib.request.urlretrieve(ICONS_URL[idx], ICONS_PNG[idx])
requestURLs()

def displayLives(lives):
    img = Image.open(LIVES_PNG[lives])
    img1 = img.resize((230, 100))
    img2 = ImageTk.PhotoImage(img1)
    return img2

def displayIcons():
    idx1 = random.randint(0, 4)
    idx2 = random.randint(0, 4)
    while idx2 == idx1:
        idx2 = random.randint(0, 4)
    img1_1 = Image.open(ICONS_PNG[idx1])
    img1_2 = img1_1.resize((230, 230))
    img1_3 = ImageTk.PhotoImage(img1_2)
    img2_1 = Image.open(ICONS_PNG[idx2])
    img2_2 = img2_1.resize((230, 230))
    img2_3 = ImageTk.PhotoImage(img2_2)
    return [img1_3, img2_3]

# ========================================================== GUI INTERFACE ==========================================================

title = Label(window, width=35, text="Wurd Game", font="Courier 80 bold", bg="seashell")
subtitle = Label(window, width=50, text="HOW TO PLAY", font="Courier 20 bold", bg="seashell")
description = Label(window, width=107, text="A prompt will appear on your screen. \
Think of a word with those letters (consecutively) in them and \ntype it in the text box on your side of the screen before \
the timer runs out! Each player gets three lives. \n Win by being the only player remaining or by using all the letters\
on the left. Have fun!", font="Courier 25", bg="seashell")
img = displayLives(3)
p1Lives = Label(window, width=180, image=img, bg="SlateGray1", anchor="center")
p2Lives = Label(window, width=180, image=img, bg="SlateGray1", anchor="center")
img2 = displayIcons()
p1Icon = Label(window, width=250, image=img2[0], bg="SlateGray1", anchor="center")
p2Icon = Label(window, width=250, image=img2[1], bg="SlateGray1", anchor="center")

title.grid(row=1, column=1, columnspan=3, padx=(0, 10), pady=(0, 10))
subtitle.grid(row=2, column=1, columnspan=3, padx=(0, 10), pady=(0, 10))
description.grid(row=3, column=1, columnspan=3, padx=(0, 10), pady=(0, 10))
p1Lives.grid(row=4, column=1, padx=(0, 10), pady=(0, 10))
p2Lives.grid(row=4, column=3, padx=(0, 10), pady=(0, 10))
p1Icon.grid(row=5, column=1, padx=(0, 10), pady=(0, 10))
p2Icon.grid(row=5, column=3, padx=(0, 10), pady=(0, 10))



window.mainloop()

