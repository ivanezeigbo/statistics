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
route = []
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
        

for i in sorted_edges:
    if len(states) == 0:
        break
    elif (i[0] in states and i[1] in states) or (i[0] not in memory or i[1] not in memory):
        if (i[0] in states and i[1] in states) == False:
            if i[0] not in states:
                if len(memory[memory[i[0]][1]]) == 2:
                    if (i[0], memory[i[0]][1]) in route:
                        route.remove((i[0], memory[i[0]][1]))
                    else:
                        route.remove((memory[i[0]][1], i[0]))
                    memory[memory[i[0]][1]].remove(i[0])
                    if memory[i[0]][1] not in states:
                        states.append(memory[i[0]][1])
                    memory[i[0]].remove(memory[i[0]][1])
                    
                elif len(memory[memory[i[0]][0]]) == 2:
                    if (i[0], memory[i[0]][0]) in route:
                        route.remove((i[0], memory[i[0]][0]))
                    else:
                        route.remove((memory[i[0]][0], i[0]))
                    memory[memory[i[0]][0]].remove(i[0])
                    if memory[i[0]][0] not in states:
                        states.append(memory[i[0]][0])
                    memory[i[0]].remove(memory[i[0]][0])
            else:
                if len(memory[memory[i[1]][1]]) == 2:
                    if (i[1], memory[i[1]][1]) in route:
                        route.remove((i[1], memory[i[1]][1]))
                    else:
                        route.remove((memory[i[1]][1], i[1]))
                    memory[memory[i[1]][1]].remove(i[1])
                    if memory[i[1]][1] not in states:
                        states.append(memory[i[1]][1])
                    memory[i[1]].remove(memory[i[1]][1])
                    
                elif len(memory[memory[i[1]][0]]) == 2:
                    if (i[1], memory[i[1]][0]) in route:
                        route.remove((i[1], memory[i[1]][0]))
                    else:
                        route.remove((memory[i[1]][0], i[1]))
                    memory[memory[i[1]][0]].remove(i[1])
                    if memory[i[1]][0] not in states:
                        states.append(memory[i[1]][0])
                    memory[i[1]].remove(memory[i[1]][0])
                    
        route.append((i[0], i[1]))
        if i[0] not in memory:
            memory[i[0]] = [i[1]]
        else:
            memory[i[0]].append(i[1])
        if len(memory[i[0]]) == 2 and i[0] in states:
            states.remove(i[0])
        if i[1] not in memory:
            memory[i[1]] = [i[0]]
        else:
            memory[i[1]].append(i[0])
        if len(memory[i[1]]) == 2 and i[1] in states:
            states.remove(i[1])

#import pdb; pdb.set_trace()

if len(states) != 0:        
    Continue = True
    for k in range(len(states) - 1):
        for j in range(k + 1, len(states)):
            if (states[k], states[j]) in E or (states[j], states[k]) in E:
                Continue = False
                route.append((states[k], states[j]))
                       
        
    if Continue:
        cases = states[:]
        for (u, v, x) in sorted_edges:
            if u in states or v in states:
                if v in memory[u]:
                    continue
                else:
                    if v in states:
                        r = v
                    else:
                        r = u
                tracker = []
                check = float('inf')
                def modify(route, states, memory, r, tracker, check):
                    copied = route[:]
                    s_copy = states[:]
                    m_copy = [memory][:][0]
                    t_copy = tracker[:]
                    if r in t_copy:
                        copied2 = copied[:]
                        m_copy2 = [m_copy][:][0]
                        return copied2, check, m_copy2
                    t_copy.append(r)
                    List = list(set(G.neighbors(r)) & set(s_copy))
                    if len(List) == 1:
                        copied.append((r, List[0]))
                        m_copy[r].append(List[0])
                        m_copy[List[0]].append(r)
                        s_copy.remove(List[0])
                        if len(s_copy) == 0:
                            t_copy.append(List[0])
                            check = len(s_copy)
                            copied2 = copied[:]
                            m_copy2 = [m_copy][:][0]
                            return copied2, check, m_copy2
                        else:
                            for p in s_copy:
                                copied2, check, m_copy2 = modify(copied, s_copy, m_copy, p, t_copy, check)
                                if check == 0:
                                    break
                        return copied2, check, m_copy2
                    if len(List) > 1:
                        for q in List:
                            copied2 = copied[:]
                            s_copy2 = s_copy[:]
                            t_copy2 = t_copy[:]
                            m_copy2 = [m_copy][:][0]
                            
                            copied2.append((r, q))
                            s_copy2.remove(q)
                            m_copy2[r].append(q)
                            m_copy2[q].append(r)
                            copied2, check, m_copy2 = modify(copied2, s_copy2, q, t_copy2, check)
                            if check == 0:
                                break
                        return copied2, check, m_copy2
                    if len(List) == 0:
                        for d in rank[r]:
                            if d in t_copy:
                                continue
                            if (r, d) not in copied and (d, r) not in copied:
                                copied2 = copied[:]
                                s_copy2 = s_copy[:]
                                t_copy2 = t_copy[:]
                                m_copy2 = [m_copy][:][0]
                            
                                copied2.append((r, d))
                                if d in s_copy2:
                                    s_copy2.remove(d)
                                if r in s_copy2:
                                    s_copy2.remove(r)
                                m_copy2[r].append(d)
                                m_copy2[d].append(r)
                                if rank[d][0] in s_copy2 and rank[d][0] not in m_copy2[d]:
                                    copied2.append((d, rank[d][0]))
                                    m_copy2[d].append(rank[d][0])
                                    m_copy2[rank[d][0]].append(d)
                                    s_copy2.remove(rank[d][0])
                                    if d in s_copy2:
                                        s_copy2.remove(d)
                                    if len(s_copy2) == 0:
                                        t_copy2.append(rank[d][0])
                                        check = len(s_copy2)
                                        return copied2, check, m_copy2
                                    else:
                                        for p in s_copy2:
                                            copied2, check, m_copy2 = modify(copied2, s_copy2, m_copy2, p, t_copy2, check)
                                            if check == 0:
                                                break
                                        return copied2, check, m_copy2
                                elif rank[d][1] in s_copy2 and rank[d][1] not in m_copy2[d]:
                                    copied2.append((d, rank[d][1]))
                                    m_copy2[d].append(rank[d][1])
                                    m_copy2[rank[d][1]].append(d)
                                    s_copy2.remove(rank[d][1])
                                    if len(s_copy2) == 0:
                                        t_copy2.append(rank[d][1])
                                        check = len(s_copy2)
                                        return copied2, check, m_copy2
                                    else:
                                        for p in s_copy2:
                                            copied2, check, m_copy2 = modify(copied2, s_copy2, m_copy2, p, t_copy2, check)
                                            if check == 0:
                                                break
                                        return copied2, check, m_copy2
                                for h in m_copy2[d]:
                                    if h in s_copy2:
                                        continue
                                    if len(list(set(m_copy2[h]) & set(s_copy2))) == 0:
                                        copied3 = copied2[:]
                                        s_copy3 = s_copy2[:]
                                        t_copy3 = t_copy2[:]
                                        m_copy3 = [m_copy2][:][0]
                                        t_copy3.append(d)
                                        m_copy3[d].remove(h)
                                        m_copy3[h].remove(d)
                                        if (d, h) in copied3:
                                            copied3.remove((d, h))
                                        if (h, d) in copied3:
                                            copied3.remove((h, d))
                                        copied2, check, m_copy2 = modify(copied3, s_copy3, m_copy3, h, t_copy3, check)
                                        if check == 0:
                                            break
                                return copied2, check, m_copy2
                copied, check, mem = modify(route, cases, memory, r, tracker, check)
                memory = mem
                if check == 0:
                    break

                city_list = cities[:]
                def mem_check(prior, city_list, mem, vertex, s_vertex):
                    if vertex == s_vertex:
                        if prior != s_vertex and len(city_list) != 0:
                            return False
                        else:
                            return True
                    city_list.remove(vertex)
                    if mem[vertex][0] != prior:
                        return mem_check(vertex, city_list, mem, mem[vertex][0], s_vertex)
                    else:
                        return mem_check(vertex, city_list, mem, mem[vertex][1], s_vertex)

                if mem_check(s_vertex, city_list, mem, s_vertex, s_vertex):
                    break

steps = []
def hamilton(prior, mem, vertex, s_vertex):
    steps.append(vertex)
    if vertex == s_vertex and prior != s_vertex:
        return steps
    if mem[vertex][0] != prior:
        return hamilton(vertex, mem, mem[vertex][0], s_vertex)
    else:
        return hamilton(vertex, mem, mem[vertex][1], s_vertex)

steps = hamilton(s_vertex, memory, s_vertex, s_vertex)
print('The Sorted Edges Hamiltonian cycle is:', steps)
