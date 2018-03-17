# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:46:20 2016
@author: Nathalie
"""

from AlgoPy import redBlackTree
from AlgoPy.redBlackTree import RedBlackTree



def nodeToDot(T, color):
    if color:
        redFormat = "shape = circle, style = filled, color = red"
    else:
        redFormat = "shape = doublecircle"
    s = str(id(T)) + '[label="' + str(T.key) + '"'
    if T.red:
        s += redFormat
    s += '];\n'
    return s
    
def linkToDot(A, B):
    return "   " + str(id(A)) + " -- " + str(id(B)) + ";\n"

def nulChild(T, side):
    s = str(id(T)*side) + '[shape=point, color=white]\n'
    return s + "   " + str(id(T)) + " -- " + str(id(T)*side) + "[color=white];\n"

def __toDot(T, color):
    s = ""
    if T.left != T.right:
        if T.left:
            s += nodeToDot(T.left, color)
            s += linkToDot(T, T.left)
            s += __toDot(T.left, color)
        else:
            s += nulChild(T, 2)
        if T.right:
            s += nodeToDot(T.right, color)
            s += linkToDot(T, T.right)
            s += __toDot(T.right, color)
        else:
            s += nulChild(T, 3)
    return s

def RBTtoDot(T, color=True):
    if T:
        s = "graph {\n"
        s += "node [width=.4, height = .4, fixedsize=true];\n"
        s += nodeToDot(T, color)
        return s + __toDot(T, color) + '}'


#------------------------------------------------
# rendu graphviz directment dans Python
import IPython
from IPython.display import Image 
from graphviz import Graph, Source


def viewTree(B):
    return Image(Source(RBTtoDot(B), format='png').render('test', cleanup=True))

    
#import queue
#from queue import Queue

#    
#def toDot(T, color=True):
#    s = "graph {\n"
#    s += "node [width=.5];\n"
#    q = Queue()
#    queue.enqueue(T, q)
#    s += nodeToDot(T, color)
#    while not queue.isEmpty(q):    
#        T = queue.dequeue(q)
#        if T.left != T.right:
#            if T.left:
#                s += nodeToDot(T.left, color)
#                s += linkToDot(T, T.left)
#                queue.enqueue(T.left, q)
#            else:
#                s += nulChild(T, 2)
#            if T.right:
#                s += nodeToDot(T.right, color)
#                s += linkToDot(T, T.right)
#                queue.enqueue(T.right, q)
#            else:
#                s += nulChild(T, 3)
#    s += "}"
#    return s
