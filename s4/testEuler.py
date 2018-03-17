# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:49:38 2017
@author: Nathalie
"""

from algopy import graphmat
import Euler

G1 = graphmat.loadgra("files/house.gra") # the house, eulerian

G2 = graphmat.loadgra("files/notEuler.gra") # not eulerian!


#several eulerian paths for the house
housePaths = [[1, 0, 2, 1, 2, 7, 5, 6, 7, 4, 3, 4, 5, 3, 6, 0],
              [1, 2, 7, 6, 5, 7, 4, 3, 4, 5, 3, 6, 0, 2, 1, 0],
              [0, 6, 7, 5, 6, 3, 4, 3, 5, 4, 7, 2, 1, 2, 0, 1],
              [0, 1, 2, 0, 6, 5, 7, 6, 3, 4, 3, 5, 4, 7, 2, 1]]



