# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:24:24 2017
Grahs: biconnectivity
@author: Nathalie
"""

from algopy import graph
from algopy import stack

# TODO: complete the following functions in order to detect cut points 
# (cut edges will be done in tutorial) 

def __biconnectivity(G, x, p, depth, cutPoints, cutEdges):
    """performs the DFS from x in G, returns the "plushaut" value of x
    
    :param p: x's parent
    :rtype: int
    """
    ph_x = depth[x]
    for y in G.adjlists[x]:
        if depth[y] == -1:
            
            depth[y] = depth[x] + 1
            ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges)
            ph_x = min(ph_x, ph_y)
            
            if ph_y >= depth[x]:
                cutPoints[x] += 1
                if ph_y > depth[x]:
                    cutEdges.append((x, y))
        else:
            if y != p:
                ph_x = min(ph_x, depth[y])
            
    return ph_x
    
    
def biconnectivity(G):
    """ launches the DFS (not the first level!)
        returns 
        - cut point vector (int list): how many times each vertex has been detected as cut point
        - cut edge vector (int*int list): later!
    """
    depth = [-1] * G.order    # mark vector: the depth in the spanning forest
    cutPoints = [0] * G.order
    cutEdges = []

    # the first level is here, the recursive DFS is launched only at the next level...
    for x in range(G.order):
        if depth[x] == -1:
            depth[x] = 0
            nbchildren = 0
            for y in G.adjlists[x]:
                if depth[y] == -1:
                    depth[y] = 1
                    ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges)
                    if ph_y > depth[x]:
                        cutEdges.append((x, y))
                    nbchildren += 1
            cutPoints[x] = nbchildren - 1
    
    return (cutPoints, cutEdges)
    
    
# result with "files/graphISP_2.gra"
    
(cutPoints, cutEdges) = ([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2], 
                         [(9, 12), (13, 11), (0, 13)])
    
    
    
    
    
