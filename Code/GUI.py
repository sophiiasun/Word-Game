import random
import time
from tkinter import *
import math
from PIL import ImageTk, Image

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10)


# ========================================================== GUI INTERFACE ==========================================================

title = Label(window, width=35, text="Wurd Game", font="Courier 40 bold", bg="seashell")
description = Label(window, width=138, text="HOW TO PLAY: A prompt will appear on your screen. \n \
    Think of a word with those letters (consecutively) in them and type it in the text box on your side of the screen before the timer runs out! \n\
    Each player gets three lives. Win by being the only player remaining or by using all the letters on the left. Have fun!", font="Courier 10", bg="seashell")

# threeHearts = "C:/Users/14168/Documents/GitHub/Word-Game/ThreeHearts.jpeg"
# twoHearts = "C:/Users/14168/Documents/GitHub/Word-Game/TwoHearts.jpeg"
# oneHeart = "C:/Users/14168/Documents/GitHub/Word-Game/OneHeart.jpeg"
# die = "C:/Users/14168/Documents/GitHub/Word-Game/Die.jpeg"
#
# img = ImageTk.PhotoImage(Image.open(threeHearts))
#
# p1Label = Label(window, width=15, image=img)

title.grid(row=1, column=1, columnspan=2)
description.grid(row=2, column=1, columnspan=2)


window.update()
