#
# hw9pr1.py - Game of Life lab (Conway)
#
# Name: Dora Ding
#

import random
from copy import deepcopy

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You might use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A


def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:                # row is the whole row
        for col in row:          # col is the individual element
            print(col, end = '') # Print that element
        print()


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A


def innerCells(w, h):
    """
    accepts the width and height of the board
    returns a 2D array that has all live cells—with a value of 1—except for a one-cell-wide border of empty cells (with a value of 0) around the edge of the 2D array.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1

    return A


def randomCells(w, h):
    """
    accepts the width and height of the board
    returns an array of randomly-assigned 1's and 0's except that the outer edge of the array is still completely empty (all 0's) as in the case of innerCells
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0, 1])

    return A


def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    newA = deepcopy(A)

    return newA


def innerReverse(A):
    """
    accepts a board
    returns a new generation newA of the same shape and size but the new generation should be the "opposite" of A's cells everywhere except on the outer edge.
    """
    w = len(A[0])
    h = len(A)
    newA = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            newA[row][col] = 1 if A[row][col] == 0 else 0

    return newA



#
# +++ Helper functions for when Life has been completed! +++
#

"""
These allow for "terminal-graphics animation"

Once next_life_generation is complete, run

   lifedemo()

You may need to adjust your terminal's shape/size to 
    create a smooth animation.

"""

import sys

def printBoard_with_d( A, d = None ):
    """ this function prints the 2d list-of-lists A
        using the dictionary d 
    """
    if (d == None) or (0 not in d) or (1 not in d): # can we use d?
        for row in A:
            for col in row:
                sys.stdout.write( str(col) )     # use raw contents
            sys.stdout.write( '\n' )
    else:
        for row in A:
            for col in row:
                sys.stdout.write( str(d[col]) )  # lookup each value
            sys.stdout.write( '\n' )

def placeGlider(row,col,A):
    """ creates a glider with a bounding box
        whose upper-left corner is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+1], [+1,+2], [+2,+0], [+2,+1], [+2,+2] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

def placeAirDancer(row,col,A):
    """ creates an up-down air dancer with top location
        (upper-left corner) is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+0], [+1,+0], [+2,+0] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

import time

def lifedemo():
    """ ASCII demo! 
    """
    W = 42; H = 21          # alter to suit!
    
    A = createBoard(W, H)    # empty grid
    placeGlider(2, 2, A)
    placeAirDancer(2, 20, A)
    placeAirDancer(3, 36, A)

    # A = randomCells(W,H)   # random grid
    
    # dictionaries to indicate what to print
    # d = { 0: 0,    1: 1 }
    # d = { 0: 0,    1: " " }
    # d = { 0: " ",  1: "0" }
    # d = { 0: " ",  1: "#" }
    # d = { 0: "▯", 1: "▮" }
    d = { 0: " ",  1: "🙂" } 


    while True:
        print("\n")

        
        printBoard_with_d(A, d)
        print("\n")
        A = next_life_generation(A)
        time.sleep(0.42)

    
# the terminal colors don't seem as successful
# d = { 0: "\033[6;36;47m0\033[0m", 1: "\033[6;37;40m1\033[0m" }
# www.cs.hmc.edu/twiki/bin/view/CS5/TerminalColorsInPython


#
# +++ end of helper functions +++
#

def countNeighbors(row, col, A):
    """
    accepts the row & col of the current tile and the board
    return the number of live neighbors for a cell in the board A at a particular row and col.
    """
    n = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if not (r == row and c == col):
                n += 1 if A[r][c] == 1 else 0
                
    return n


def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    w = len(A[0])
    h = len(A)
    newA = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if A[row][col] == 1:
                newA[row][col] = 0 if (countNeighbors(row,col,A)<2 or countNeighbors(row,col,A) >3) else 1
            else:
                newA[row][col] = 1 if countNeighbors(row,col,A) == 3 else 0

    return newA