# CS5, hw4pr2
# Filename: hw4pr2.py
# Name: Dora Ding
# Problem description: Conversions and Compressions

def numToBaseB(N, B):
    """
    arguments are a non-negative integer N and a base B (between 2 and 10 inclusive)
    return a string representing the number N in base B
    """
    if N == 0:
        return ''
    digits = [str(x) for x in range(B)]
    return numToBaseB(N // B,B) + digits[N % B]

assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'



def baseBToNum(S, B):
    """
    accepts as arguments a string S and a base B, where S represents a number in base B, and where B is between 2 and 10 inclusive
    return an integer in base 10 representing the same number as S
    """
    if S == '':
        return 0
    return B * baseBToNum(S[:-1], B) + int(S[-1]) % B

assert baseBToNum('5733', 9) == 4242
assert baseBToNum('1474462', 8) == 424242
assert baseBToNum('222', 4) == 42
assert baseBToNum("101010", 3) == 273
assert baseBToNum("", 10) == 0             



def  baseToBase(B1, B2, s_in_B1):
    """
    takes three arguments: a base B1, a base B2 (both of which are between 2 and 10, inclusive) and s_in_B1, which is a string representing a number in base B1
    return a string representing the same number in base B2.
    """
    return numToBaseB(baseBToNum(s_in_B1, B1), B2)

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'



def add(S, T):
    """
    takes two binary strings S and T
    returns their sum, also in binary
    """
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

assert add('11', '100') == '111'
assert add("11100", "11110") == '111010'
assert add('110','11') == '1001'
assert add('110101010','11111111') == '1010101001'
assert add('1','1') == '10'



def addB(S, T):
    """
    takes two binary strings S and T
    returns their sum, also in binary
    """
    if S == '' or T == '':
        return T if S=='' else S
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'   # 0 + 0 == 0
    if S[-1] == '1' and T[-1] == '0' or  S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'   # 0 + 1 == 1
    if S[-1] == '1' and T[-1] == '1':
        carry = addB(S[:-1], '1') 
        return addB(carry, T[:-1]) + '0'
    
assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'



def compress(S):
    """
    argument is a binary string S of length less than or equal to 64
    returns another binary string as its result. The resulting binary string should be a run-length encoding of the original
    """
    if not S:
        return ''
    count = 1
    while count < len(S) and S[count] == S[0]:
        count += 1
    num = numToBaseB(count,2)
    return S[0] + ('0' * (7 - len(num)) + num) + compress(S[count:])

assert compress('11111') == '10000101'
assert compress('101010') == '100000010000000110000001000000011000000100000001'
assert compress(42*'0') == '00101010'



def uncompress(C):
    """
    accepts a single argument, a binary string that is a run-length encoding of a binary string
    returns the uncompressed/undone binary string of the run-length encoding binary argument
    """
    if C == '':
        return ''
    return C[0] * (baseBToNum(C[1:8], 2)) + uncompress(C[8:])

assert uncompress('01000000') == '0000000000000000000000000000000000000000000000000000000000000000'
assert uncompress('10000101') == '11111'
assert uncompress('100000010000000110000001000000011000000100000001') == '101010'