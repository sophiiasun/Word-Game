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

threeHearts = "https://i.ibb.co/qrkbDGT/Drawing-1.png"
twoHearts = "https://i.ibb.co/j6t62c5/Drawing-2.png"
oneHeart = "https://i.ibb.co/d02Q6Nw/Drawing-3.png"
die = "https://i.ibb.co/h9gYVLq/Drawing-4.png"
urllib.request.urlretrieve(threeHearts, "threeHearts.png")
urllib.request.urlretrieve(twoHearts, "twoHearts.png")
urllib.request.urlretrieve(oneHeart, "oneHeart.png")
urllib.request.urlretrieve(die, "die.png")


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

# ========================================================== GUI INTERFACE ==========================================================

title = Label(window, width=35, text="Wurd Game", font="Courier 80 bold", bg="seashell")
description = Label(window, width=107, text="HOW TO PLAY: A prompt will appear on your screen. \
Think of a word with those letters (consecutively) in them and \ntype it in the text box on your side of the screen before \n \
    the timer runs out! \n\
    Each player gets three lives. Win by being the only player remaining or by using all the letters on the left. Have fun!",\
    font="Courier 25", bg="seashell")
img = displayLives(3)
p1Label = Label(window, width=180, image=img, anchor="center")
p2Label = Label(window, width=180, image=img, anchor="center")

title.grid(row=1, column=1, columnspan=3)
description.grid(row=2, column=1, columnspan=3)
p1Label.grid(row=3, column=1)
p2Label.grid(row=3, column=3)

window.mainloop()

