# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:05:18 2016

@author: Nathalie

search for a path from src to dst
return a list with vertices in the path found (empty if no path)
"""

from algopy import graph, graphmat
from algopy import queue

# search for a path with a bfs whith
# uses the parent vector 

def __pathBFSmat(G, src, dst, p):
    q = queue.Queue()
    q.enqueue(src)
    p[src] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in range(G.order):
            if G.adj[s][adj]:
                if p[adj] == None:       
                    p[adj] = s
                    if adj == dst:
                        return True
                    q.enqueue(adj)
            
    return False
    
def __pathBFS(G, src, dst, p):
    q = queue.Queue()
    q.enqueue(src)
    p[src] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if p[adj] == None:       
                p[adj] = s
                if adj == dst:
                    return True
                q.enqueue(adj)
            
    return False

def pathBFS(G, src, dst):
    L = []
    p = [None] * G.order
    if type(G) == graph.Graph:
        findPath = __pathBFS(G, src, dst, p)
    else:
        findPath = __pathBFSmat(G, src, dst, p)
    if findPath:
        while dst != -1:
            L.insert(0, dst)
            dst = p[dst]
    return L
    
# search for a path with a dfs
# parent vector can also be used
# here, a list is built when going up
    
def __pathDFS(G, s, dst, M, path):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            if adj == dst or __pathDFS(G, adj, dst, M, path):
                path.insert(0, adj)
                return True
    return False

def pathDFS(G, src, dst):
    M = [False] * G.order
    path = []
    if __pathDFS(G, src, dst, M, path):
        path.insert(0, src)
    return path

#------------------------------------------------------------------------------
# more...


"""
test whether a list is a valid path in G
"""

def testPath(G, L):
    """
    L (int list): not empty list that contains vertices of the path
    """
    x = L[0]
    for i in range(1, len(L)):
        if L[i] not in G.adjlists[x]:
            return False
        else:
            x = L[i]
    return True
