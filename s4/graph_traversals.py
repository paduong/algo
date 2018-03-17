# -*- coding: utf-8 -*-
"""
Graphs: traversals - tutorial part 2
Nov 2017
@author: Nathalie
"""

from algopy import graph
from algopy import graphmat


#------------------------------------------------------------------------------
# Ex 2.1 q.4
"""
 Breadth First Search (Traversal): 
same algorithm whether the graph is directed or not
"""

from algopy import queue

# with adjacency lists
def __bfs(G, s, p):
    q = queue.Queue()
    q.enqueue(s)
    p[s] = -1    # M[s] = True
    while not q.isempty():
        s = q.dequeue()
        print(s, end = ' ')
        for adj in G.adjlists[s]:
            if p[adj] is None: # not M[adj]       
                p[adj] = s
                q.enqueue(adj)
#                print(s, "->",  adj)
                
# with adjacency matrix
def __bfsMat(G, s, p):
    q = queue.Queue()
    q.enqueue(s)
    p[s] = -1    # M[s] = True
    while not q.isempty():
        s = q.dequeue()
        print(s, end = ' ')
        for adj in range(G.order):
            if G.adj[s][adj]:   #adj is a successor
                if p[adj] is None: # not M[adj]       
                    p[adj] = s
                    q.enqueue(adj)
#                   print(s, "->",  adj)

# call      
def bfs(G):
    """
         Performs a BFS on G
         Returns:
             p (List[int]): represents the spanning forest
             contains the parent of each vertex (-1 for roots)
    """
    p = [None] * G.order   # M = [False] * G.order
    for s in range(G.order):
        if p[s] is None:       # not M[s]
             __bfs(G, s, p)
    return p

#------------------------------------------------------------------------------
# ex 2.2 q2.4

"""
Depth first search (DFS)
"""

# simple DFS with adjacency lists
def __dfs(G, s, M):
    M[s] = True    # usually vertices are marked here
    print(s, end=' ')
    for adj in G.adjlists[s]:
        if not M[adj]: 
            __dfs(G, adj, M)
                
def dfs(G):
    M = [False] * G.order
    for s in range(G.order):
        if not M[s]:
            __dfs(G, s, M)
            
# q.3(c) graph depth-first traversal with back edge detection (with adjacency matric)
def __dfsforest(G, s, p):
    for adj in range(G.order):
        if G.adj[s][adj]:
            if p[adj] == None:  # tree edge
                p[adj] = s      # vertices has to be marked here
                print(s, "->", adj)
                __dfsforest(G, adj, p)
            else:
                if adj != p[s]:
                    print(s, '->', adj, "back edge")    # unless adj -> s is a back edge!
                
def dfsforest(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] == None:
            p[s] = -1
            __dfsforest(G, s, p)
    return p


# q.4(c) digraph depth-first traversal -> prefix and suffix numbering with a single counter
# to detect edge types (with adjacency lists)

def __dfs_digraph(G, s, pref, suff, cpt):
    cpt += 1
    pref[s] = cpt
    for adj in G.adjlists[s]:
        if pref[adj] == 0:
           print (s, "->",  adj)
           cpt = __dfs_digraph(G, adj, pref, suff, cpt)
        else:
            if pref[s] < pref[adj]:
                print (s, "->",  adj, "forward")
            else:
                if suff[adj] == 0:
                    print (s, "->",  adj, "back")
                else:
                    print (s, "->",  adj, "cross")
    cpt += 1
    suff[s] = cpt
    return cpt

def dfs_digraph(G, s = 0):
    pref = [0] * G.order
    suff = [0] * G.order 
    cpt = 0
    cpt = __dfs_digraph(G, s, pref, suff, cpt) # only when there is a source
    for s in range(G.order):    # when the traversal is "complete"
        if pref[s] == 0:
            cpt = __dfs_digraph(G, s, pref, suff, cpt)
    return(pref, suff)