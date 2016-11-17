# Minima should be around 1.0 
#Function:f
from math import *
x_old = 0 # The value does not matter as long as abs(x_new - x_old) > precision
x_new = 4 # The algorithm starts at x=6
y_old = 0
y_new = 7
gamma = 0.001 # step size
precision = 0.000001

def f(x, y): #the function
    E = (cos(0.5*x)*cos(y)) + 2
    return E

print("Initial value  before algorithm was run was", f(x_new, y_new))

def dfx(x, y): #partial derivative with respect to x
    X = (-0.5 *sin(0.5*x)*cos(y)) 
    return X
def dfy(x, y):#partial derivative with respect to y
    Y = (-sin(y) * cos(0.5 *x)) 
    return Y

while (abs(x_new - x_old) >  precision) or (abs(y_new - y_old)> precision):
    x_old = x_new
    y_old = y_new
    x_new += -gamma * dfx(x_old, y_old)
    y_new += -gamma * dfy(x_old, y_old)
    

print("The local minimum occurs at ", f(x_new, y_new))
