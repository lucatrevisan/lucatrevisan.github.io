import matplotlib.pyplot as plt
import networkx as nx
from dfs import directed_scc

n=15
p=0.15



G = nx.gnp_random_graph(n,p,directed=True)
component = directed_scc(G)
pos = nx.spring_layout(G)
nc = [component[v] for v in G.nodes()]
nx.draw(G,pos,node_size=200,node_color=nc,labels=component)
plt.show()
