import math
import numpy as np

# CF = taxaJuros / 1-(1+n)**-periodo
 # tj = spread + t 

def montante_comp(pv, i, n):
   #Função para cálculo de montantecom juros compostos
   i = i/100
   return pv*(1+i)**n
   
def montante_simpl(c,i,n):
   #Função para cálculo de montante  com juros simples (Bom somente para comparação com os compostos)
   i = i/100
   return c*(1+i*n)

def parcela(pv,i,n):
   #Função para cálculo do valor de uma parcela de empréstimo
   i=i/100
   return pv*( (i*(1+i)**n) / (((1+i)**n)-1) )
   

   
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