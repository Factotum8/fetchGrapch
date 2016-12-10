import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_adjlist("graphFriends")

print ("Количество узлов",len (G))

raspr = nx.average_degree_connectivity(G)

print ("Средняя cтепень вершины", sum(raspr.values())/len(raspr))

print ("Средняя минимальная длина пути",nx.average_shortest_path_length (G) )

print ("Кластерный коэффициент ",nx.average_clustering (G) )

nx.draw(G)
plt.draw()
plt.show()
