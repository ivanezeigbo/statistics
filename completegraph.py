import networkx as nx
import matplotlib.pyplot as plt

Cl= {} #landmark label
Cl[0] = 'Residence Hall'
Cl[1] = 'East Side Gallery' 
Cl[10] = 'Checkpoint Charlie'
Cl[9] = 'TV Tower'
Cl[2] = 'Berlin Cathedral'
Cl[7] = 'Potsdamer Platz'
Cl[6] = 'Memorial of the Murdered Jews'
Cl[4] = 'Brandenburg Gate'
Cl[3] = 'Reichstag'
Cl[8] = 'Victory Column'
Cl[5] = 'Tiergarten'
Cl[11] = 'Alexanderplatz'





G = nx.Graph()
cities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#paths is the list of edges/edge connections as first two elements in each tuple of the list and the weight (in decimals) of the edge as third element
paths = [(1, 3, 0.2), (2, 3, 0.2), (0, 3, 0.4), (0, 1, 0.3), (11, 1, 0.33), (10, 11, 0.6), (4, 11, 0.8), (2, 4, 0.1), (5, 7, 0.2), (5, 9, 0.5), (3, 5, 0.6), (1,9, 0.34), (3, 10, 0.7), (4, 5, 0.3), (5, 6, 0.5), (6, 4, 0.3), (6, 7, 0.3), (7, 8, 0.2), (8, 9, 0.2), (9, 10, 0.1), (10, 1, 0.23), (6, 8, 0.04), (2, 9, 0.8)]
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
    s_vertex = 0 #starting vertex/residence
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

for i in Circuits:
    if sorted(i) in Sorted: #some routes are just reverse, so repetition
        pass
    else:
        Sorted.append(sorted(i))
        H_Cycle.append(i)
print("The most optimal Hamiltonian cycle here are: \n", H_Cycle)
print("")
print("There are", len(H_Cycle), "number of Hamiltonian circuits without repetition")
print("")

if len(H_Cycle) == 1:
    opt = H_Cycle[0]
    print("This is the only Hamiltonian cycle. So the the optimal cycle is: /n", opt)
else:
    indx = len(H_Cycle[0]) - 1
    H_Cycle = sorted(H_Cycle, key=lambda H_Cycle:H_Cycle[indx])
    opt = H_Cycle[0]
    print("The most optimal Hamiltonian cycle is: \n", opt)
print("")

y = len(opt) - 1
Path = opt[:]
Path.pop(y)
y = y - 1
Sol = [] #Path of the optimal cycle
while y > 0:
    Sol.append((Path[y], Path[y-1]))
    y -= 1
print ("These are the edge connections of the best path (and reverse):", Sol)
print("")

edge_col = []
for i in E:
    if i in Sol:
        pass
    else:
        edge_col.append(i)       

y = len(opt) - 1
Path = opt[:]
Path.pop(y)
print("This is the best route to follow:")
for i in Path:
    print(Cl[i])
    
