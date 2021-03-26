import networkx as nx
import random
import numpy as np

def random_weighted_grid(n,maxweight):

    G = nx.grid_2d_graph(n,n)
    pos = { (a,b) : np.array([a,b]) for (a,b) in G.nodes() }
    for (u,v) in G.edges():
        G.edges[u,v]['weight']=1+random.randrange(maxweight)
    return G,pos

