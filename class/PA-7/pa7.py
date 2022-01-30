"""
Author: Andrei Razvan Oproiu
Date: Sun Jan 30 2022
"""

def montante_comp(pv, i, n):
    i = i / 100
    return pv * (1 + i) ** n


def montante_simpl(c,i,n):
   i = i/100
   return c*(1+i*n)

def parcela(pv,i,n):
   i=i/100
   return pv*( (i*(1+i)**n) / (((1+i)**n)-1) )


if __name__ == "__main__":
    linha = '-'
    c = float(input("Capital : "))
    i = float(input("taxa de juros %: "))
    n = float(input("Periodo em meses :" ))
    print (linha)

    print ("Montante com Juros simples: %0.2f " % (montante_simpl(c,i,n)))
    print (linha)
    print ("Montante com Juros Compostos: %0.2f " % (montante_comp(c,i,n)))
    print (linha)
    print ("Prestacao : %0.2f " % (parcela(c,i,n)))
    print (linha)