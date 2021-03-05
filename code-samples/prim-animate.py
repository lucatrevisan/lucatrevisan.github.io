from heap import Heap
from visualizer import Graph_Visualizer
from randomgraphs import random_weighted_grid
import networkx as nx


def prim_animate(G,s,pos):

    n=G.number_of_nodes()
    Q = Heap(n)
    S = { v: False for v in G.nodes() }
    prev = { v: "" for v in G.nodes() }
    infty = 1+max([G.edges[u,v]['weight'] for (u,v) in G.edges()])
    cost = { v: infty for v in G.nodes() }
    cost[s] = 0
   
    for v in  G.nodes():
        Q.insert(v,cost[v])

    visualizer = Graph_Visualizer(G,pos,cost)
    visualizer.draw()
    T = nx.DiGraph()
    for v in G.nodes():
        T.add_node(v)
    visualizer.graph = T
    
    while not Q.is_empty():
        v = Q.remove_min()
        S[v]=True
        
        visualizer.colors[v]="orange"
        if v != s :
            T.add_edge(prev[v],v)
            
        for w in G.neighbors(v):
            L = G.edges[v,w]['weight']
            if (not S[w]) and (cost[w] >  L):
                cost[w] =  L
                Q.decrease_key(w,cost[w])
                
                if prev[w]!="":
                    T.remove_edge(prev[w],w)
                T.add_edge(v,w)

                prev[w]=v

        visualizer.draw()

    return (prev)
    
n=5
G,pos=random_weighted_grid(n,10)
prev = prim_animate(G,(n//2,n//2),pos)


