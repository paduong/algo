# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:42:48 2018

@author: admin
"""


#------------------------------------------------------------------------------
# Indicateurs de connexité (connectivity indicators?)


def __nbVertexDFS(G, s, M):
    M[s] = True
    nb = 1
    for adj in G.adjlists[s]:
        if not M[adj]:
            nb += __nbVertexDFS(G, adj, M)
    return nb
    
def connectivity(G):
    M = [False]*G.order
    k = 0
    IC2 = 0
    for s in range(G.order):
        if not M[s]:
            k += 1
            nb = __nbVertexDFS(G, s, M)
            IC2 += nb*nb
    IC1 = (G.order - k) / (G.order-1)
    IC2 = IC2 / (G.order * G.order)
    return (IC1, IC2)
    
    
#------------------------------------------------------------------------------
# strong connectivity Test, Tarjan

def __isStronglyConnected(G, x, pref, cpt):
    cpt += 1
    pref[x] = cpt
    return_x = pref[x]
    for y in G.adjlists[x]:
        if pref[y] == 0:
            (ret_y, cpt) = __isStronglyConnected(G, y, pref, cpt)
            if ret_y == -1:
                return (-1, cpt)
            return_x = min(return_x, ret_y)
        else:
            return_x = min(return_x, pref[y])
    
    if return_x == pref[x]:
        if pref[x] != 1:    # the root must be thefirst vertex
            return (-1, cpt)
    
    return (return_x, cpt)

def isStronglyConnected(G):
    pref = [0]*G.order
    cpt = 0
    (_, cpt) = __isStronglyConnected(G, 0, pref, cpt)
    return (cpt == G.order) # all vertices have been encountered
    
    
    
    