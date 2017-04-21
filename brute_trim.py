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


def intera(i, nodes, ct, route):
    if (i != s_vertex) and (len(nodes) >= 1):               
        for m in dic[i]: #neighbors in i
            if m in nodes:
                br = nodes[:]
                link = ct[:]
                if (m == s_vertex) and (len(nodes) == 1):
                    ct.append(s_vertex)
                    route.append(ct)
                    return route
                if (m != s_vertex):
                    link.append(m)
                    br.remove(m)
                    intera(m, br, link, route)
 
    
            
                    
                        
def hamiltonian(G, cities):#Hamiltonian cycle
    global dic, nodes, ct, route, s_vertex
    dic = {}
    for i in cities:
        dic[i] = G.neighbors(i)       
    edges = E
    s_vertex = 'A' #starting vertex/residence
    start = dic[s_vertex]
    route = []
    for i in start:
        nodes = cities[:]
        ct = [s_vertex, i]
        nodes.remove(i)
        intera(i, nodes, ct, route)
                   
    return route


Circuits =  hamiltonian(G, cities)
H_Cycle = []
Sorted = []

for g in Circuits:
    weight_sum = 0
    num = len(g) - 1
    while num > 0:
        weight_sum += G[g[num]][g[num - 1]]['weight']
        num -= 1
    g.append(weight_sum)
print ("This is the list of all Hamiltonian cycles and their weights at the end: \n", Circuits)
print("")
print("There are", len(Circuits), "number of Hamiltonian circuits possible.")
print("")

if len(Circuits) == 1:
    opt = Circuits[0]
    print("This is the only Hamiltonian cycle. So the the optimal cycle is: /n", opt)
else:
    indx = len(Circuits[0]) - 1
    H_Cycle = sorted(Circuits, key=lambda Circuits:Circuits[indx])
    opt = H_Cycle[0]
    opt.pop(-1)
    print("The most optimal Hamiltonian cycle is: \n", opt)
