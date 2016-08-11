'''
Simulating predator/prey relationship by the Lotka-Volterra Equation using Euler's Method
you can compare this result to NetLogo's Wolf-Sheep Predation Model

'''
import matplotlib.pyplot #import matplotlib.pyplot for graph plotting

#function calculates the new population density of prey and predator and plots its graph.

def LotkaVolterra():
    x = eval(input("Please provide a value for the population density (between 0 and 1) of prey: "))#x is the population density of the prey
    t = 0.0 #t is the time
    y = eval(input("Please provide a value for the population density (between 0 and 1) of predator: "))#y is the population density of the predator
    h = eval(input("Please provide a value for the time step: ")) #h is the time step
    a = eval(input("Please provide a value for the reproduction rate (between 0 and 1) of prey: ")) #a is the reproduction rate of the prey
    b = eval(input("Please provide a value for the frequency of encounter (between 0 and 1) between predator and prey: ")) #b is the frequency of encounters between the prey and the predator
    o = eval(input("Please provide a value for the growth rate(between 0 and 1) of predator: ")) #o is the growth rate of the predator
    v = eval(input("Please provide a value for the mortality rate (between 0 and 1) of predator: "))#mortality rate of the predator

    time = [0.0] #created a list, time, and assigned it the initial t
    prey = [x] #created a list, prey, and assigned it the initial x
    predator = [y] #created a list, predator, and assigned it the initial y
    while t >= 0 and t < 100: #for only up to 100 time steps
        t += h #increments time by time step
        x1 = ((((a*x) - (b*x*y)) * h) + x) #assigns new x value, i.e. x(t + h) as x for next iteration
        y1 = ((((o*y*x) - (v*y)) * h) + y) #same as above
        x = x1
        y = y1
        if float(x) > 0.0: #prevents production of negative numbers
            pass
        else:
            if int(x) <= 0:
                x = 0
        if float(y) > 0.0:
            pass
        else:
            if int(y) <= 0:
                y = 0
        time.append(t) #appends new time
        prey.append(x) #appends new x
        predator.append(y) #appends new y

        '''
            You can uncomment this if you wish!
            '''
        #print ("Sheeps are about", int(x * 100), "in number and wolves are about", int(y * 100), "in number, at time", str(t) + ".")
        if x == 0 and y == 0: #stops function if both prey and predator population density decimates to zero.
            matplotlib.pyplot.plot(time, prey, color = 'blue') #plots prey's population density against time, t.
            matplotlib.pyplot.plot(time, predator, color = 'red') #plots predator population density against time, t.
            matplotlib.pyplot.show()
            return x, y, t
        
    matplotlib.pyplot.plot(time, prey, color = 'blue') #plots prey's population density against time, t.
    matplotlib.pyplot.plot(time, predator, color = 'red') #plots predator population density against time, t.
    matplotlib.pyplot.show()
    
LotkaVolterra() #runs function.
