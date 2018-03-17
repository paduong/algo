#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nov 2017

@author: nathalie
"""
from  algopy import graphmat, queue


"""
3.2 distance from start: displays vertices 
at distance in [dmin, dmax]
"""

def __distances(G, s, depth, dmin, dmax):
    depth[s] = 0
    q = queue.Queue()
    q.enqueue(s)
    actual = 0
    while not q.isempty():
        s = q.dequeue()
        if depth[s] >= dmin:
            if depth[s] > actual:   # not nice...
                actual = depth[s]
                print()
            print(s, end=' ')
        if depth[s] < dmax:
            for adj in range(G.order):
                if G.adj[s][adj]:
                    if depth[adj] == None:
                        depth[adj] = depth[s] + 1
                        q.enqueue(adj)
    print()
    
def distances(G, src, dmin, dmax):
    depth = [None] * G.order
    __distances(G, src, depth, dmin, dmax)
    return depth

# without depth vector

def __distances2(G, s, M, dmin, dmax):    
    q = queue.Queue()
    q.enqueue(s)
    M[s] = True
    q2 = queue.Queue()
    depth = 0
    while not q.isempty():
        s = q.dequeue()
        if depth >= dmin:
            print(s, end=' ')
        if depth < dmax:
            for adj in range(G.order):
                if G.adj[s][adj]:
                    if not M[adj]:
                        q2.enqueue(adj)
                        M[adj] = True
        if q.isempty():
            depth += 1
            if depth > dmin:
                print()
            (q, q2) = (q2, q)
            
    
def distances2(G, src, dmin, dmax):
    M = [False] * G.order
    __distances2(G, src, M, dmin, dmax)

   