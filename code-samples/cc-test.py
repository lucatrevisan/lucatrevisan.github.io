import matplotlib.pyplot as plt
import networkx as nx
from dfs import undirected_cc

size = [40,30,30]
probs = [[0.1,0,0],[0,0.1,0],[0,0,0.1]]



G= nx.stochastic_block_model(size,probs)
component = undirected_cc(G)
print (component)
pos = nx.spring_layout(G)
nc = [component[v] for v in G.nodes()]
nx.draw(G,pos,node_size=100,node_color=nc)
plt.show()
