from time import clock
import random
import matplotlib.pyplot as plt
random.seed(5001)
def first(list):
    def merge(first_half, second_half):
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
        
     

    def mergesort(list):
        if len(list) < 3:
            if len(list) == 0: #in case there are no elements in list
                print("No element in list")
                return list
            if len(list) == 2:
                if list[1] < list[0]:
                    list[1], list[0] = list[0], list[1]
            return list
        cutoff = int(round(len(list) / 3)) #integar call here also allows for times when you have an odd list
        first = mergesort(list[:cutoff])
        second = mergesort(list[cutoff: cutoff*2])
        third = mergesort(list[cutoff*2 :])
        return merge(merge(first, second), third)
    mergesort(list)

def second(list):
    def merge(first_half, second_half, third_half):
        sorted_list = []
        
        i ,j , k = 0, 0, 0
        while (i < len(first_half) and j < len(second_half)) and (k < len(third_half)):
            if first_half[i] <= second_half[j] and first_half[i] <= third_half[k]:
                sorted_list.append(first_half[i])
                i += 1
            elif second_half[j] < first_half[i] and second_half[j] <= third_half[k]:
                sorted_list.append(second_half[j])
                j += 1
            else:
                sorted_list.append(third_half[k])
                k += 1
        if i >= len(first_half):
            return merge_two_way(second_half, third_half, j, k, sorted_list)
        elif j >= len(second_half):
            return merge_two_way(first_half, third_half, i, k, sorted_list)
        elif k >= len(third_half):
            return merge_two_way(first_half, second_half, i, j, sorted_list)
                    
        
    def merge_two_way(first_half, second_half, i, j, sorted_list):

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
     

    def mergesort(list):
        if len(list) < 3:
            if len(list) == 0: #in case there are no elements in list
                print("No element in list")
                return list
            if len(list) == 2:
                if list[1] < list[0]:
                    list[1], list[0] = list[0], list[1]
            return list
        cutoff = int(round(len(list) / 3)) #integar call here also allows for times when you have an odd list
        first = mergesort(list[:cutoff])
        second = mergesort(list[cutoff: cutoff*2])
        third = mergesort(list[cutoff*2 :])
        return merge(first, second, third)
    
    mergesort(list)
x = []
First = []
Second = []

for q in range(0, 6):
    size = 10**q
    A = random.sample(range(-2*size, 2*size), size)
    x.append(size)
        
    start1 = clock()
    first(A)
    end1 = clock()
    run_time1 = end1 - start1
    First.append(run_time1)

    start2 = clock()
    second(A)
    end2 = clock()
    run_time2 = end2 - start2
    Second.append(run_time2)

plt.plot(x, First, 'r', label = 'Recursion - three way sort')
plt.plot(x, Second, 'b', label = 'Three-way Revised')
plt.xlabel("Size of dataset")
plt.ylabel("Running time")
plt.title("Running time for two versions of three way merge sort")
plt.legend(["Recursion - three way sort", 'Three-way Revised'])
plt.show()
    

    
