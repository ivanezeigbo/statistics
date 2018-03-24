import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from random import *
import networkx as nx
import pandas as pd
from collections import Counter



# Total population, N.
N = int(input('How many people in the population? '))
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0

people = [a for a in range(N)] #nodes
beta = float(input('What is the probability/rate of contact (eg. 0.3, 0.55, 0.4381, etc.)? '))
alpha = float(input('What is the efficacy of the vaccine (eg. 0.3, 0.55, etc.)? '))
def random_layering():
    path = []
    for g in range(int(round(beta*N * (N-1) * 0.5))):
        x, y = sample(people, 2)
        while ((x, y) in path or (y, x) in path):
            x, y = sample(people, 2)
        path.append((x, y))
    return path


'''
Connect = False
#For a graph that must be connected 
while not Connect: #makes sure graph is connected
    G = nx.Graph()   
    G.add_nodes_from(people)
    path = random_layering() #function that calls for diversity in every round of a game. Commenting this line of code removes diversity in the rounds of the game
    G.add_edges_from(path)
    if nx.is_connected(G): #makes sure graph is a connected graph
        Connect = True
    else:
        Connect = True
        path = random_layering()
'''
path = random_layering() #function that calls for diversity in every round of a game. Commenting this line of code removes diversity in the rounds of the game
G = nx.Graph()
G.add_nodes_from(people)
G.add_edges_from(path)
pos = nx.random_layout(G)
#Must not be a connected graph
def plotter(I_list, S_list, R_list):
    colors = []
    for n in people:
        if n in I_list:
            colors.append('r')
        elif n in S_list:
            colors.append('b')
        else:
            colors.append('g')
        
    nx.draw(G, pos, node_color = colors)
    plt.show() #plots the network
    

        
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
time = int(input('How long would you like to run it? '))
# A grid of time points (in days)
t = np.linspace(0, time, time)

# The SIR model differential equations.
def deriv(y, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    if dIdt >= 0:
        dRdt = (gamma * I) + (alpha * dIdt)
        dIdt -= (alpha *dIdt)
    else:
        dRdt = (gamma * I) - (alpha * dIdt)
        dIdt += (alpha *dIdt) 
    return dSdt, dIdt, dRdt


# Integrate the SIR equations over the time grid, t.
#ret = odeint(deriv, y0, t, args=(N, beta, gamma))
#S, I, R = ret.T
b = 10 #denom for the gamma value
S, I, R = [], [], []
for interval in range(time):
    # Initial conditions vector
    y0 = S0, I0, R0
    if interval == 0:
        pass
        '''
        people_copy = people[:]
        shuffle(people_copy)
        I_list = people_copy[:int(I0)]
        people_copy = people_copy[int(I0):]
        shuffle(people_copy)
        S_list = people_copy[:int(S0)]
        R_list = people_copy[int(I0):]
        plotter(I_list, S_list, R_list)
        '''
    b += 0.5
    gamma = 1./b
    s, i, r = deriv(y0, N, beta, gamma)
    S0 += s
    I0 += i
    R0 += r
    S.append(S0)
    I.append(I0)
    R.append(R0)
    people_copy = people[:]
    shuffle(people_copy)
    I_list = people_copy[:int(I0)]
    people_copy = people_copy[int(I0):]
    shuffle(people_copy)
    S_list = people_copy[:int(S0)]
    R_list = people_copy[int(I0):]
   
    if (interval == int(time/2) - 1) or (interval == time - 1):
        plotter(I_list, S_list, R_list)


S = np.array(S)
I = np.array(I)
R = np.array(R)

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axis_bgcolor='#dddddd', axisbelow=True)
ax.plot(t, S/N, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/N, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/N, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number ('+ str(N) + 's)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
