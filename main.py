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

import enchant
from random_word import RandomWords

d = enchant.Dict("en_US")
r = RandomWords()

class player:
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.letters = [0] * 26
        self.used = []

    def wordExist(self, letters, word):
        word = word.lower()
        if letters in word:
            if (word in self.used) == False:
                return d.check(word)
            return False
        return False

    def useWord(self, word):
        word = word.lower()
        self.used.append(word)
        for character in range(0, len(word)):
            self.letters[ord(word[character]) - 97] = 1

    def checkAllLetters(self):
        for idx in range(0, 24):
            if self.letters[idx] == 0:
                return
        self.lives++




tmp = player("Jeffrey")
tmp.useWord("abcdefghijklmnopqrstuvwxyz")
tmp.checkAllLetters()
print(tmp.lives)

