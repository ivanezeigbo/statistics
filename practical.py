import math
import random
import scipy.stats as st
from time import clock
#import pdb; pdb.set_trace()
import matplotlib.pyplot as plt
'''
50 kg of cement = $70 => 1kg = $1.4
50000g = $70
'''
Cost = math.pi * 2160 * (1.4)
print("The actual cost should be", "$"+ str(Cost)) 

threshold = 1 #cannot allow a loss greater than this

#Best proportion to use. Could not easily import previous code because of code's structure. Had to rewrite.

 
x, y = 5, 6
radius = 12
rec_width = 2* radius 
rec_height = 2 * radius 
cir_x, cir_y = x, y
            
def Monte_Carlo(a, b, w, h, r, x, y, n):
    A = 0
    for i in range(n):
        x_1 = random.uniform(a - w/2, a + w/2)
        y_1 = random.uniform(b - h/2, b + h/2)
        if math.sqrt((x_1 - x)**2 + (y_1 - y)**2) <= r:
            A += 1
    pi = (A * w * h )/ ( n * r**2)
    return pi
x1 = []
y1 = []
y2 = []
y_error = []
trials = int(input("\nHow many trials do you want to run to estimate pi from each datasize? "))
print("\nNow computing...\n")    
p = math.pi * (radius**2)/(rec_width *rec_height)
q = 1-p
i = 4
Loss = True
start = clock()
while Loss:
    n = 3**i
    pi = 0
    for m in range(trials):
             Pi = Monte_Carlo(x, y, rec_width, rec_height, radius, cir_x, cir_y, n)
             pi += Pi
    pi = pi/trials
    T = pi * 2160 * (1.4)
    Max_error = st.norm.ppf(1-(1-0.95)/2) * math.sqrt(p * q/n)
    y_error += [Max_error]
    x1.append(math.log(n))
    y1.append(T)
    y2.append(Cost)
    i += 1
    loss = T - Cost
    if loss >= 0 and loss <= threshold:
        end = clock()
        print("Amount of time taken to reach this accuracy is", end - start, "and this is for a data size (number of darts) of", n)
        print("\nLoss made is", loss, "and amount spent will be", T)
        Loss = False

plt.plot(x1, y1, 'b')
plt.plot(x1, y2, 'r')
plt.errorbar(x1, y1, yerr = y_error , ecolor = 'k', elinewidth = 2, capsize = 3, fmt='o')
plt.xlabel("Size of dataset (in log-scale)")
plt.ylabel("Cost for particular Pi")
plt.legend(['Cost for particular Pi', 'Actual Cost for Pi Value (to the 15th d.p.)'])
plt.show()
