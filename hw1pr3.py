# CS5, hw1pr3
# Filename: hw1pr3.py
#
# Name: Dora Ding
# Problem description: Function Frenzy!
#

def mult(n, m):
    """mult returns the product of its two arguments
       Arguments: n and m are both integers
       Return value: the result of multiplying n and m
    """
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return m if n == 1 else n
    elif m > 0:
        return n + mult(n, m - 1)
    else:
        return -mult(n, -m)

# Tests (mult)
print("mult")
print( "mult(6, 7)           should be  42 :",  mult(6, 7) )
print( "mult(6, -7)          should be  -42 :",  mult(6, -7) )
print( "mult(-6, 7)          should be  -42 :",  mult(-6, 7) )
print( "mult(-6, -7)         should be  42 :",  mult(-6, -7) )
print( "mult(6, 0)           should be  0 :",  mult(6, 0) )
print( "mult(0, 7)           should be  0 :",  mult(0, 7) )
print( "mult(0, 0)           should be  0 :",  mult(0, 0) )



def dot(L, K):
    """dot returns the dot product of the lists L and K.
       Arguments: L and K are lists
       Return value: the dot product of L and K
    """

    if len(L) != len(K) or len(L) == 0 or len(K) == 0:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])
    
# Tests (dot)
print("\ndot")
print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )



def ind(e, L):
    """ind returns the index of the to find element e in the list L or the length if not present
       Arguments: L is either string or lsit, e is either an element 
       Return value: the index of e in L or if it is not included, len(L)
    """

    if len(L) == 0 or e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])
    
# Tests (ind)
print("\nind")
print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(55, [55, 77, 42, 12, 42, 100]) should be  0 :",  ind(55, [55, 77, 42, 12, 42, 100]) )
print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration') )



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
    
# Tests
print("\nletterScore")
print( "letterScore('h') should be  4 :",  letterScore('h') )
print( "letterScore('c') should be  3 :",  letterScore('c') )
print( "letterScore('a') should be  1 :",  letterScore('a') )
print( "letterScore('z') should be 10 :",  letterScore('z') )
print( "letterScore('^') should be  0 :",  letterScore('^') )



def scrabbleScore(S):
    """scrabbleScore returns the scrabble point value of the string S
       Arguments: S is a string
       Return value: the scrabble point value of the string S
    """

    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])

# Tests
print("\nscrabbleScore")
print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )



def transcribe(S):
    """transcribe returns the messenger RNA that would be produced from that string S
       Arguments: S is a string
       Return value: the messenger RNA that would be produced from that string S
    """

    conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }

    keys = conversion.keys()

    if len(S)!= 0:
        if S[0] in keys:
            return conversion[S[0]] + transcribe(S[1:])
        else:
            return transcribe(S[1:])
    return ''

# Tests
print("\ntranscribe")
print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!

# assert statements!  See below for details...
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'   # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that non-DNA other characters disappear
assert transcribe('')         == ''



def pigletLatin(s):
    """pigletLatin returns the translation of s to "piglet latin"
       Arguments: s is single word string with only lowercase letters
       Return value: the translation of s to "piglet latin"
    """

    if len(s) == 0:
        return ''
    elif s[0] in 'aeiou':
        return s + 'way'
    else:
        if len(s) !=1:
            return s[1:] + s[0] + 'ay'
        else:
            return s + 'ay'
    
# Tests
print("\npigeletLatin")
print( "pigletLatin('string')    should be  'tringsay'   :",  pigletLatin('string') )
print( "pigletLatin('apple')     should be  'appleway'   :",  pigletLatin('apple') )
assert pigletLatin('yoohoo')    ==  'oohooyay'  
assert pigletLatin('yttrium')   ==  'ttriumyay' 
assert pigletLatin('stymie')    == 'tymiesay'  



def pigLatin(s):
    """pigLatin returns the translation of s to "pig latin"
       Arguments: s is single word string with only lowercase letters
       Return value: the translation of s to "pig latin"
    """

    if len(s) == 0:
        return ''
    elif s[0] in 'aeiou' or (s[0] in 'y' and s[1] not in 'aeiou'):
        return s + 'way'
    else:
        if s[1] not in 'aeiou':
            return pigLatin(s[1:] + s[0])
        else:
            return s[1:] + s[0] +'ay'
    
# Tests
print("\npigLatin")
print( "pigLatin('string')             should be  'ingstray'   :",  pigLatin('string') )
print( "pigLatin('apple')              should be  'appleway'   :",  pigLatin('apple') )
print( "pigLatin('yttrium')            should be  'yttriumway' :",  pigLatin('yttrium') )
print( "pigLatin('yoohoo')             should be  'oohooyay'   :",  pigLatin('yoohoo') )
print( "pigLatin('stymie')             should be  'ymiestay'   :",  pigLatin('stymie') )
