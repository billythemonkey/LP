"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

import numpy as np
import math

def list_of_words(s):
    l1 = s.split(' ')
    return l1

def set_of_words(s):
    s1 = set(list_of_words(s))
    return s1

def num_of_repeated_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    s = set(s)
    for x in s:
        if x in vowels:
            count += 1
    return count

def intersect_strings(s1, s2):
    s1 = set_of_words(s1)
    
    s2 = set_of_words(s2)
    
    result = s1.intersection(s2)
    return len(result)

if __name__ == "__main__":
    value = "Andrei"
    s1 = "Andrei o grande!"
    s2 = "Andrei o maior"
    l1 = list_of_words(value)
    print(l1)
    s = set_of_words(value)
    print(s)
    
    print(num_of_repeated_vowels(value))
    
    result = intersect_strings(s1, s2)
    print(result)
    
    