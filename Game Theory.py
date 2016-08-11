#Game Theory

'''
Suppose each week, 500 competing grocery stores each decide whether or not to continue selling GMO products. Unbeknownst to each other, they all make this decision based on what their competitors did in the last week, figuring that this may be a reasonable gauge of demand for these potentially controversial goods. More specifically, for a given grocery store, labeled  i , there is a threshold  n_i  such that when the number of grocery stores that sold GMO products in week  t-1  is greater than  n_i  , then a grocery story will sell them in week t .


1. Write a program that simulates this game subject to the following guidelines:

    i) The user will input the number of weeks to run the simulation, input the initial number of stores selling GMO products (or set to random), and set the thresholds for each store. The user should not have to set all 500 by hand, but rather should at the very least be able to set all of them to a single value, values from a distribution of some kind, or random.
    ii) The program should output a plot of the number of stores selling GMO products each week.

'''
import random
import matplotlib.pyplot as plt
#assign random thresholds for each grocery store
stores = []
for i in range(500): #creates list of tresholds
    ni = random.randrange(0, 500) #threshold for each store
    stores.append(ni)
n0 = eval(input("Please provide the number of stores selling initially. \t" )) #initial number number of stores selling.
t = eval(input ("How many weeks do you wish to run the simulation? \t")) #time to run simulation
stores_selling = [n0]
init = 0
time = [init]
while init < t:
    n1 = 0 #number selling at every giving time, begins initially with zero
    for r in stores:
        if n0 > r:
            n1 += 1 #increments by 1
    n0 = n1 #new number of stores selling
    stores_selling.append(n0) #append number of stores selling
    init += 1
    time.append(init) #append new time
print ("Number of stores selling at the end of simulation of time,", str(t) + ", is:", n0)
plt.plot(time, stores_selling, color = 'red') #plots graph
plt.show()

