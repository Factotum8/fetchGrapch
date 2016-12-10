import requests 
import re
import json
import networkx as nx

def getFriends(idx): 
 print("==", idx)
 answer = requests.get("https://api.vk.com/method/friends.get?user_id=" + idx)
 if answer.status_code != 200:
 	return []
 decoded = json.loads(answer.text)
 if "response" not in decoded:
 	return []
 return [str(x) for x in decoded["response"]]


G=nx.Graph()

G.add_node(str(26611424))

toCheck = set([str(26611424)])

setAdded = set([str(26611424)])

while  len(toCheck):

	tempHeap = set()

	for node in toCheck :
		neighbours = getFriends(node)

		if len (G)<100:
			tempHeap.update( neighbours )
			setAdded.update( neighbours )
			G.add_nodes_from( neighbours )

		for neighbour in neighbours:
			if node in setAdded and neighbour in setAdded:
				G.add_edge(node,neighbour) 
				G.add_edge(neighbour,node) 

	toCheck = tempHeap
	print (len (G) )

nx.write_adjlist(G,"graphFriends")

