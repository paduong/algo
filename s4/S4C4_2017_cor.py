# even tree
# 5 pts

def __even_tree(g, src, M):
    M[src] = True
    size = 1
    removed = 0
    for succ in g.adjLists[src]:
        if not M[succ]:
            s, r = __even_tree(g, succ, M)
            removed += r
            if s % 2 == 0:
                removed += 1
            else:
                size += s
    return size, removed

def even_tree(G):
    M = [False]*G.order
    (_, removed) = dfs(G, 0, M)
    return removed


def __even_tree2(g, src, p, L):
    n = 1
    s = 0
    for succ in g.adjLists[src]:
        if p[succ] == -2:
            p[succ] = src
            n += __even_tree2(g, succ, p, L)
    if n % 2 == 0 and p[src] != -1:
        L.append(s)
    return n
        
def even_tree2(g, src = 0):
    p = [-2] * g.order
    L = []
    p[0] = -1
    n = __even_tree2(g, src, p, L)
    return len(L)


def __even_tree3(G, s, p, num):
    impair = True
    for adj in G.adjLists[s]:
        if adj != p:
            (impair_, num) = __even_tree3(G, adj, s, num)
            if impair_:
                impair = not impair
    if not impair:
        num += 1
    return (impair, num)

def even_tree3(G):
    (_, num) = __even_tree3(G, 0, -1, 0)
    return num


#------------------------------------------------------------------------------
# Warshall

def CCFromWarshall(M):
    n = len(M)
    cc = [0]*n
    k = 0
    for x in range(n):
        if cc[x] == 0:
            k += 1
            cc[x] = k
            for y in range(x+1, n):
                if M[x][y]:
                    cc[y] = k
    return (k, cc)



#-----------------------------------------------------------------------------
# union-find given (or how to learn to read appendix!)

def find(x, p):
    rx = x
    while p[rx] >= 0:
        rx = p[rx]
    return rx

def union(x, y, p):
    rx = find(x, p)
    ry = find(y, p)
    if rx != ry:
        if p[rx] < p[ry]:
            p[rx] = p[rx] + p[ry]
            p[ry] = rx
        else:
            p[ry] = p[ry] + p[rx]
            p[rx] = ry

def buildUnionFind(L, n):
    '''
    n: integer > 0
    L: list of pairs (a, b) with a and b in [0, n[
    '''
    p = [-1]*n
    for (x, y) in L:
        union(x, y, p)
    return p

#------------------------------------------------------------------------------
# Connected Components from Union-Find
    
def CCFromEdges(L, n):
    p = build(L, n)
    cc = [None]*n
    k = 0
    for s in range(n):
        if p[s] < 0:
            k += 1
            cc[s] = k
    for s in range(n):
        cc[s] = cc[find(s, p)]
    return (cc, k)


#------------------------------------------------------------------------------
# To The Moon
    
def Moon(n, L):
    p = build(L, n)
    nbVert = []
    for i in range(n):
        if p[i] < 0:
            nbVert.append(-p[i])
    k = len(nbVert)
    ways = 0
    for a in range(k):
        for b in range(a+1, k):
            ways += nbVert[a]*nbVert[b]
    return ways
