# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:49:12 2018

@author: Nathalie
"""

from algopy import graph
import os

def __graphlist(dirpath):
    """builds a list of graphs from a given directory
    Args: 
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        Graph list
    """
    
    files = os.listdir(dirpath)
    files.sort()
    L = []
    for f in files:
        L.append(graph.loadgra(dirpath + "/" + f))
    return L
    
# pour les adeptes des "list comprehensions" )

def __graphlist2(dirpath):
    files = os.listdir(dirpath)
    files.sort()
    return [graph.loadgra(dirpath + "/" + f) for f in files]
    

#without verification!
def run_coloration(f, dirpath):
    return [f(G)[0] for G in __graphlist(dirpath)]

# with verification

def __testcolors(G, colors):
    for s in range(G.order):
        if not colors[s]:
            return False
        for adj in G.adjlists[s]:
            if colors[s] == colors[adj]:
                return False
    return True

def run_verif_coloration(f, dirpath):
    """tests coloration function on a list of graphs
    Args: 
        f (function): the coloration function (returns (nbcol, color list)) 
            color list: contains integer in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result list: list of color numbers
    """
    tests = __graphlist(dirpath)
    results = []
    for G in tests:
        (nb, colors) = f(G)
        if not __testcolors(G, colors):
            raise Exception("wrong coloration")
        results.append(nb)
    return results