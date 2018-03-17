# -*- coding: utf-8 -*-
"""
Nov. 2017
@author: Nathalie
"""

''' 3 ways to traverse a string '''

def print_string(s):
    i = 0
    n = len(s)
    while i < n:
        print(s[i])
        i = i + 1

def print_string2(s):
    for i in range(len(s)):
        print(s[i], end='-')

def print_string3(s):
    for c in s:
        print(c, end='')

#----------------------- ex 1.1 -----------------------------------------------

def in_string(c, s):
    '''
    tests whether character c is in string s
    '''
    i = 0
    n = len(s)
    while (i < n) and (s[i] != c):
        i = i + 1
    if i < n:
        return i
    else:
        return -1


def substring(s, str):
    '''
    tests whether s is a substring of s
    '''
    n = len(s)
    n2 = len(str)
    i = 0
    ok = False
    while (i <= n2 - n) and not ok:  # ok can be replaced by j == n
        j = 0
        while (j < n) and (s[j] == str[i+j]):
            j = j + 1
        ok = j == n
        i = i + 1
    return ok

def substring2(s, str):
    '''
    returns the position of s in str, -1 if s not in str
    '''
    n = len(s)
    n2 = len(str)
    i = 0
    j = 0
    ok = False
    while (i <= n2 - n) and j < n:
        j = 0
        while (j < n) and (s[j] == str[i+j]):
            j = j + 1
        ok = j == n
        i = i + 1
    if ok:
        return i-1
    else:
        return -1
        
#----------------------- ex 1.2 -----------------------------------------------
    
def palindrome(s):
    '''    
    tests whether s is a palindrome
    '''
    i = 0
    n = len(s)
    while (i < n//2) and (s[i] == s[n-i-1]):
        i = i+1
    return (i == n//2)

def palindrome2(s):
    i = 0
    j = len(s)-1
    while (i < j) and (s[i] == s[j]):
        if s[i] == ' ':
            i = i+1
        if s[j] == ' ':
            j = j-1
        i = i+1
        j = j-1
    return (i >= j)
    
   
#----------------------- ex 2.1 -----------------------------------------------

# power

def power(x, n):
    '''
    returns x^n only if n natural!
    '''
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power(x*x, n//2)
        else:
            return power(x*x, n//2) * x
            
# decimal integer -> p-bit two’s complement representation
    
def dec_to_bin(n, p):
    '''
    transform a decimal in binary (as a string)
    '''
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    while len(s) < p:
        s = '0' + s
    return s

def integer_to_twoscomp(n, p):
    '''
    returns the p-bits two's complement representation  of the integer n
    '''
    if n < 0:
        n = power(2, p) + n
    return dec_to_bin(n, p)


def not_b(c):
    if c == '1':
        return '0'
    else:
        return '1'

def integer_to_twoscomp2(n, p):
    if n < 0:
        sign = -1
    else:
        sign = 1
    s = dec_to_bin(sign*n, p)
    if sign == -1:
        s2 = ""     # str unmutable
        i = p-1
        while s[i] != '1':      # True eventually
            s2 = s[i] + s2
            i = i - 1
        i = i - 1
        while i >= 0:
            s2 = not_b(s[i]) + s2
            i = i - 1
        s = s2
    return s
    
# p-bit two’s complement representation -> decimal integer
    
def bin_to_dec(s):
    '''
    transform a binary (string) in decimal
    '''
    n = 0
    for b in s:
        n = n * 2 + int(b)
    return n

def twoscomp_to_integer(b, p):
    '''
    returns the integer n from its p-bits two's complement representation 
    '''
    n = bin_to_dec(b)    
    if b[0] == '1':
        n = n - power(2, p)
    return n

def test(n, p):
    return twoscomp_to_integer(integer_to_twoscomp(n,p), p) == n
    


#----------------------- ex 2.2 -----------------------------------------------

def frequent(s):
    '''
    returns (nb, c):
    c: the most frequent char in s
    nb: number of c in s
    '''
    max = 0
    for i in range(len(s)):
        cpt = 0
        for j in range(i, len(s)):
            cpt = cpt + (s[i] == s[j])
        if cpt > max:
            (max, c) = (cpt, s[i])
    return (max, c)
    # this version is in n**2 (n(n+1)/2)

def frequent2(s):
    max = 0
    for i in range(255):
        cpt = 0
        for ch in s:
            cpt = cpt + (ord(ch) == i)
        if cpt > max:
            (max, c) = (cpt, chr(i))
    return (max, c)
    # this version: 256 * n
# a better version later (with an histogram)


'''
to build a string randomly
'''
from random import randint
def build_ex(n):
    s = ""
    for i in range(n):
        s += chr(randint(0,255))
    return s
