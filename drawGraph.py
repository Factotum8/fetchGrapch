import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_adjlist("graphFriends")

nx.draw(G)
plt.draw()
plt.show()

#raspr = nx.average_degree_connectivity(G)

#plt.bar(range(len(raspr)), raspr.values())
#plt.xticks(range(len(raspr)), list(raspr.keys()) )
#plt.show()
