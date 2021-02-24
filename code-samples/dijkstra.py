from heap import Heap

def dijkstra(G,s):
    n=G.number_of_nodes()
    Q = Heap(n)
    infty = 1+sum([G.edges[u,v]['weight'] for (u,v) in G.edges()])
    dist = { v : infty for v in G.nodes() }
    dist[s]=0
     
    for v in  G.nodes():
        Q.insert(v,dist[v])
    
    while not Q.is_empty():
        v = Q.remove_min()
        for w in G.neighbors(v):
            L = G.edges[v,w]['weight']
            if dist[w] > dist[v] + L:
                dist[w] = dist[v] + L
                Q.decrease_key(w,dist[w])

    return (dist)
