'''
Type I and Type II Errors
'''

import numpy as np
import random
import math
from scipy.stats import norm
significance_level = 0.05 #sets significance level
population1 = np.random.choice(500, 10000) #creates population
mean1 = np.mean(population1) #population1 mean
population2 = np.random.choice(500, 10000) #creates population
mean2 = np.mean(population2) #population2 mean
def significant(pop, size):
    population_mean = np.mean(pop)
    sample = np.random.choice(pop, (size, ))
    sample_mean = np.mean(sample)
    SE = (np.std(pop))/float((math.sqrt(size)))
    z = (sample_mean - population_mean)/SE #using population as the standard/null figure
    p_value = 1 - (norm.cdf(z, loc=0, scale=1))
    return p_value
def main():
    error = 0 #calculates error
    for i in range(1000):
        error1 = ''
        error2 = ''
        p1 = significant(population1, 100) #where 100 is population size
        if p1 < 0.05:
            error1 = 1
        else:
            error1 = 0
        p2 = significant(population2, 100)
        if p2 < 0.05:
            error2 = 1 #error checker for population 2
        else:
            error2 = 0
        if error1 == 1 or error2 == 1: #making a type 1 error on either p value
            error += 1
    proportion = (error/float(1000))*100
    return proportion

print ("Percentage of error is", main(), "%")

