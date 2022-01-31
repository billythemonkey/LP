"""
Author: Andrei Razvan Oproiu
Date: Mon Jan 31 2022
"""
from distutils.fancy_getopt import wrap_text
import json
import csv
import numpy as np

def serialize_dict(file_path, d):
    with open(file_path, "w") as outfile:
        json.dump(d, outfile, indent = 4)
        

def get_data_from_file(file_path):
    file = open(file_path)
    csvreader = csv.reader(file)
    result = []
    for row in csvreader:
        result.append(tuple(row))
        
    file.close()
    return result

def csv_sum(file_path):
    sum = 0
    with open(file_path, "r") as file:
        for line in file:
            value = int(line[len(line) - 2])
            print(value)
            sum =  sum + value
            
    return sum

def random_csv(file_path):
    numbers = np.random.uniform(size = 100)
    with open(file_path, "w") as file:
        writer = csv.writer(file, delimiter= ',')
        
        #print(numbers.tolist())
        writer.writerow(numbers.tolist())


if __name__ == "__main__":
    ex_1 = {
        "a": "b",
        "c": 3
    }
    serialize_dict("class/12_11_2021/PC-2/serial_dict.json",ex_1)
    
    ex_2 = get_data_from_file("class/12_11_2021/PC-2/tuples.csv")
    print(ex_2)
    
    ex_3 = csv_sum("class/12_11_2021/PC-2/csv_sum.csv")
    print(ex_3)
    
    ex_4 = random_csv("class/12_11_2021/PC-2/rand_csv.csv")