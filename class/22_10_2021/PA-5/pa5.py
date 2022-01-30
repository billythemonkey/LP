"""
Author: Andrei Razvan Oproiu
Date: Fri Oct 22 2021
"""

import numpy as np
# import sympy as sp

# Alínea a)

def eq_lineares( a, b ):
    s = np.linalg.solve(a, b)
    return s


# Alínea b)

def determinante(a):
    s = np.linalg.det(a)
    return s

# Alínea c)

def cramer(a):
    inv = np.linalg.inv(a)
    return np.dot(inv, a)

# def cramer_sp():
#     s = sp.Matrix([[4,3,2],[-2,2,3],[3,-5,2]])
#     inv = s.inv()
#     return s * inv


if __name__ == "__main__":
    
    a = np.array([[4,3,2],[-2,2,3],[3,-5,2]])
    b = np.array([[25],[-10],[-4]])
    
    print(eq_lineares(a, b))
    print(determinante(a))
    print(cramer(a))