# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:28:19 2017

@author: Nathalie
"""

from AlgoPy import binTree

def searchBST(x, B):
    if B == None:
        return None
    elif x == B.key:
        return B
    else:
        if x < B.key:
            return searchBST(x, B.left)
        else:
            return searchBST(x, B.right)

def insertBST(x, B):
    if B == None:
        return binTree.BinTree(x, None, None)
    else:
        if x == B.key:
            return B
        else:
            if x < B.key:
                B.left = insertBST(x, B.left)
            else:
                B.right = insertBST(x, B.right)
            return B
                
# after the copy, change a value in the initial tree and take a look at the copy!

def copy(B):
    if B == None:
        return binTree.BinTree(None, None, None)
    else:
        C = binTree.BinTree(B.key, B.left, B.right)
        copy(B.left)
        copy(B.right)
        return C
    
def __copy2(B, C = None):
    if B == None:
        C = binTree.BinTree(None, None, None)
    else:
        C = binTree.BinTree(B.key, B.left, B.right)
        __copy2(B.left, C.left)
        __copy2(B.right, C.left)
        return C




                