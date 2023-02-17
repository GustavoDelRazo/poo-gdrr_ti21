"""
   Programa10
   Nombre: Gustavo DRR
   Fecha: 07/02/2023
   Descripcion: Comentarios multilinea, variables con input, if, elif y else
"""


n1=int(input("Numero 1: ")) #Ingresa una variable  de nombre n1
n2=int(input("Numero 2: ")) #Ingresa una variable  de nombre n2

#Forma 1
if n1 > n2: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
if n2 > n1: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
if n1 == n2: #Hace una condicion de los valores para identificar si son iguales
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 2
if n2 > n1: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
if n1 > n2: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 3
if n1 > n2: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
elif n2 > n1: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 4
if n1 == n2: #Hace una condicion de los valores para identificar si son iguales
  print(None) #Imprime el valor None, cuando los valores son iguales
elif n1 > n2: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
elif n2 > n1: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto

#Forma 5
if n1 < n2: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
if n2 < n1: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
if n1 == n2: #Hace una condicion de los valores para identificar si son iguales
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 6
if n2 > n1: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
if n2 < n1: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 7
if (n2<n1>n2): #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser mas alto
elif (n1<n2>n1): #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
  print(None) #Imprime el valor None, cuando los valores son iguales

#Forma 8
if n1 <= n2: #Hace una condicion para saber cual es el valor mas alto
  if n1 == n2: #Hace una condicion de los valores para identificar si son iguales
    print(None) #Imprime el valor None, cuando los valores son iguales
  else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
    print(n2) #Imprime el valor n2 por ser mas alto
else: #Hace referencia a lo que pasaría si ninguna de las condiciones se cumple
  print(n1) #Imprime el valor n1 por ser mas alto
