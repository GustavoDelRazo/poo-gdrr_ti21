"""
   Programa9
   Nombre: Gustavo DRR
   Fecha: 02/02/2023
   Descripcion: Comentarios multilinea, variables con input y prints
"""


n1 = int(input("Ingresa el primer valor: ")) #Ingresa una variable  de nombre n1
n2 = int(input("Ingresa el segundo valor: ")) #Ingresa una variable  de nombre n2

if n1 < n2: #Hace una condicion para saber cual es el valor mas alto
  print(n2) #Imprime el valor n2 por ser mas alto
elif n1 == n2: #Hace una condicion de los valores para identificar si son iguales
  print(None) #Imprime el valor none por ser iguales
elif n2 < n1: #Hace una condicion para saber cual es el valor mas alto
  print(n1) #Imprime el valor n1 por ser el mas alto
  
