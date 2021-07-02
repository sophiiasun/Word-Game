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
window.config(padx=10, pady=10)


# ========================================================== GUI INTERFACE ==========================================================

title = Label(window, width=35, text="Wurd Game", font="Courier 40 bold", bg="seashell")
description = Label(window, width=138, text="HOW TO PLAY: A prompt will appear on your screen. \n \
    Think of a word with those letters (consecutively) in them and type it in the text box on your side of the screen before the timer runs out! \n\
    Each player gets three lives. Win by being the only player remaining or by using all the letters on the left. Have fun!", font="Courier 10", bg="seashell")

threeHearts = "https://i.ibb.co/qrkbDGT/Drawing-1.png"
twoHearts = "https://i.ibb.co/j6t62c5/Drawing-2.png"
oneHeart = "https://i.ibb.co/d02Q6Nw/Drawing-3.png"
die = "https://i.ibb.co/h9gYVLq/Drawing-4.png"

# u = urllib.urlopen(threeHearts)
# raw_data = u.read()
# u.close()
# b64_data = base64.encodestring(raw_data)
# img = ImageTk.PhotoImage(Image.open(twoHearts))
urllib.request.urlretrieve(threeHearts, "threeHearts.png")
urllib.request.urlretrieve(twoHearts, "twoHearts.png")
urllib.request.urlretrieve(oneHeart, "oneHeart.png")
urllib.request.urlretrieve(die, "die.png")
img1 = Image.open("twoHearts.png")
img2 = img1.resize((230, 100))

img = ImageTk.PhotoImage(img2)

p1Label = Label(window, width=1000, image=img)
p1Label.grid(row=3, column =1, columnspan = 100, rowspan = 100)

title.grid(row=1, column=1, columnspan=3)
description.grid(row=2, column=1, columnspan=3)

window.mainloop()

