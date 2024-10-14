# CS 5 Gold, hw2pr3
# filename: hw2pr3.py
# Name: Dora Ding
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *

# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2 * x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x ** 2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2 * x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x // 2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x / 2 for x in range(N)]

# printing tests
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )   
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) ) 
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) ) 

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]


# Here is where your functions start for the lab:
def unitfracs(N):
    """
        N: the number of sections to divide 1 by
        Return: a list of N evenly-spaced left-hand endpoints (fractions) in the unit interval [0, 1)
    """
    return [x / N for x in range(N)]

def scaledfracs(low, high, N):
    """
        low: the lower bound of the interval
        high: the upper bound of the interval
        N: the number of sections between the interval
        Return: a list of N evenly-spaced left endpoints uniformly through the interval [low, high)
    """
    return [x * (high - low) + low for x in unitfracs(N)]

def sqfracs(low, high, N):
    """
        low: the lower bound of the interval
        high: the upper bound of the interval
        N: the number of sections between the interval
        Return: the list containing the y values (results) of a function at each of these x positions (squared)
    """
    return [x * x for x in scaledfracs(low,high,N)]

def f_of_fracs(f, low, high, N):
    """
        f: function to produce y
        low: the lower bound of the interval
        high: the upper bound of the interval
        N: the number of sections between the interval
        Return: the list containing the y values (results) of a function at each of these x positions 
    """
    return [f(x) for x in scaledfracs(low,high,N)]

def integrate(f, low, high, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit high (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to high
    """

    return sum(f_of_fracs(f, low, high, N)) * (high - low) / N

print( "integrate(dbl, 0, 10, 4) should be 75 :", integrate(dbl, 0, 10, 4) )
print( "integrate(sq, 0, 10, 4) should be 218.75 :", integrate(sq, 0, 10, 4) )




"""Q1. 

In a sentence explain why integrate will always underestimate the correct value of this particular integral.
Intergrate will always underestimate the correct value of this particular integral because y=2x has a positive slope, meaning that when using the left riemann rums (which is how the integral is calculated in the function) will always miss certain area under the line.

As a follow up, what is a function whose integral would always be overestimated on the same interval, from 0 to 10? (If you're not sure about this, answer the next question first.)
y=-x+11

"""

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x ** 2) ** 0.5


"""Q2. 

In [2]: integrate(c, 0, 2, 2)
Out[2]: 3.732050807568877

In [3]: integrate(c, 0, 2, 20)
Out[3]: 3.2284648797549815

As N goes to infinity (i.e., becomes larger and larger), what does the value of this integral become? Why?
As N goes to infinity, the integrate function will return a result closer and closer to pi (3.14) as the function with the x interval draws a quarter of a circle with a radius of 2 and with the smaller and smaller interval, the integrate function will return a result more accurate.

"""