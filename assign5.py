import os
import pandas as pd
import numpy as np
from sklearn.neighbors.kde import KernelDensity
from sklearn.neighbors import kde
import matplotlib.pyplot as plt

data = pd.read_csv("anonymized.csv")
data['month'] = [s[2:] for s in data.Date]
counts = data.Amount.groupby([data['month']]).agg({'count'})
counts = np.array(counts).reshape(-1, 1)
data['day'] = [s[:2] for s in data.Date]
day = np.array(data['day']).reshape(-1, 1)
trans = np.array(data.Amount).reshape(-1, 1)

X1 = np.linspace(0, 120, 1000)[:, np.newaxis]
X2 = np.linspace(0, 32, 1000)[:, np.newaxis]
X3 = np.linspace(min(trans), max(trans)+1, 1000)[:, np.newaxis]
for kernel in ['gaussian', 'tophat']:
    kde1 = KernelDensity(kernel=kernel, bandwidth=5).fit(counts)
    kde2 = KernelDensity(kernel=kernel, bandwidth=5).fit(day)
    kde3 = KernelDensity(kernel=kernel, bandwidth=5).fit(trans) 
    log_dens1 = kde1.score_samples(X1)
    log_dens2 = kde2.score_samples(X2)
    log_dens3 = kde3.score_samples(X3)
    samples = int(kde1.sample(1)[0][0])
    print('There are', samples, 'transactions', '\n')
    num_days = kde2.sample(samples)
    for m in range(len(num_days)):
        num_days[m] = int(round(num_days[m][0]))
        while num_days[m] <= 0 or num_days[m] > 31:
            num_days[m] = int(round(kde2.sample(1)[0][0]))           
    print('The days are:')
    print(num_days, '\n')
    num_trans = kde3.sample(samples)
    print('The transactions are:')
    print(num_trans, '\n')

    #Plotting density of number of transactions in a month
    plt.plot(X1[:, 0], np.exp(log_dens1), '-',
            label="kernel = '{0}'".format(kernel))
    plt.title("Density of number of transactions in a month")
    plt.legend(loc='upper right')
    plt.plot(counts, -0.0005 - 0.001 * np.random.random(len(counts)), '+k')
    #plt.show()
    
    #Plotting Density of days in the month
    plt.plot(X2[:, 0], np.exp(log_dens2), '-',
            label="kernel = '{0}'".format(kernel))
    plt.title("Density of days in the month")
    plt.legend(loc='upper right')
    plt.plot(day, -0.0005 - 0.001 * np.random.random(len(day)), '+k')
    #plt.show()
    
    #Plotting Density of size of transactions
    plt.plot(X3[:, 0], np.exp(log_dens3), '-',
            label="kernel = '{0}'".format(kernel))
    plt.title("Density of size of transactions")
    plt.legend(loc='upper right')
    plt.plot(trans, -0.0005 - 0.001 * np.random.random(len(trans)), '+k')
    #plt.show()

    N = 10000
    new_trans = kde3.sample(N)
    count_1 = 0
    count_2 = 0
    for m in new_trans:
        first_num = str(str(m[0])[0])
        if first_num == '-':
            first_digit = str(str(m[0])[1])
        else:
            first_digit = first_num
        if first_digit == '1':
            count_1 += 1
        if first_digit == '2':
            count_2 += 1
    print ('Number of digits beginning in 1 for', kernel, 'kernel is', count_1*100/N)
    print ('Number of digits beginning in 2 for', kernel, 'kernel is', count_2*100/N)
     




