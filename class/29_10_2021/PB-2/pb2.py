"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

# Alínea a)


from re import L


def recursive_sub_vowels(string):
    if not string:
        return ''
    c = '' if string[0] in 'aeiouAEIOU' else string[0]
    return c + recursive_sub_vowels(string[1:])


# Alínea b)

def recursive_replace_b_for_a(string):
    if not string:
        return ''
    c = 'a' if string[0] in 'bB' else string[0]
    return c + recursive_replace_b_for_a(string[1:])
    
# Alínea c)

def recursive_vowels_count(string, size):
    global sum
    if size > 0:
        size -= 1
        if string[size] in 'aeiouAEIOU':
            sum = sum + 1
        recursive_vowels_count(string, size)
    return sum 
    

# Alínea d)
    
def recursive_even_numbers(a, b):
    
    global l1
    
    if b < a:
        return
    if b % 2 == 0:
        recursive_even_numbers(a, b - 2)
    else:
        recursive_even_numbers(a, b - 1)
        
    if b % 2 == 0:
        l1.append(b)
    return l1
    
    
    
if __name__ == "__main__":
    sum = 0
    string = "Borcalho"
    l1 = []
    print(recursive_sub_vowels(string))
    
    print(recursive_replace_b_for_a(string))
    
    print(recursive_vowels_count(string, len(string)))
    
    print(recursive_even_numbers(10, 20))