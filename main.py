# functions to run wurd game
# todo:
# generate 2 letters (possible to make a word with)
# scoring : 3 lives, rotate players each time someone is unable to get wurd they lose life
# time : start with 10s, reduce by 0.25s each round
#      if both at 0s it is a tie (higher lives wins?)


# logic / rules :
# if all letters of alphabet are used then player gains a life
# if player runs out of time player loses life
# can't reuse words
# 10 attempts
# if player has no life they cannot do anything
# if all other players have no life you win
# if all players fail a prompt, the prompt changes
import time
from threading import Thread
import enchant
import random
from random_word import RandomWords
from tkinter import *

d = enchant.Dict("en_US")
r = RandomWords()
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class player:
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.letters = [False] * 26
        self.used = []
        self.score = 0
        self.inc = 10
        self.highScore = 0

    def wordExist(self, letters, word):
        if letters in word:
            if (word in self.used) == False:
                return d.check(word)
            return False
        return False

    def useWord(self, word):
        word = word.lower()
        self.used.append(word)
        self.score += 1
        if(self.inc>=3.2):
            self.inc-=0.2
        if(word.isalpha()==False):
            return
        for character in range(0, len(word)):
            self.letters[ord(word[character]) - 97] = True
        self.checkAllLetters()

    def checkAllLetters(self):
        for idx in range(0, 26):
            if self.letters[idx] == False:
                return False
        return True

def generateLetters():
    rword = r.get_random_word()
    while(rword is None or len(rword) <= 1 or rword.isalpha() == False):
        rword = r.get_random_word()
    idx = random.randint(0, len(rword)-2)
    return str(rword[idx] + rword[idx+1])

class LetterBoxes:
    def __init__(self, window):
        self.cvs = Canvas(window, width=70, height=550, bg="SlateGray2")
        self.pos = [[0, 0]] * 26

    def drawRect(self, x, y, colour):
        self.cvs.create_rectangle(x, y, x + 25, y + 25, fill = colour)

    def drawText(self, x, y, txt):
        self.cvs.create_text(x, y, text=txt, font="Courier 21")

    def drawBoxes(self):
        counter = 0
        for y in range(10, 540, 30):
            self.drawRect(10, y, "SlateGray1")
            self.drawText(22, y+12, LETTERS[counter])
            self.pos[counter] = [10, y]
            counter += 1
        for y in range(10, 250, 30):
            self.drawRect(40, y, "SlateGray1")
            self.drawText(52, y+12, LETTERS[counter])
            self.pos[counter] = [40, y]
            counter += 1

    def drawUsed(self, letter):
        if(ord(letter)<115):
            y = (ord(letter) - 97)*30 + 10
            self.drawRect(10, y, "SlateGray3")
            self.drawText(22, y+12, letter)
        else:
            y = (ord(letter) - 115) * 30 + 10
            self.drawRect(40, y, "SlateGray3")
            self.drawText(52, y+12, letter)



