# -*- coding: utf-8 -*-
"""reto 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18qwotgys5bTKRQm1kDRUSOMuyj4RI68S
"""

import json
lista=[]
monedas={}
lista1=[]
#{"peso_chileno": 5307, "dolar_canadiense": 9132, "peso_mexicano": 7972, "yuan": 9685, "dolar_australiano": 8346, "real": 4299, "sol": 6769}
#euro libra_esterlina driham rupia sol peso_mexicano dolar_canadiense
monedas=input()
monedas=json.loads(monedas)
#print(type(monedas))
lista=list(monedas.keys())
y=input().split() #2do ingreso
#print(monedas)
#print(y)
acum=0
for k in y:
   #print(k)
   if k in lista:
     #print("la palabra está")
     acum+=monedas[k]
     lista1.append(k)
print(acum)
#print(lista1)
#print(monedas)
#print(lista1[::-1])
for j in lista1:
  #if conta==1:
   print(j,end=" ")
   #conta=2
  #else:
   #print(j,end="\n")