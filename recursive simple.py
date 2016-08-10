#Recursive function to get largest number in list
list = [56, 345, 322, 6677, 798, 4, 322, 5667, 6676, 322, 7777, 566, 2322]
largest = list[0] #initially assigns the first term as the largest
x = 1 #index position
def large_num(largest, list, x):
    if largest < list[x]: #compares with next
        largest = list[x]
    if x == (len(list) - 1):
        print ("Largest number is", largest)
        return (largest)
    x += 1 #increments value of index
    return (large_num(largest, list, x)) #checks largest against next value

large_num(largest, list, x) #runs function
