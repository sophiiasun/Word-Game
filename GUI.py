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

threeHeartsUrl = "https://i.ibb.co/qrkbDGT/Drawing-1.png"
twoHeartsUrl = "https://i.ibb.co/j6t62c5/Drawing-2.png"
oneHeartUrl = "https://i.ibb.co/d02Q6Nw/Drawing-3.png"
dieUrl = "https://i.ibb.co/h9gYVLq/Drawing-4.png"
pigUrl = "https://i.ibb.co/pPRbw8q/OinkOink.png"
cowUrl = "https://i.ibb.co/ggg6g8C/MooMoo.png"
beeUrl = "https://i.ibb.co/K0H5J3H/BeeIcon.png"
chickenUrl = "https://i.ibb.co/tHMckNz/BakBak.png"
dogUrl = "https://i.ibb.co/b15XgKd/BarkBark.png"
urllib.request.urlretrieve(threeHeartsUrl, "threeHearts.png")
urllib.request.urlretrieve(twoHeartsUrl, "twoHearts.png")
urllib.request.urlretrieve(oneHeartUrl, "oneHeart.png")
urllib.request.urlretrieve(dieUrl, "die.png")
urllib.request.urlretrieve(pigUrl, "pig.png")
urllib.request.urlretrieve(cowUrl, "cow.png")
urllib.request.urlretrieve(beeUrl, "bee.png")
urllib.request.urlretrieve(chickenUrl, "chicken.png")
urllib.request.urlretrieve(dogUrl, "dog.png")


# ============================================================= METHODS =============================================================

def displayLives(num):
    img = Image.open("die.png")
    if num == 1:
        img = Image.open("oneHeart.png")
    elif num == 2:
        img = Image.open("twoHearts.png")
    elif num == 3:
        img = Image.open("threeHearts.png")
    img1 = img.resize((230, 100))
    img2 = ImageTk.PhotoImage(img1)
    return img2

def displayIcons():
    img = 

# ========================================================== GUI INTERFACE ==========================================================

title = Label(window, width=35, text="Wurd Game", font="Courier 80 bold", bg="seashell")
description = Label(window, width=107, text="HOW TO PLAY: A prompt will appear on your screen. \
Think of a word with those letters (consecutively) in them and \ntype it in the text box on your side of the screen before \n \
    the timer runs out! \n\
    Each player gets three lives. Win by being the only player remaining or by using all the letters on the left. Have fun!",\
    font="Courier 25", bg="seashell")
img = displayLives(3)
p1Lives = Label(window, width=180, image=img, anchor="center")
p2Lives = Label(window, width=180, image=img, anchor="center")
img = displayIcons()
p1Icon = Label(window, width=180, image=img[0], anchor="center")
p2Icon = Label(window, width=180, image=img[1], anchor="center")

title.grid(row=1, column=1, columnspan=3)
description.grid(row=2, column=1, columnspan=3)
p1Lives.grid(row=3, column=1)
p2Lives.grid(row=3, column=3)

window.mainloop()

