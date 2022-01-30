"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

import numpy as np


def normal_random_distribution(n,sigma = 2.0):
    l1 = np.random.normal(0.0, sigma, n)
    return l1

def remove_negatives_from_list(l1):
    l2 = []
    for x in l1:
        if x >= 0:
            l2.append(x)
    return l2

def sum_of_positives_in_list(l1):
    sum = 0
    for x in l1:
        if x >= 0:
            sum += x
    return sum

def sum_even_first_digit(l1):
    sum = 0
    for x in l1:   
        z = int(x)
        if z < 0:
            z = z * (-1)
            if int(str(z)) % 2 == 0:
                sum += x
        else:
            if int(str(z)) % 2 == 0:
                sum += x
    return sum

if __name__ =="__main__":

    list = normal_random_distribution(10)
    print(list)
    positive_list = remove_negatives_from_list(list)
    print(positive_list)
    sum = sum_of_positives_in_list(list)
    print(sum)
    even_digit_sum = sum_even_first_digit(list)
    print(even_digit_sum)