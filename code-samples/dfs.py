def undirected_cc(G):

# returns a dictionary "component" such that component[v] is
# the number of the connected component that v belongs to

    def explore_cc(v):
        visited[v]=True
        component[v] = c
        for w in G.neighbors(v):
            if not visited[w]:
                explore_cc(w)



    visited = { v: False for v in G.nodes()}
    component = {v: 0 for v in G.nodes()}
    c=0
    for v in G.nodes():
        if not visited[v]:
            c=c+1
            explore_cc(v)
    return component
    
    
def linearize(G):

# If G is a DAG, returns a list L of vertices in topologically
# sorted order. It does not test that G is a DAG

    def explore_lin(v):
        nonlocal L
        visited[v]=True
        for w in G.neighbors(v):
            if not visited[w]:
                explore_lin(w)
        L = [v]+L

    L=[]
    visited = { v: False for v in G.nodes()}
    print(L)
    for v in G.nodes():
        if not visited[v]:
            explore_lin(v)
    return L

def directed_scc(G):

# returns a dictionary "component" such that component[v] is
# the number of the strongly connected component that v belongs to

    def explore_cc(v):
        visited[v]=True
        component[v] = c
        for w in G.neighbors(v):
            if not visited[w]:
                explore_cc(w)


    GR = G.reverse()
    L = linearize(GR)
    
    visited = { v: False for v in G.nodes()}
    component = {v: 0 for v in G.nodes()}
    c=0
    for v in L:
        if not visited[v]:
            c=c+1
            explore_cc(v)
    return component

    
