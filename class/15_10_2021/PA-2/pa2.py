"""
Author: Andrei Razvan Oproiu
Date: Tue Oct 19 2021
"""

# Alínea a)

from typing import Text


def count_vogals(string):
    counter = 0
    vogals = ['a', 'e', 'i', 'o', 'u']
    for l in string:
        for v in vogals:
            if l.lower() == v:
                counter += 1
    return counter


# Alínea b)

def change_even_to_a(string):
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for s in string:
        for n in numbers:
            if s == str(n) and n % 2 == 0:
                
                string = string.replace(s, 'A')
    return string

# Alínea c)

def sum_digits(input):
    counter = 0
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for s in input:
        for n in numbers:
            if s == str(n):
                counter += n
    
    return counter

# Alínea d)

def repeat_string(string, n):
    counter = 0
    frase = ""
    while n > counter:
        frase += string
        counter += 1
        
    return frase
        

if __name__ == "__main__":
    # print("Hello World!")
    testA = "Andrei Razvan Oproiu"
    a = count_vogals(testA)
    print(a)
    
    testB = "1C 02146"
    b = change_even_to_a(testB)
    print(b)
    
    testC = "123dufjfj3490"
    c = sum_digits(testC)
    print(c)
    
    testD = "OLA "
    d = repeat_string(testD, 10)
    print(d)