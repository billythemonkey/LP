"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""
import numpy as np

# Alínea a)

def recursive_random_number_list(l1, n):
    i = np.random.randint(0, 101)
    if n > 0:
        l1.append(i)
        n -= 1
        recursive_random_number_list(l1, n)
    return l1

# Alínea b)

def recursive_odd_numbers_sum(l1, item):
    global sum
    if item > 0:
        item -= 1
        if(l1[item] % 2 != 0):
            sum = sum + l1[item]
        recursive_odd_numbers_sum(l1, item)
    return sum

# Alínea c)

def f1(value):
    return value - 1

# Alínea d)

def recursive_subtract_odd_list(l1, size, f1):
    
    global l2
    
    if size > 0:
        size -= 1
        if l1[size] % 2 != 0:
            l2.append(f1(l1[size]))
        recursive_subtract_odd_list(l1, size, f1)
    
    return l2

if __name__ == "__main__":
    list = []
    random_list = recursive_random_number_list(list, 10)
    sum = 0
    l2 = []
    print(random_list,len(random_list))
    
    print(recursive_odd_numbers_sum(random_list, len(random_list)))
    
    print(recursive_subtract_odd_list(random_list, len(random_list), f1))
    