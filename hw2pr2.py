# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Dora Ding
# Problem description: Sleepwalking student

import random  
import time
import sys

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])


def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)


def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge

        backstory: You are a young girl that is currently thinking about whether you love your mom or dad more. 
                   You have decided to let your parents stand on either side of the sidewalk and see who you will reach while sleepwalking to determine who you like the most.
                   You also want to know how many steps you have taken to reach one of your parent to see how much "attraction" there is between the two of you.
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "👧" + walkway[S:]  # put our sleepwalker "👧"

    walkway = "👨" + walkway + "👩"              # parents on either side

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        print("You like your", "mom" if start==hi else "dad", "more")
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!
    

def race(o, c, p, low, hi):
        """
            This simulator observes animals, the owl and the chick, trying to get the peanut in the center. The owl should be on the left side and the chick on the right side of the peanut. If any of the animals tocuhes the wall, they lose. 

            o:  the location of the owl (who wanders)
            c:  the location of the chick (who wanders)   
            p:  the location of the peanut
            low: the lowest point (end point)
            hi: the highest point (end point)

            The peanut does not move.
            The endpoints are low and hi.  
            The owl should be on the left side and the chick on the right side of the peanut.
   
            Return: the animal that wins if the inputs are valid or else "Invalid inputs. Please try again"; the number of steps in the race

            Good values to run: race(6,18,12,0,24)   # evenly spaced
                                race(3,18,12,0,24)   # uneven spacing: chick is much closer to 12, the peanut
        """ 

        if low >= hi or p<low or p>hi or o>p or c<p:
            return "Invalid inputs. Please try again!"

        walkway = "_"*(hi-low)            

        walkway = walkway[:(o-low)] + "🦉" + walkway[(o-low):(p-low)] + "🥜" + walkway[(p-low):(c-low)] + "🐥" + walkway[(c-low):]

        walkway = "|" + walkway + "|"             # walls on the side

        print(walkway, "    ", o, c, p, low, hi)   
        time.sleep(0.05)

        if (o==p) or (c==p):            # base case: no steps touching the peanut
            print("Winner:", "owl" if o==p else "chick")
            return 0
        elif (o==low or o==hi) or (c==low or c==hi):            # base case: no steps touching the wall 
            print("Winner:", "chick" if (o==low or o==hi) else "owl")
            return 0
        else:               # takes one step for both animals
            return 1 + race(o+rs(), c+rs(), p, low, hi)            
