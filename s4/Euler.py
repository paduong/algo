#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:29:14 2018

@author: nathalie
"""

from algopy import graphmat


def __isEulerian(G, s, M):
    (nb, odd) = (1, 0)
    M[s] = True
    deg = 0
    for adj in range(G.order):
        if G.adj[s][adj] != 0:
            if not M[adj]:
                (n, o) = __isEulerian(G, adj, M)
                nb += n
                odd += o
    # calcul degré (deg) ?
    # stop si odd > 2 ?
                
    return (nb, odd + deg % 2)

def isEulerian(G):
    M = [False] * G.order
    (nb, odd) = __isEulerian(G, 0, M)
    return (nb == G.order) and (odd < 3)


# question 2: check whether a list(path) is an eulerian path (graph is supposed to be eulerian)
def test_Euler_path(G, path):
    #FIXME
    pass