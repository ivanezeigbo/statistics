import networkx as nx
import matplotlib.pyplot as plt
cities = ['A', 'B', 'C', 'D', 'E', 'F']
paths =    [('A', 'B', 1),
            ('A', 'C', 5),
            ('A', 'D', 3),
            ('B', 'C', 4),
            ('B', 'D', 2),
            ('C', 'D', 1),
            ('E', 'A', 4),
            ('F', 'E', 5),
            ('F', 'C', 4),
            ('E', 'D', 2)
            ]
s_vertex = 'A'
G = nx.Graph()
#paths is the list of edges/edge connections as first two elements in each tuple of the list and the weight (in decimals) of the edge as third element
G.add_nodes_from(cities)
G.add_weighted_edges_from(paths)
pos = nx.circular_layout(G) #form of layout of graph I want. Since I want a Hamiltonian cycle, then I want something circular for easy interpretation
print("Is graph connected? ", 'Yes' if nx.is_connected(G) else 'No')
print("There are", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")
E = G.edges()
print("These are the edges we have in the graph: \n", E)
print("")

labels = {} #node labels
for i in cities:
    labels[i] = i
edge_label = {} #add weights to drawing
for u, v in E:
    edge_label[(u, v)] = G[u][v]['weight']
    
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos, labels, font_size = 14) #you can change 'labels' to 'Cl' if you want their full names on the graph
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_label, font_size = 10)
#plt.savefig('graphth.png') #to save image
plt.show()


indx = len(paths[0]) - 1
sorted_edges = sorted(paths, key =lambda paths:paths[indx])
#print(sorted_edges)

states = cities[:]
memory = {}
route = [s_vertex]
rank = {}
val = 0
for g in sorted_edges:
    if g[0] not in rank:
        rank[g[0]] = [g[1]]
    else:
        rank[g[0]].append(g[1])
    if g[1] not in rank:
        rank[g[1]] = [g[0]]
    else:
        rank[g[1]].append(g[0])       
#print(rank)

checker = cities[:]
checker.append(s_vertex)
def hamilton(route, vertex, prior, checker, s_vertex):
    checker1 = checker[:]
 
    checker1.remove(vertex)
    if vertex == s_vertex and s_vertex != prior:
        if len(checker1) == 0:
            return route, checker1           
        else:
            return route, checker
    else:
        for i in rank[vertex]:
            if i not in checker1:
                continue
            new1 = route[:]
            new1.append(i)
            route2, checker = hamilton(new1, i, vertex, checker1, s_vertex)
            if len(checker) == 0:
                route = route2[:]
                break
        return route, checker
    return route, checker
    
route, checker = hamilton(route, s_vertex, s_vertex, checker, s_vertex)
print('The Greedy/Nearest Neighbor Hamiltonian Cycle is:', route)

