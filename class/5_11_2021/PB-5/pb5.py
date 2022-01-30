"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

import numpy as np
import random
import string

def normal_distribution_list(n):
    return np.random.normal(0.0, 3.4, n)
   
def random_lower_case_char(n):
    c = ""
    while n > 0:
        c = c + random.choice(string.ascii_letters.lower())
        n -= 1
        
    return c

def random_int_tuple(n):
    a = np.random.uniform(0.0, 100.0,size=n)
    a = tuple(a.astype(int))
    return a
    
def even(n):
    return n * 2
def random_even_int_tuple(n):
    a = np.random.uniform(0.0, 100.0,size=n)
    a = tuple(a.astype(int))
    a = tuple(map(even, a))
    return a


if __name__ == "__main__":
    print(normal_distribution_list(10))
    print(random_lower_case_char(50))
    print(random_int_tuple(10))
    print(random_even_int_tuple(10))