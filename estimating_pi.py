#import pdb; pdb.set_trace()
import random
import math
def inputs():
    x, y = eval(input("What is the coordinate of the center of the board? Please represent in the form: x, y " ))
    rec_width = float(input("What is the width of the rectangle " ))
    rec_height = float(input("What is the height of the rectangle " ))
    radius = float(input("What is the radius of the circle " ))
    print("\nThis program works under the assumption that the circle is located at the center of the rectangle. If this is not correct, you can tell us the coordinates of the circle's center")
    Continue = True
    while Continue: 
        center = input("\nIs the circle exactly at the center of the rectangle? Please reply either Yes or No ")
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
            
    n = int(input("\nHow many darts should we throw? "))
    print("\nNow computing...\n")
    return Monte_Carlo(x, y, rec_width, rec_height, radius, cir_x, cir_y, n)

def Monte_Carlo(a, b, w, h, r, x, y, n):
    A = 0
    for i in range(n):
        x_1 = random.uniform(a - w/2, a + w/2)
        y_1 = random.uniform(b - h/2, b + h/2)
        if math.sqrt((x_1 - x)**2 + (y_1 - y)**2) <= r:
            A += 1
    print("The ratio of the circle to the rectangle is", A/n)
    pi = (A * w * h )/ ( n * r**2)
    print( "\nValue of pi is", pi)
    return

inputs()   
