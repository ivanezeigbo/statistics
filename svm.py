#gradient descent - three variables
import csv
import numpy
import matplotlib.pyplot as plt
def loadDataset(filename, X= [], Y= [], Z= []):
    global dataset
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        #Next, I convert the two coordinates from their original string form to float.
        for x in range(len(dataset)):
            try:
                for y in range(2):
                    dataset[x][y] = float(dataset[x][y])
                X.append(dataset[x][0])
                Y.append(dataset[x][1])
                Z.append(dataset[x][2])                        
            except ValueError:
                pass
X = [] #list for X1
Y = [] #list for X2
Z = [] #list for the characteristics            
loadDataset('cs111-svm-datasetsheet1.csv', X, Y, Z) #loads data
dataset.pop(0) #remove first line
for i in range(len(Z)):
    if Z[i]==0:
        Z[i]=-1


#i = m1, j = m2, k = b
from math import *
i_old = 0 # The value does not matter as long as abs(x_new - x_old) > precision
i_new = 4 # The algorithm starts at x=6
j_old = 0
j_new = 7
k_old = 0
k_new = 10
gamma = 0.01 # step size
precision = 0.0001

def func(x, y, j, k, i): #the function
    F = (x*i) + (y*j) + k #x and y are x1 and x2 resp.
    return F
clas = []
def Loss(F): #loss function
    if F < 0:
        c = -1 #c = yi (the class)
    else:
        c = 1
    clas.append(c)
    L = log(1 + exp(-c * F))
    return L
def Error(dataset, j, k, i): #the function
    Total = 0 #total losses
    for m in dataset:
        a = func(m[0], m[1], j, k, i)
        Total += Loss(a) #adds to total
    E = Total/len(dataset) #averages
    return E

print("Initial value  before algorithm was run was", Error(dataset, j_new, k_new, i_new), "for starting values, m1:", i_new, "m2:", j_new, "b:", k_new)


def dfx(dataset, i, j, k): #partial derivative with respect to m1
    X = 0
    for g in dataset:
        t = func(g[0], g[1], j, k, i)
        if t < 0:
            c = -1 #the classes
        else:
            c = 1
        X += (1/(1 + exp(-c * t)))* -c * g[0] * (exp(-c* t))
    I = X/len(dataset) #averages for all ith observation
    return I

def dfy(dataset, i, j, k):#partial derivative with respect to m2
    Y = 0
    for g in dataset:
        t = func(g[0], g[1], j, k, i)
        if t < 0:
            c = -1
        else:
            c = 1
        Y += (1/(1 + exp(-c * t)))* -c * g[1] * (exp(-c * t))
    J = Y/len(dataset)# averages for all ith observation 
    return J

def dfz(dataset, i, j, k):#partial derivative with respect to b
    Z = 0
    for g in dataset:
        t = func(g[0], g[1], j, k, i)
        if t < 0:
            c = -1
        else:
            c = 1
        Z += (1/(1 + exp(-c * t)))* -c * (exp(-c * t))
    K = Z/len(dataset) # averages for all ith observation
    return K


def plot_hyperplane(dataset, m1, m2, b):
    max_x1 = max([sublist[0] for sublist in dataset])#max value of x1 in dataset
    min_x1 = min([sublist[0] for sublist in dataset])
    def x2(x1, m1, m2, b):
        return -(m1*x1+b)/m2
    max_x2 = x2(max_x1, m1, m2, b)
    min_x2 = x2(min_x1, m1, m2, b)
    plt.scatter(X, Y, c=Z, cmap='gray', marker = 'o')#plots data
    plt.plot([min_x2, min_x1], [max_x2, max_x1])
    plt.show()

    plt.scatter(X, Y, c=clas, cmap='gray', marker = 'o')
    plt.plot([min_x2, min_x1], [max_x2, max_x1])
    plt.show()

while ((abs(i_new - i_old) >  precision) or (abs(j_new - j_old)> precision) or (abs(k_new - k_old)> precision)): #or ((j_new - j_old == 0) and (i_new-i_old == 0) and (k_new-k_old == 0))
    i_old = i_new
    j_old = j_new
    k_old = k_new
 
    i_new += -gamma * dfx(dataset, i_old, j_old, k_old) #new m1
    j_new += -gamma * dfy(dataset, i_old, j_old, k_old) #new m2
    k_new += -gamma * dfz(dataset, i_old, j_old, k_old) #new b

plot_hyperplane(dataset, i_new, j_new, k_new)

print("The local minimum of the Error occurs when the Error is", Error(dataset, j_new, k_new, i_new))
print ("The value of m1 is", i_new, "and m2 is", j_new, "and b is", k_new)
