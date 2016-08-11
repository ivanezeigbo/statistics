# Function my_mean: input is a list and output is the mean of that list
def my_mean(a):
    return sum(a)/float(len(a))

# Function my_median: input is a list and output is the median of that list
def my_median(a):
    a.sort()
    l = len(a)
    if l % 2 == 0:
        median = (a[(l/2)-1]+a[l/2])/float(2)
    else: 
        median = a[l/2]
    return median 

#Function my_mode: input is a list and output is the mode of that list
def my_mode(a):
    count = [[x, a.count(x)] for x in set(a)] 
    mode = []
    index = 0
    for i in range(1, len(count)):
        if (count[i][1]>=count[index][1]):
            index = i
    if(count[index][1] == 1): 
        mode = ["No mode"]
    else: 
        for j in range(0, len(count)):
            if (count[j][1]==count[index][1]):
                mode.append(count[j][0])
    return mode

#Function my_SD: input is a list and output is the standard deviation of that list 
import math 
def my_SD(a):
    sum = 0
    mean = my_mean(a)
    for i in range(0, len(a)):
        each = pow((a[i]- mean),2)
        sum += each
    SD = math.sqrt(sum/len(a))
    return SD 

#Function my_cc: input is a list of tuples which contain the ordered data of two variables
#and output is the correlation coefficient of that two variables
def my_cc(a): 
    var1 = [x[0] for x in a]
    var2 = [x[1] for x in a]
    mean1 = my_mean(var1)
    mean2 = my_mean(var2)
    SD1 = my_SD(var1)
    SD2 = my_SD(var2)
    standard1 = []
    standard2 = []
    if (SD1 == 0 or SD2 == 0): 
    #When either SD equals to 0, we cannot divide by 0 and it makes sense because no variable that has standard deviation 0 could possibly be correlated with another non-constant variable
    #then there is no correlation
        cc = 0 #I can put it "undefined" here, but later we have to sort the variable based on correlation coeffient, then it is more comfortable to put r as 0 here
    else:
        for k in var1: 
            standard1.append((k-mean1)/SD1)
        for h in var2:
            standard2.append((h-mean2)/SD2)
        sum = 0
        for l in range(0, len(a)):
            sum += standard1[l]*standard2[l]
        cc = sum/len(a)
    return cc
import math 
def my_SD(a):
    sum = 0
    mean = my_mean(a)
    for i in range(0, len(a)):
        each = pow((a[i]- mean),2)
        sum += each
    SD = math.sqrt(sum/len(a))
    return SD 

#Function my_cc: input is a list of tuples which contain the ordered data of two variables
#and output is the correlation coefficient of that two variables
def my_cc(a): 
    var1 = [x[0] for x in a]
    var2 = [x[1] for x in a]
    mean1 = my_mean(var1)
    mean2 = my_mean(var2)
    SD1 = my_SD(var1)
    SD2 = my_SD(var2)
    standard1 = []
    standard2 = []
    if SD1 == 0 or SD2 == 0:
        cc = 0
    else:
        for k in var1: 
            standard1.append((k-mean1)/SD1)
        for h in var2:
            standard2.append((h-mean2)/SD2)
        sum = 0
        for l in range(0, len(a)):
            sum += standard1[l]*standard2[l]
        cc = sum/len(a)
    return cc


def two_variable(tuple_list):
    new_l = [] #New_l is a list of small lists. Each small list contains names of two variables and the correlation coefficient
#This two for_loop helps us make all the pairs of variables without repeating
#For example, if we have 3 variables, it will pair var1 and var2 (p=0,q=1), var1 and var3 (p=0,q=2), var2 and var3 (p=1,q=2)
#q should be more than p all the time to avoid repeating
    num_var = len(tuple_list[0])
    for p in range(0, num_var-1):
        for q in range(1, num_var):
            if q > p: 
                l = []
                two_var = [(x[p],x[q]) for x in tuple_list]
                new_l.append(two_var)
    return new_l
            
def aggregate_stats(tuple_list):
    num_var = len(tuple_list[0])  #Number of variables: the length of the first tuple
    new_list = [] #I want this new list to have the format as a list of sublist  
    for i in range(0,num_var):
        sub_list = [] #I want sublist to contain: variable name, mean, median, mode, standard deviation of data of that variable
        var_name = tuple_list[0][i] #Var_name is variable name, the first element of every sublist
        sub_list.append(var_name) #Add var_name to one sublist
        one_var = [] #I want this one_var to contain the data of each variable (does not include the name)
        for j in range(1,len(tuple_list)):
            one_var.append(tuple_list[j][i]) #Append data to each variable
        sub_list.append(my_mean(one_var)) #Calculate mean of data of each variable, append the value to list
        sub_list.append(my_median(one_var)) #Calculate median of data of each variable, append the value to list
        sub_list.append(my_mode(one_var)) #Calculate mode of data of each variable, append the value to list
        sub_list.append(my_SD(one_var)) #Calculate standard deviation of data of each variable, append the value to list
        new_list.append(sub_list) #Append list to new_list so that new_list contains a list of list, each list contains information about one variable
#When we print new_list, we can get thing like: 
#[['temp', 52.33, 52, 'No mode', 2.05], ['pressure', 11.0, 11, 'No mode', 0.82],['precipitation', 0.13, 0.1, [0.1], 0.047]]
    sorted_list = sorted(new_list, key=lambda var: var[0]) #I sort new_list based on the name of variable (in alphabetical order), then key is the first element
#The sorted_list should look like:
#[['precipitation', 0.13, 0.1, [0.1], 0.047],['pressure', 11.0, 11, 'No mode', 0.82],['temp', 52.33, 52, 'No mode', 2.05]]
#This for_loop loops through each element of the sorted_list and print out the name, the mean, the median, the mode and the standard deviation of each variable
    for m in range(0, num_var):
        print "Variable name: %s" % sorted_list[m][0]
        print "Mean = %s" % sorted_list[m][1]
        print "Median = %s" % sorted_list[m][2]
        print "Mode = "+','.join(str(e) for e in sorted_list[m][3])
        print "Standard deviation = %s" % sorted_list[m][4]


    new_l = [] #New_l is a list of small lists. Each small list contains names of two variables and the correlation coefficient
#This two for_loop helps us make all the pairs of variables without repeating
#For example, if we have 3 variables, it will pair var1 and var2 (p=0,q=1), var1 and var3 (p=0,q=2), var2 and var3 (p=1,q=2)
#q should be more than p all the time to avoid repeating
    for p in range(0, num_var-1):
        for q in range(1, num_var):
            if q > p: 
                l = []
                two_var = [(x[p],x[q]) for x in tuple_list] 
#two_var is a list of tuples, 
#where the first tuple contains the two variables names and subsequent tuples contain the ordered data
                cut = [] 
#I want "cut" to contain only the data, not the variables names 
#so that I can use function my_cc for "cut" to calculate the correlation coefficient 
                for y in range(1,len(tuple_list)):
                    cut.append(two_var[y])
                r = my_cc(cut)
                l.append(two_var[0]) #Append the name of variable to each small list
                l.append(r) #Append the correlation coefficient to each small list
                new_l.append(l) #Append each small list to the new lis
    sorted_l = sorted(new_l, key=lambda var: abs(var[1])) #I sort new_l based on the absolute value of r, then key is the second element 
#This for_loop loops through each element of the sorted_l and print out the names of two variables and the relative r
    for x in sorted_l: 
        print "Variable 1: %s" % x[0][0]
        print "Variable 2: %s" % x[0][1]
        print "Correlation Coefficient = %s" % x[1]
        

#Test aggregate_stats 
aggregate_stats([('temp', 'pressure', 'precipitation'),(50, 10, 0.1),(55, 11, 0.1)])
aggregate_stats([('annual average temperature anomaly', 'annual precipitation anomaly', 'Palmer Drought Index anomaly', 'cooling degree days anomaly', 'heating degree days anomaly'), (-0.41, -0.24, 0.34, 22, 115), (-0.36, 0.39, 0.2, -18, 2), (-0.65, 1.76, 1.58, -57, 136), (0.27, 5.02, 4.45, 25, -223), (0.24, 0.68, 3.07, -81, -154), (-0.52, 3.09, 3.32, -34, -86), (-0.55, -3.63, -0.75, -173, 148), (0.53, 0.5, -1.55, 88, 14), (-0.97, 0.2, 0.52, 31, 360), (-1.14, 2.81, 1.83, -87, 192), (0.37, -1.67, -0.8, 110, 101), (1.1, 0.02, -1.16, 9, -92), (-0.67, 3.92, 2.97, -58, 17), (-0.14, 4.82, 4.61, 48, 19), (-0.04, 1.46, 3.55, 17, -105), (-0.72, 0.03, 0.56, 7, 23), (1.3, 1.44, 1.74, 59, -344), (1.31, -0.93, -0.97, 72, -296), (0.61, -4.04, -3.91, 91, -8), (-0.18, -0.89, -1.25, -27, 47), (1.49, 2.23, -0.37, 76, -619), (1.14, 2.5, 0.75, 140, -445), (0.58, 1.32, 0.79, -135, -228), (-0.76, 2.68, 3.97, 23, 38), (0.85, 0.68, 1.74, 38, -191), (0.63, 2.75, 2.4, 103, -150), (-0.13, 3.76, 2.39, 8, 13), (0.18, 1.92, 3.9, -25, -138), (2.21, 3.95, 1.15, 236, -684), (1.86, -1.47, -0.54, 117, -516), (1.25, -1.72, -4.84, 70, -247), (1.68, -0.92, -3.27, 86, -470), (1.19, -0.89, -2.46, 190, -360), (1.24, 0.57, 0.18, 91, -175), (1.08, 3.31, 0.91, 32, -361), (1.62, 0.14, -0.31, 199, -349), (2.23, -0.12, -2.62, 172, -648), (1.63, -0.76, -2.05, 199, -412), (0.27, 1.3, -0.05, 85, -181), (0.37, 2.36, 0.85, 44, -189), (0.96, 1.43, 2.65, 256, -198), (1.16, 0.16, -0.56, 268, -348), (3.26, -2.41, -4.41, 291, -891), (0.41, 1.12, -0.62, 100, -178), (0.51, 0.9, 0.84, 85, -80)])
