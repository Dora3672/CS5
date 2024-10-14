# coding: utf-8
# hw0pr2rps.py
# Name: Dora Ding

import random          # imports the library named random

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """

    choices = ['rock', 'paper', 'scissors']   # all possible choices (in order of the latter one can win the previous one)

    user = input("Choose your weapon: ")
    comp = random.choice(choices)
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    # change to index number for comparison
    user = choices.index(user) 
    comp = choices.index(comp) 

    if user > comp or (user == 0 and comp == 2):
        print("Lucky you! You will not be this lucky next time.")
    elif comp > user or (comp == 0 and user == 2):
        print("I guess bad luck. I win! :)")
    else:
        print("Tie, but I still win. Hahaha :)")