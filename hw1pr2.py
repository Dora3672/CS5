# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Dora Ding
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2 * x


def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3 * x


def sq(x):
    """Result: sq returns the square of its argument
       Argument x: a number (int or float)
    """
    return x * x


def interp(low, hi, fraction):
    """Result: interp returns the floating-point value that is 'fraction' of the way between 'low' and 'high'
       Argument low: a number (int or float)
       Argument hi: a number (int or float)
       Argument fraction: a number/fraction (float)
    """
    return low + ((hi - low) * fraction)


def checkends(s):
    """Result: returns True if the first character in the argument is the same as the last character. It returns False otherwise
       Argument s: word/phrase/sentence (string)
    """

    if s[0] == s[-1]:
        return True
    
    return False


def has42(d):
    """Result: returns True if the key 42 is in the argument. It returns False otherwise
       Argument d: dictionary
    """

    keys = list(d.keys())

    if 42 in keys:
        return True
    
    return False


def hasKey(k, d):
    """Result: returns True if the key k is in the key of the dictionary d. It returns False otherwise
       Argument k: int/string
       Argument d: dictionary
    """

    keys = list(d.keys())

    if k in keys:
        return True
    
    return False


def flipside(s):
    """Result: returns a string whose first half is s's second half and whose second half is s's first half. 
               If len(s) (the length of s) is odd, the "first half" of s is considered to have one fewer character than the second half.
       Argument s: string
    """

    length = len(s)

    if length % 2 == 0:
        s = s[int(length / 2):] + s[:int(length / 2)]
    else:
        s = s[int((length / 2) - 0.5):] + s[:int((length / 2) - 0.5)]
    
    return s


def convertFromSeconds(s):
    """Result: a list with the corresponding days, hours, minutes and seconds represented in the argument
       Argument s: a number (int)
    """
    days = s // 86400
    s = s % 86400

    hours = s // 3600
    s = s % 3600

    minutes = s // 60
    seconds = s % 60

    return [days, hours, minutes, seconds]