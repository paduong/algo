# -*- coding: utf-8 -*-
"""
Feb. 2018
Connected Graphs and connected components with dfs
@author: Nathalie
"""

from algopy import graph, graphmat

# to test on large graphs
import sys
sys.setrecursionlimit(3000)

#------------------------------------------------------------------------------
# not in the tutorial : seen with istree(S3-td4) and isEulerian (S4-td0)

# test: graph is connected?

def __nbVertexDFS(G, s, M):
    M[s] = True
    nb = 1
    for adj in G.adjlists[s]:
        if not M[adj]:
            nb += __nbVertexDFS(G, adj, M)
    return nb
    
def isConnected(G):
    M = [False]*G.order
    return __nbVertexDFS(G, 0, M) == G.order


# find connected components: basic...


def __components(G, s, cc, no):
    cc[s] = no
    for adj in G.adjlists[s]:
        if cc[adj] == 0:
            __components(G, adj, cc, no)

def components(G):
    '''
    return (nbc, cc)
    nbc: the number of connected components
    cc: the vector of components (cc[i] is the number of the component i belongs to)
    '''
    
    cc = [0]*G.order
    no = 0
    for s in range(G.order):
        if cc[s] == 0:
            no += 1
            __components(G, s, cc, no)
    return (no, cc)

def components2(G):
    '''
    return the list of G's connected components: 
    each component is a list of vertices
    '''
    cc = [0]*G.order
    no = 0
    comp = []
    for s in range(G.order):
        if cc[s] == 0:
            comp.append([])
            no += 1
            __components(G, s, cc, no)
    for i in range(G.order):
        comp[cc[i]-1].append(i)
    return comp


#------------------------------------------------------------------------------
# test tree not in tutorial (see next exercise)
# connected + without cycles

def __isTree(G, s, p):
    '''
    vertex are marked with parents in p
    returns (nb, tree)
    nb: number of met vertices
    tree: boolean == without cycle
    '''
    nb = 1
    for adj in G.adjlists[s]:
        if p[adj] == None:
            p[adj] = s
            (n, tree) = __isTree(G, adj, p)
            nb += n
            if not tree:
                return (nb, False)
        else:
            if adj != p[s]:
                return (nb, False)
    return (nb, True)

def isTree(G):
    p = [None] * G.order
    p[0] = -1
    (nb, tree) = __isTree(G, 0, p)
    return tree and nb == G.order






#------------------------------------------------------------------------------
# assuming G (GraphMat) is a simple graph

def __makeMeTree(G, s, p, cc, k):
    cc[s] = k
    for adj in range(G.order):
        if G.adj[s][adj]:
            if cc[adj] == 0:
                __makeMeTree(G, adj, s, cc, k)
            else:
                if adj != p:
                    G.adj[s][adj] = 0
                    G.adj[adj][s] = 0
                    
    
def makeMeTree(G):
    cc = [0]*G.order
    x = 0
    k = 1
    __makeMeTree(G, 0, -1, cc, k)
    for y in range(1, G.order):
        if cc[y] == 0:
            k += 1
            __makeMeTree(G, y, -1, cc, k)
            G.adj[x][y] = 1
            G.adj[y][x] = 1
            #x = y   
    return cc

    

        
