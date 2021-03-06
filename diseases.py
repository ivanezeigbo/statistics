import networkx as nx
import matplotlib.pyplot as plt
from random import *

Cl= {} #country label
Cl[0] = ['Germany', 0, 12050, 0.5] #country, infected people, population, threshold between countries
Cl[1] = ['Belgium', 0, 14000, 0.58] 
Cl[2] = ['Czech Republic', 0, 9200, 0.7]
Cl[3] = ['Finland', 0, 1502, 0.46]
Cl[4] = ['France', 1, 10312, 0.34]
Cl[5] = ['Estonia', 0, 14005, 0.79]
Cl[6] = ['Latvia', 0, 13211, 0.67]
Cl[7] = ['Italy', 0, 32123, 0.7]
Cl[8] = ['Luxembourg', 0, 532887, 0.4]
Cl[9] = ['Malta', 0, 65474, 0.8]
Cl[10] = ['Norway', 0, 643864, 0.65]
Cl[11] = ['Spain', 0, 57276, 0.3]
Cl[12] = ['Switzerland', 0, 9876, 0.44]
Cl[13] = ['Netherland', 0, 85885, 0.52]


G = nx.Graph()
cities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#paths is the list of edges/edge connections as first two elements in each tuple of the list and the weight (in decimals) of the edge as third element
paths = [(1, 3, 0.4), (7, 8, 0.3), (13, 1, 0.2), (13, 4, 0.7), (13, 0, 0.4), (13, 9, 0.5), (13, 12, 0.6), (13, 4, 0.55), (11, 10, 0.6), (12, 11, 0.5), (12, 3, 0.5), (12, 5, 0.2), (12, 8, 0.3), (6, 11, 0.7), (11, 2, 0.5), (11, 8, 0.8), (9, 10, 0.56), (10, 1, 0.5), (10, 6, 0.4), (10, 8, 0.6), (10, 5, 0.5), (2, 3, 0.5), (8, 0, 0.7), (9, 1, 0.3), (9, 5, 0.6), (9, 2, 0.7), (4, 1, 0.7), (1, 2, 0.6), (8, 3, 0.5), (8, 6, 0.3), (8, 1, 0.45), (6, 1, 0.5), (3, 6, 0.4), (7, 1, 0.25), (6, 7, 0.3), (0, 5, 0.4), (0, 1, 0.45), (2, 4, 0.62), (3, 5, 0.47), (4, 5, 0.55)]
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
    
labels2 = {} #another node labels with names
for i in cities:
    labels2[i] = Cl[i][0]
    
edge_label = {} #add weights to drawing
for u, v in E:
    edge_label[(u, v)] = G[u][v]['weight']
    
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos, labels2, font_size = 14) #you can change 'labels' to 'Cl' if you want their full names on the graph
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
    global dic, nodes, ct, route, s_vertex, d_places, Continue
    dic = {}
    d_places = cities[:]
    try:
        s_vertex = 0 #relief center
    except KeyError:
        Continue = False
        print ("\nUsed all Hamiltonian Cycles possible \n")
        return
    for i in cities:
        if len(G.neighbors(i)) <=1:
            if i != s_vertex:
                d_places.remove(i)

        else:
           dic[i] = G.neighbors(i)
           for s in dic[i]:
               if s not in d_places:
                  dic[i].remove(s)
    cities = d_places[:]       
    edges = E
    try:
        start = dic[s_vertex] #starting vertex/residence
    except KeyError:
        Continue = False
        print ("\nUsed all Hamiltonian Cycles possible \n")
        return 
 
    route = []
 
    for m in start:
        nodes = cities[:]
        ct = [s_vertex, m]
        if m in nodes:
            nodes.remove(m)
        intera(m, nodes, ct, route)
                   
    return route

def flow(G, cities):
    global Continue, Circuits
    Circuits =  hamiltonian(G, cities)
    H_Cycle = []
    Sorted = []
    if Continue:
        try:
            for g in Circuits:
                weight_sum = 0
                num = len(g) - 1
                while num > 0:
                    weight_sum += G[g[num]][g[num - 1]]['weight']
                    num -= 1
                g.append(weight_sum)
        except AttributeError:
            Continue = False
            print ("\nUsed all Hamiltonian Cycles possible \n")
            return
    else:
        return
        
    #print ("This is the list of all Hamiltonian cycles and their weights at the end: \n", Circuits)
    #print("")
    print("\nThere are", len(Circuits), "number of Hamiltonian circuits possible.")
    print("")

    for i in Circuits:
        if sorted(i) in Sorted: #some routes are just reverse, so repetition
            pass
        else:
            Sorted.append(sorted(i))
            H_Cycle.append(i)
    #print("The most optimal Hamiltonian cycle here are: \n", H_Cycle)
    #print("")
    print("\nThere are", len(H_Cycle), "number of Hamiltonian circuits without repetition")
    print("")

    if len(H_Cycle) != 0:
        Continue = True
        if len(H_Cycle) == 1:
            opt = H_Cycle[0]
            print("This is the only Hamiltonian cycle. So the the optimal cycle is: \n", opt)
        else:
            indx = len(H_Cycle[0]) - 1
            H_Cycle = sorted(H_Cycle, key=lambda H_Cycle:H_Cycle[indx])
            opt = H_Cycle[0]
            print("The most optimal Hamiltonian cycle is: \n", opt)
        print("")
    else:
        Continue = False
        print("No Hamiltonian circuit. \n")
        
    if Continue:
        y = len(opt) - 1
        Path = opt[:]
        Path.pop(y)
        y = y - 1
        Sol = [] #Path of the optimal cycle
        while y > 0:
            Sol.append((Path[y], Path[y-1]))
            y -= 1
        #print ("These are the edge connections of the best path (and reverse):\n", Sol)
        #print("")

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
            print(Cl[i][0])
        print("")
            
def disease(y, N): #Differential equation showing change in infected people
    J = round(0.0001*(y)*(N-y), 0)
    return int(J)

Continue = True

d_places = cities[:]
def main(G, cities, Cl, d_places):
    a = 0
    places = cities[:]
    
    while Continue:
        a += 1
        flow(G, places) #changed this from 'places' to 'rem'
        if Continue:
            for g in d_places:
                if Cl[g][1] > Cl[g][2]:
                    Cl[g][1] = Cl[g][2]
                  
                elif (Cl[g][1] > 0) and (Cl[g][1]/Cl[g][2] < 1):
                    Cl[g][1] += disease(Cl[g][1], Cl[g][2])
                    if Cl[g][1] > Cl[g][2]:
                        Cl[g][1] = Cl[g][2]
            for i in d_places:
                if Cl[i][1] > 0:
                    for m in G.neighbors(i):
                        #print(i, m)
                        if m in d_places:
                            if Cl[m][1] != Cl[m][2]:
                                z = random()
                                if z <= ((Cl[i][1]/Cl[i][2]) * (1 - G[i][m]['weight'])):
                                    t = z * Cl[i][2]/(1 -G[i][m]['weight'])
                                    if (t != 0) and (t == round(t, 0)):
                                        k = int(t)
                                    else:
                                        k = int(t) + 1
                                    Cl[m][1] += k
                                    if Cl[m][1] > Cl[m][2]:
                                        Cl[m][1] = Cl[m][2]
            for v in d_places: #people cured from medication
                Cl[v][1] -= round(0.1*Cl[v][1])               
            
        for y in range(len(Cl)):
            if y == len(Cl) - 1:
                print (Cl[y], end = '. \n')
            else:
                print(Cl[y], end = ', ')
        print("")

        isolated = True
        rem = [] #remaining nodes in circuit
        for u, l in G.edges():
            if u not in rem:
                rem.append(u)
            if l not in rem:
                rem.append(l)
        if len(rem) != 0:
            for r in rem:
                if Cl[r][1] > 0:
                        isolated = False
        if isolated and (len(rem) != 0):
            print("\nThere was successful isolation. Diesease can no longer spread in network!")
            a -= 1 #successful isolation occured during the last step
            break
        
        for f in cities:
            for j in G.neighbors(f):
                if Cl[j][1]/Cl[j][2] > Cl[f][3]:
                    print ("Ban transportation between", Cl[f][0], "and",Cl[j][0])
                    G.remove_edge(f, j)
        
    print("")               
    print("Could only travel about", a, "times.")
    new_lab = {}
    for z in G.edges():
        new_lab[z] = edge_label[z]
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos, labels2, font_size = 14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = new_lab, font_size = 10)
    plt.show()
                    
main(G, cities, Cl, d_places)            
