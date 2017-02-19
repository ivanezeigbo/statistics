#import pdb; pdb.set_trace()
import random
import math
import matplotlib.pyplot as plt
import scipy.stats as st

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
for i in range(4, 16):
    n = 3**i
    pi = 0
    for i in range(trials):
             Pi = Monte_Carlo(x, y, rec_width, rec_height, radius, cir_x, cir_y, n)
             pi += Pi
    pi = pi/trials
    Max_error = st.norm.ppf(1-(1-0.95)/2) * math.sqrt(p * q/n)
    y_error += [Max_error]
    x1.append(math.log(n))
    y1.append(pi)
    y2.append(math.pi)

plt.plot(x1, y1, 'b')
plt.plot(x1, y2, 'r')
plt.errorbar(x1, y1, yerr = y_error, ecolor = 'k', elinewidth = 2, capsize = 3, fmt = 'o')
plt.xlabel("Size of dataset (in log-scale)")
plt.ylabel("Value of pi")
plt.legend(['Estimated Pi', 'Actual Pi Value (to the 15th d.p.)'])
plt.show()
