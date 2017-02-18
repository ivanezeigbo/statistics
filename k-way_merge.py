#import pdb; pdb.set_trace()
from time import clock
import random; import math
random.seed(501)
import matplotlib.pyplot as plt

def insertion(list):
    for i in range(1,len(list)):    
        w = i #w is for comparing                   
        while w > 0 and list[w] < list[w-1]: 
            list[w], list[w-1] = list[w-1], list[w] #swap
            w -= 1 
    return list

def merging(first_half, second_half):
    sorted_list = []
    i ,j = 0, 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            sorted_list.append(first_half[i])
            i += 1
        else:
            sorted_list.append(second_half[j])
            j += 1
    sorted_list += first_half[i:]
    sorted_list += second_half[j:]
    return sorted_list
    
def merge(divide):
    ind = 0
    ind2 = ind + 1
    sorted_list = merging(divide[ind], divide[ind2])
    for g in range(2, len(divide)):
        ind2 += 1
        sorted_list = merging(sorted_list, divide[ind2])
    return sorted_list
        
    
 

def mergesort(list):
    if len(list) < k: #if list less than k, algorithm performs insertion/shell sort
        if len(list) == 1:
           return list
        if len(list) == 0: #in case there are no elements in list
            print("No element in list")
            return list
        else:
            return insertion(list)
    cutoff = int(round(len(list) / k)) #integar call here also allows for times when you have an odd list
    copy = cutoff
    divide = []
    divide.append(mergesort(list[:cutoff]))
    indx = cutoff * 2
    while indx <= len(list):
        divide.append(mergesort(list[copy : indx]))
        copy, indx = indx, indx + cutoff
    if copy != len(list):
        divide.append(mergesort(list[copy:]))
    return merge(divide)

x = [] #x coordinate
y = [] #y coordinate

A = random.sample(range(-2000, 2001), 1000)

for k in range(2, 31):
    run_time = 0
    for i in range(1000):
        start = clock()
        mergesort(A)
        end = clock()
        run_time += end - start
    run_time = run_time/1000
    x.append(k)
    y.append(run_time)

plt.plot(x, y, 'r')
plt.ylabel("Running time for k")
plt.xlabel("Values of k")
plt.title("Graph for running time for k")
plt.show()

#end = clock()
#print("\nRunning time is:", end - start)
