"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

import numpy as np
import math

def even_random_ints(n):
    l = []
    
    while len(l) < n:
        x = np.random.randint(0, 51)
        if x % 2 == 0:
            l.append(x)
    
    return l

def floats_list (list):
    l2 = []
    for item in list:
        try:
            l2.append(math.sqrt(item))
        except:
            l2.append(0.0)
            
    return l2

def triple_value(value):
    return value * 3

def map_int_list(l1):
    result = map(triple_value, l1)
    l2 = []
    for x in result:
        l2.append(x)
    
    return l2

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False
    
def filter_even_numbers(l1):
    f = filter(is_odd, l1)
    l2 = []
    for x in f:
        l2.append(x)
    return l2

if __name__ == "__main__":

    even_list = even_random_ints(20)
    print(even_list)
    list = np.random.randint(-50, 51, 10)
    print(list)
    sqrt_list = floats_list(list)
    print(sqrt_list)
    triple_list = map_int_list(even_list)
    print(triple_list)
    filtered_list = filter_even_numbers(list)
    print(filtered_list)
    