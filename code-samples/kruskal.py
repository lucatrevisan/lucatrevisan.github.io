from unionfind import UnionFind

def kruskal(G):
    T = []
    C = UnionFind([v for v in G.nodes()])
    E = [(u,v) for (u,v) in G.edges()]
    E.sort(key = lambda e : G.edges[e]['weight'] )
    for (u,v) in E:
        if C.find(u)!= C.find(v):
            C.union(u,v)
            T = T+[(u,v)]
    return (T)
