#import pdb; pdb.set_trace()
import random
import math
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
from time import clock

x, y = eval(input("What is the coordinate of the center of the board? Please represent in the form: x, y " ))
rec_width = float(input("What is the width of the rectangle " ))
rec_height = float(input("What is the height of the rectangle " ))
radius = float(input("What is the radius of the circle " ))
print("\nThis program may work under the assumption that the circle is located at the center of the rectangle, if you please. If not, you can tell us the coordinates of the circle's center")
Continue = True
while Continue: 
    center = input("\nIs the circle exactly at the center of the rectangle? Please reply either Yes or No: ")
    if center =='Yes':
        cir_x, cir_y = x, y
        Continue = False
    elif center == 'No':
        cir_x, cir_y = eval(input("Please tell us the coordinate of the center of the circle. Put this in the form: x, y "))
        Continue = False
    else:
        print("Please follow the instructions.")
            
Valid = False
    
while not Valid:
    if cir_x + radius <= x + rec_width/2 and cir_x - radius >= x - rec_width/2 and cir_y + radius <= y + rec_height/2 and cir_y + radius >= y - rec_width/2:
        Valid = True
    else:
        print("\nPlease choose a valid radius, and coordinate of the center of the circle")
        radius = float(input("What is your radius "))
        cir_x, cir_y = eval(input("Please tell us the coordinate of the center of the circle. Put this in the form: x, y "))


def Monte_Carlo(a, b, w, h, r, x, y, n):
    start = clock()
    A = 0
    for i in range(n):
        x_1 = random.uniform(a - w/2, a + w/2)
        y_1 = random.uniform(b - h/2, b + h/2)
        if math.sqrt((x_1 - x)**2 + (y_1 - y)**2) <= r:
            A += 1
    pi = (A * w * h )/ ( n * r**2)
    end = clock()
    return pi, end - start
x1 = []
y1 = []
y2 = []
y_error = []
accuracy = []
timed = []
#n_size = []
trials = int(input("\nHow many trials do you want to run to estimate pi from each datasize? "))
print("\nNow computing...\n")

pi_value = str(math.pi)
p = math.pi * (radius**2)/(rec_width *rec_height)
q = 1-p

for i in range(0, 18):
    Accuracy = 0
    n = 3**i
    pi = 0
    Time = 0
    for ml in range(trials):
             Pi, time = Monte_Carlo(x, y, rec_width, rec_height, radius, cir_x, cir_y, n)
             pi += Pi
             Time += time
    pi = pi/trials
    Time = Time/trials
    timed.append(Time)
    m = str(pi)
    Compare = True
    k = 0
    while Compare:
        if k == 1:
            if m[k] != pi_value[k]:
                Accuracy -= 1
                Compare = False
        elif m[k] == pi_value[k]:
            Accuracy += 1
        else:
            Compare = False
        k += 1
    accuracy.append(Accuracy)    
    Max_error = st.norm.ppf(1-(1-0.95)/2) * math.sqrt(p * q/n)
    y_error += [Max_error]
    x1.append(math.log(n))
    #n_size.append(n)
    y1.append(pi)
    y2.append(math.pi)



plt.plot(x1, y1, 'b')
plt.plot(x1, y2, 'r')
plt.errorbar(x1, y1, yerr = y_error, ecolor = 'k', elinewidth = 2, capsize = 3, fmt='o')
plt.xlabel("Size of dataset (in log-scale)")
plt.ylabel("Value of pi")
plt.legend(['Estimated Pi', 'Actual Pi Value (to the 15th d.p.)'])
plt.show()

slope, intercept, r_value, p_value, std_err = st.linregress(x1, accuracy)
slope1_2, slope1_1, intercept1 = np.polyfit(x1, accuracy, 2)

plt.plot(x1,accuracy, 'b')
plt.plot([min(x1), max(x1)], [slope * min(x1) + intercept, slope* max(x1) + intercept], 'g')
plt.xlabel('Size of dataset (in log-scale)')
plt.ylabel('Accuracy')
plt.legend(['Accuracy Est.', 'Regression Line'])
plt.title('Accuracy Estimation Against Data Size')
plt.show()



'''
To attain an accuracy of 8 dec places - (or accuracy of 9)
'''
dp = int(input("How many decimal places should this be approximated? "))

'''
Will not use this because the graph of accuracy is a quadratic graph; hence, non linear
'''
lin_x = (dp - intercept)/slope #used the equation of a line
print('For a linear relationship, we need a data size of the order, e (natural number) to the power of', round(lin_x), 'that is about', round(math.exp(lin_x)), 'darts.')

timeslop2, timeslop1, timeint = np.polyfit(x1, timed, 2)
fit = np.polyfit(x1, timed, 2)
pl = np.poly1d(fit)

plt.plot(x1, timed, x1, pl(x1))
plt.plot(x1, timed)
plt.xlabel('Data Size (in log scale)')
plt.ylabel('Time')
plt.legend(['Time Taken', 'NonLinear Regression'])
plt.title('Time Against Data Size')
plt.show()

#Calculating time taken
non_time = (lin_x**2 * timeslop2) + (lin_x * timeslop1) + timeint
print("Calculated time taken to run this large N is about", int(round(non_time/60)), "minutes.")

#non_x = (math.sqrt(slope1_1**2 - (4 * slope1_2 * (intercept1 - dp)))- slope1_1)/ (2* slope1_2) #The Quadratic Formula
#print('\nFor a nonlinear relationship, we need a data size of the order, e (natural number) to the power of', round(non_x), 'that is about', round(math.exp(non_x)), 'darts.')
