"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

import string
from unittest import result


def string_repeat_chars(string, n):
    sub = ""
    if len(string) < 20:
        print("Less than 20 characters!")
        return
    sub = string[1] + string[4] + string[8] + string[13]
    return sub * n


def create_dict(s):
    
    result = {}
    
    keys = set(s)
    for k in keys:
        counter = 0
        for c in s:
            if c == k:
                counter += 1
        result.update({k: counter})
        
    return result

def even_string_list(lstring):
    new_list = []
    for x in lstring:
        if len(x) % 2 == 0:
            new_list.append(x)
            
    return ' '.join(new_list)


        

if __name__ == "__main__":
    value = "asdfasfasfkjbb bopi12j12 12j3nb "
    
    print(string_repeat_chars(value, 10))
    
    dictionary = create_dict(value)
    print(dictionary)
    
    str_list = ['Depois', 'de', 'ver', 'como', 'as', 'coisas', 'andam']
    result = even_string_list(str_list)
    print(result)