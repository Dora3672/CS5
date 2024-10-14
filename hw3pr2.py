#
# hw3pr2.py - algorithms and use-it-or-lose-it
#

print("Onward, Algorithms!")

# The NEXT_CHAR dictionary for use in rotc(c)
#
NEXT_CHAR = { "a": "b", "A": "B",
              "b": "c", "B": "C",
              "c": "d", "C": "D",
              "d": "e", "D": "E",
              "e": "f", "E": "F",
              "f": "g", "F": "G",
              "g": "h", "G": "H",
              "h": "i", "H": "I",
              "i": "j", "I": "J",
              "j": "k", "J": "K",
              "k": "l", "K": "L",
              "l": "m", "L": "M",
              "m": "n", "M": "N",
              "n": "o", "N": "O",
              "o": "p", "O": "P",
              "p": "q", "P": "Q",
              "q": "r", "Q": "R",
              "r": "s", "R": "S",
              "s": "t", "S": "T",
              "t": "u", "T": "U",
              "u": "v", "U": "V",
              "v": "w", "V": "W",
              "w": "x", "W": "X",
              "x": "y", "X": "Y",
              "y": "z", "Y": "Z",
              "z": "a", "Z": "A",
}

# The function shift1(c)
def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    


def shiftN(c, N):
    """ rotate 1 character, c, by N place 
        c must be 1 character.
        non-characters don't change
    """
    if N == 0:
        return c
    return shiftN(shift1(c), N - 1)
    
def encipher(s, N):
    """
    s is a string
    N is a non-negative integer between 0 and 25.
    encipher should return a new string in which the letters in s have been "rotated" by N characters forward in the alphabet, wrapping around as needed
    """
    if s == '':
        return ''
    return shiftN(s[0], N) + encipher(s[1:], N)

print("encipher('xyza', 1) == 'yzab'", encipher('xyza', 1))
print("encipher('Z A', 1) == 'A B'", encipher('Z A', 1))

assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'



def letterScore(let):
    """letterScore returns the scrabble point value of the argument
       Arguments: let is a single character string
       Return value: the scrabble point value of the argument
    """

    points = {'aeillnorstu':1, 'dg':2, 'bcmp':3, 'fhvwy':4, 'k':5, 'jx':8, 'qz':10}
    
    keys = points.keys()

    for k in keys:
        if let in k:
            return points[k]
    return 0  # if the argument is not a letter

def scrabbleScore(S):
    """scrabbleScore returns the scrabble point value of the string S
       Arguments: S is a string
       Return value: the scrabble point value of the string S
    """

    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])


def decipher(s):
    """
    decipher accepts a string as the input (ciphered text)
    returns the attempted deciphered text

    strategy:
    - base on the common frequency of the letters
    - calculate the scrabble score for each possible deciphered text
    - the lowerest scrabble score will probably be the deciphered text as scrabble gives frequenct letters low scores and these letters usually appear in words/sentences
    """
    scores = [[scrabbleScore(encipher(s, x)),encipher(s, x)] for x in range(0, 26)]
    return min(scores)[1]



def blsort(L):
    """
    accept a list L (binary list)
    return a list with the same elements as L, but in ascending order
    """
    return L.count(0) * [0] + L.count(1) * [1]



def gensort(L):
    """
    accepts a list L
    returns a list with the same elements as L, but in ascending order.
    """
    if all(L[i] == min(L) for i in range(len(L))):
        return L
    return [min(L)] + gensort(L[:L.index(min(L))] + L[L.index(min(L) + 1:])



def jscore(S, T):
    """
    accept two strings, S and T
    returns the "jotto score" of S compared with T.
    """
    if S == "" or T == "":
        return 0
    if S[0] in T:
        return 1 + jscore(S[1:], T.replace(S[0], '', 1))
    return jscore(S[1:], T)
        


def exact_change(target_amount, L):
    """
    target_amount is a single non-negative integer
    L is a list of positive integers 
    return either True or False: it should return True if it's possible to create target_amount by adding up some—or all—of the values in L. It should return False if it's not possible to create target_amount by adding up some or all of the values in L.
    """
    if target_amount == 0:
        return True
    if L != []:
        if exact_change(target_amount - L[0], L[1:]) == True:
            return True
        return exact_change(target_amount, L[1:])
    return False



def LCS(S, T):
    """
    accept two strings, S and T.
    return the longest common subsequence (LCS) that S and T share (a string whose letters are a subsequence of S and a subsequence of T (they must appear in the same order, though not necessarily consecutively, in those argument strings))
    """
    if S == '' or T == '':
        return ''
    if S[0] == T[0]:
        return S[0] + LCS(S[1:], T[1:])
    else:
        without_s = LCS(S[1:], T)
        without_t = LCS(S, T[1:])
        if len(without_s) > len(without_t):
            return without_s
        else:
            return without_t