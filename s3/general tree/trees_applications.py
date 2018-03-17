#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Feb 2018
@author: nathalie
"""

from algopy import tree, treeasbin

"""
ex3.1
"""

def __prefsuff(T, L):
    L.append(T.key)
    for child in T.children:
        __prefsuff(child, L)
    L.append(T.key)
    
def __prefsuffbin(B, L):
    L.append(B.key)
    C = B.child
    while C != None:
        __prefsuffbin(C, L)
        C = C.sibling
    L.append(B.key)

def __prefsuffbin2(B, L):
    L.append(B.key)
    if B.child != None:
        __prefsuffbin2(B.child, L)
    L.append(B.key)
    if B.sibling != None:
        __prefsuffbin2(B.sibling, L)

def prefsuff(T):
    L = []
    if type(T) == tree.Tree:
        __prefsuff(T, L)
    else:
        __prefsuffbin(T, L)
    return L


"""
ex 3.2: parent vector
"""
    
def __parents(T, p):
    for child in T.children:
        p[child.key] = T.key
        __parents(child, p)

def __parentsBin(B, p):
    C = B.child
    while C != None:
        p[C.key] = B.key
        __parentsBin(C, p)
        C = C.sibling        
        
def __parentsbin2(B, p):
    if B.child:
        p[B.child.key] = B.key 
        __parentsbin2(B.child, p)
    if B.sibling:
        p[B.sibling.key] = p[B.key]
        __parentsbin2(B.sibling, p)

def parents(T, n):
    p = [None] * n
    p[T.key] = -1
    if type(T) == tree.Tree:
        __parents(T, p)
    else:
        __parentsbin(T, p)
    return p

"""
3.4: equality
"""

def same(T, B):
    if B.key != T.key:
        return False
    i = 0
    C = B.child
    while i < T.nbchildren and C != None:
        if not same(T.children[i], C):
            return False
        i += 1
        C = C.sibling
    return (C == None and i == T.nbchildren)


"""
3.5: conversions
"""

def treeAsBin2Tree(B):
    T = tree.Tree(B.key, [])
    C = B.child
    while C != None:
        T.children.append(treeAsBin2Tree(C))
        C = C.sibling
    return T


def tree2TreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = tree2TreeAsBin(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B

"""
3.6: list representation
"""

def tree2list(T):
    s = '(' + str(T.key)
    for child in T.children:
        s += tree2list(child)
    s += ')'
    return s

def treeAsBin2list2(B):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += treeAsBin2list2(C)
        C = C.sibling
    s += ')'
    return s
    
    
def treeAsBin2list(B):
    s = '(' + str(B.key)
    if B.child:
        s += treeAsBin2list(B.child)
    s += ')'
    if B.sibling:
        s += treeAsBin2list(B.sibling)
    return s


def __list2tree(s, i=0):
    i += 1
    key = ""
    while s[i] not in "()":
        key += s[i]
        i += 1
    T = tree.Tree(int(key), [])
    while s[i] == '(':
        (child, i) = __list2tree(s, i)
        T.children.append(child)
    i += 1    
    return (T, i)

def list2tree(s):
    (T, _) = __list2tree(s)
    return T

def __list2treeasbin(s, i=0):
    if i < len(s) and s[i] == '(':
        i += 1
        key = ""
        while s[i] not in "()":
            key += s[i]
            i += 1
        B = treeasbin.TreeAsBin(int(key), None, None)
        (B.child, i) = __list2treeasbin(s, i)
        i += 1
        (B.sibling, i) = __list2treeasbin(s, i)
        return (B, i)
    else:
        return (None, i)
    
def list2treeasbin(s):
    return __list2treeasbin(s)[0]
