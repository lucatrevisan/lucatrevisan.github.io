import matplotlib.pyplot as plt
import networkx as nx
from dfs import linearize

n=30
p=0.05



G = nx.gnp_random_graph(n,p,directed=True)
L = linearize(G)
node_labels = { L[i] : i for i in range(n)}
print (node_labels)
pos = nx.spring_layout(G)
nx.draw(G,pos,labels = node_labels)
plt.show()
