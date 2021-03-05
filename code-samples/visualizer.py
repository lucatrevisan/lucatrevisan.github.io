import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Graph_Visualizer:

    def __init__ (self,G,pos,node_labels):
        self.graph = G
        self.colors = { v: "yellow" for v in G.nodes() }
        self.positions = pos
        self.node_labels = node_labels
        self.edge_labels = nx.get_edge_attributes(G,'weight')
        plt.figure(figsize=[9,9])
        plt.show(block=False)

        
    def draw(self):
        plt.clf()
        nx.draw_networkx(self.graph, self.positions,node_color=[self.colors[v] for v in self.graph.nodes()],labels = self.node_labels)
        nx.draw_networkx_edge_labels(self.graph,self.positions,edge_labels = self.edge_labels)
        plt.draw()
        if input()=='q':
            exit()


