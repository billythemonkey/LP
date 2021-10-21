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
        print("A sequência de Fobinacci de ", nrterms, ": ")
        while count < nrterms:
            # print(n1)
            numbers.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return numbers
 
 
# Alínea b)
            
def const_reciproc(n):
    sum = 0
    num = fibonacci(n)
    for n in num:
        sum += 1/n
    print(sum)
    return sum
      
      
# Alínea c)
       
if __name__ == "__main__":
    # fibonacci(10)
    const_reciproc(1000)