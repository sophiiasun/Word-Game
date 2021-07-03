# functions to run wurd game
# todo:
# generate 2 letters (possible to make a word with)
# scoring : 3 lives, rotate players each time someone is unable to get wurd they lose life

import enchant

d = enchant.Dict("en_US")

word = input("test: ")
letters = "as"
if letters in word:
    if d.check(word):
        print("true")
    else:
        print("false")
else:
    print("false")


class player:
    def __init__(self, name):
        self.lives = 3
        self.name = name

    def wordExist(self, letters, word):
        if letters in word:
            return d.check(word)
        return False
        
            
