import random
import math
import numpy as np
import matplotlib.pyplot as plt
def hash1(key, array):
    val = 0
    for i in range(len(key)):
         val += ord(key[i]) ** (i + 1)
    return val % len(array)

def hash2(key, array):
    random.seed(123)
    val = 0
    for t in range(len(key)):
        code = ord(key[t]) + (t **2 + t + 1)
        val += random.getrandbits(code) 
    return val % len(array)

random.seed(54)
n = 3000
array = random.sample(range(10000), n)    

length = int(round(2 * n/math.log(2)))#optimal size of array for 2 hash functions
#length = 10000
bloom = [0] * length


def INCLUDE_MEMBER(Input, bloom):
    index1 = hash1(str(Input), bloom) #calling first hash function
    index2 = hash2(str(Input), bloom) #calling second hash function
    bloom[index1], bloom[index2] = 1, 1 #assigning the index
    return bloom #returns Bloom_rum
	

def CHECK_MEMBER(Input, bloom):
    index1 = hash1(str(Input), bloom) #calling first hash function
    index2 = hash2(str(Input), bloom) #calling second hash function
    if bloom[index1] == 1 and bloom[index2] == 1: #checks if both equals 1
        return True
    else:
        return False

positive = []
theory = []
x = np.arange(1, n + 1, 1)
x1 = []
y1 = []
tt = []

def main(bloom, array,length):
    pos = 0
    for g in range(len(array)):
        x1.append(math.log10(g + 1))
        Input = array[g]
        if CHECK_MEMBER(Input, bloom):
            pos += 1
            positive.append(pos/(g + 1))
            y1.append(math.log10(pos/(g + 1)))
            theory.append((1 - math.exp(-2 * (g + 1)/length))**2)
            tt. append(math.log10(((1 - math.exp(-2 * (g + 1)/length))**2)))
            
        else:
            bloom = INCLUDE_MEMBER(Input, bloom)
            positive.append(pos/(g + 1))
            if pos == 0:
                y1.append(0)
            else:
                y1.append(math.log10(pos/(g + 1)))
            theory.append((1 - math.exp(-2 * (g + 1)/length))**2)
            tt. append(math.log10(((1 - math.exp(-2 * (g + 1)/length))**2)))

main(bloom, array, length)   

plt.plot(x, positive, 'b')
plt.plot(x, theory, 'r')
plt.xlabel('Size of N')
plt.ylabel('False positive (percentage)')
plt.legend(['Empirical Value', 'Theoretical Value'])
plt.title('False Positive Rate With Increasing N')
plt.show()

plt.plot(x1, positive, 'g')
plt.plot(x1, theory, 'r')
plt.xlabel('Size of N (log-scale)')
plt.ylabel('False positive (percentage)')
plt.legend(['Empirical Value', 'Theoretical Value'])
plt.title('False Positive Rate With Increasing N (log-scale)')
plt.show()

plt.plot(x, y1, 'k')
plt.plot(x, tt, 'r')
plt.xlabel('Size of N')
plt.ylabel('False positive (percentage)')
plt.legend(['Empirical Value', 'Theoretical Value'])
plt.title('False Positive Rate With Increasing N')
plt.show()
