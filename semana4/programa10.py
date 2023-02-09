"""
   Programa10
   Nombre: Gustavo DRR
   Fecha: 07/02/2023
   Descripcion: Comentarios multilinea, variables con input, if, elif y else
"""


n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))

#Forma 1
if n1 > n2:
  print(n1)
if n2 > n1:
  print(n2)
if n1 == n2:
  print(None)

#Forma 2
if n2 > n1:
  print(n2)
if n1 > n2:
  print(n1)
else: 
  print(None)

#Forma 3
if n1 > n2:
  print(n1)
elif n2 > n1:
  print(n2)
else:
  print(None)

#Forma 4
if n1 == n2:
  print(None)
elif n1 > n2:
  print(n1)
elif n2 > n1:
  print(n2)

#Forma 5
if n1 < n2:
  print(n2)
if n2 < n1:
  print(n1)
if n1 == n2:
  print(None)

#Forma 6
if n2 > n1:
  print(n2)
if n2 < n1:
  print(n1)
else:
  print(None)

#Forma 7
if (n2<n1>n2):
  print(n1)
elif (n1<n2>n1):
  print(n2)
else:
  print(None)

#Forma 8
if n1 <= n2:
  if n1 == n2:
    print(None)
  else:
    print(n2)
else:
  print(n1)

#Forma 9
if 




#Forma 10





#Forma 11
