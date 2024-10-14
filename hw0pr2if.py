# coding: utf-8
#
# hw0pr2if.py
# Name: Dora Ding

""" 
Title for your adventure: The homework

Notes on how to "win" or "lose" this adventure:
  To win, finish your work.
  To lose, do not finish your work on time (choose to watch movies in the end and decide to sleep after watching).
"""

import time

def adventure():
    """
       This function runs one session of interactive fiction
       Arguments: no arguments (prompted text doesn't count as an argument)
       Results: no results     (printing doesn't count as a result)
    """

    user_name = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome", user_name, "to this adventure")
    print()

    print("Your task is to finish your homework on time.")
    print()

    print("Today is the last day of your holiday but you have not started any of your work.")
    print("Just as you are wondering where to start, your mother comes in.")
    print("'Did you finish your homework? When are you going to start?' your mom asks.")
    hour = input("How many hours are you going to rest for before you start working: ")

    if hour.isdigit():
        hour = int(hour)
        if hour == 0:
            print("Your mom smiles and says, 'Good kid! Finish your work fast and go to bed. If you need anything, just let me know.'")
        elif 3>hour>0:
            print("Your mom says, 'Sure. Just keep an eye on the time. Don't play too long. You do have a lot of work.'")
        elif 5>hour>2:
            print("Your mom yells, 'Don't play for that long. You can only play for maximum of an hour!'")
        else:
            print("Your mom yells, 'Do you know how much work you have! Start your work right now!'")
    else:
        print("Your mom yells, 'What are you talking about! Start your homework now!'")

    print()
    print("Your mom left.")
    print("You are very obedient to your mom, so you take her words seriously. You will only play for the amount of time your mom agrees with.")
    print()

    if hour == 2:
        print("Two hours have passed.")
        time.sleep(20)
        print()
    elif (5>hour>2 or hour == 1):
        print("An hour has passed.")
        time.sleep(10)
        print()
    
    print("You start working on your homework.")
    time.sleep(20)
    print("There is a lot of homework and you got bored.")
    activity = input("What do you want to do now [homework/play/movies]: ")

    if activity.lower() == "homework":
        time.sleep(10)
        print("Your dedication paid off.")
        print("With just an additional hour, you have completed everything!")
        print("Now you can go back school with pride!")
        print("Good job,", user_name)
    elif activity.lower() == "play":
        print("You stand up and stretches.")
        print("As you start to play, you mom comes in.")
        print("Your mom sees you playing and yells, 'What are you doing!'")
        print("She is very mad at you.")
        print("She yells at you till it is bedtime.")
        time.sleep(30)
        print("You do not want to be embarrassed tomorrow, so you went back to work.")
        time.sleep(10)
        print("You finally finish your work after an hour.")
        print("You are proud of yourself and regret actually wanting to play at the first place.")
        print("But, good job,", user_name)
    else:
        print("You start to look for movies online.")
        print("You find the Barbie movie online and start watching it.")
        time.sleep(20)
        print("You have finished the movie, but as you look up, it is bedtime already.")
        next = input("Do you want to sleep now [yes/no]: ")

        if next.lower() == 'yes':
            print("You are in bed right now.")
            time.sleep(50)
            print("You awake in the morning and you do not have time to finish your work.")
            print("Farewell,", user_name)
            return None

        time.sleep(10)
        print("You are able to finish your work in an hour!")
        print("Now you can go back school with pride!")
        print("Good job,", user_name)

    return None