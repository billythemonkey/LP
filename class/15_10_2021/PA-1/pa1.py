from typing import Sized


# Alínea a)

def fibonacci(nrterms):
    
    n1 = 1
    n2 = 2
    count = 0
    numbers = []
    
    if nrterms == 1 :
        return nrterms
    elif nrterms > 1:
        while count < nrterms:
            # print(n1)
            numbers.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return numbers
 
 
def recursive_fibonacci(n):
    while n > 0:
        if n < 0:
            print("Número inválido!")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        
# Alínea b)
            
def const_reciproc(n):
    sum = 1
    num = fibonacci(n)
    for n in num:
        sum += 1/n
    return sum
      
      
# Alínea c)

def const_reciproc_with_error(const, erro):
    sum = 1
    num = fibonacci(const)
    for n in num:
        sum += 1/n
    print(sum)
    return sum

def erro_absoluto():
    print("s")
    
       
if __name__ == "__main__":
    
    # testA = fibonacci(25)
    # print(testA)
    
    # testB = const_reciproc(10000)
    # print("Constante Recíproca de Fibonacci =",testB)
    
    # testC = const_reciproc_with_error(100, 1)
    # print(testC)
    
    a = []
    a.append(recursive_fibonacci(3))
    print(a)
    