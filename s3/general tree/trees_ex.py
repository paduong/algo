# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:33:42 2018

@author: nathalie
"""

from algopy.tree import Tree
from algopy.treeasbin import TreeAsBin

#tree from tutorial

T1 = Tree(15, 
         [Tree(3, [Tree(-6), Tree(10)]),
          Tree(8, [Tree(11, [Tree(0), Tree(4)]), 
                   Tree(2), 
                   Tree(5)]), 
          Tree(9)])


C1 = TreeAsBin(3, TreeAsBin(-6, None, TreeAsBin(10)))
C2 = TreeAsBin(8, TreeAsBin(11, TreeAsBin(0, None, TreeAsBin(4)), 
                                TreeAsBin(2, None, TreeAsBin(5))))
C3 = TreeAsBin(9)
C1.sibling = C2
C2.sibling = C3
B1 = TreeAsBin(15, C1, None)
    
