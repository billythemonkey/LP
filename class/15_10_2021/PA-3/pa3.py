"""
Author: Andrei Razvan Oproiu
Date: Tue Oct 19 2021
"""

# Alínea a)
def third_deg_pol(list_of_coeficients):
    x = 1
    value = list_of_coeficients[0] * x ** 3 + list_of_coeficients[1] * x ** 2 + list_of_coeficients[2] + list_of_coeficients[3]
    return value

if __name__ == "__main__":
    print("Hello World!")