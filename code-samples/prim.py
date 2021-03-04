from heap import Heap

def prim(G,s):
    n=G.number_of_nodes()
    Q = Heap(n)
    C = { v: False for v in G.nodes() }
    infty = 1+max([G.edges[u,v]['weight'] for (u,v) in G.edges()])
    cost = { v: infty for v in G.nodes() }
    prev = {  }
    cost[s] = 0
    
    for v in  G.nodes():
        Q.insert(v,cost[v])
    
    while not Q.is_empty():
        v = Q.remove_min()
        C[v]=True
        for w in G.neighbors(v):
            L = G.edges[v,w]['weight']
            if not C[w] and cost[w] >  L:
                cost[w] =  L
                Q.decrease_key(w,cost[w])
                prev[w]=v

    return (prev)
