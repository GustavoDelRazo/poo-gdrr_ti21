"""
   Programa11
   Nombre: Gustavo DRR
   Fecha: 09/02/2023
   Descripcion: Comentarios multilinea, variables con input, if, elif y else
"""


def mayor(numero1, numero2):
  result = None
  if numero1 > numero2: #Hace una condicion para saber cual es el valor mas alto
    result = numero1
  elif numero2 > numero1: #Hace una condicion para saber cual es el valor mas alto
    result = numero2
  return result 


print(mayor(2, 1)) # 2
print(mayor(1, 2)) # 2
print(mayor(2, 2)) # None
print(mayor(-1, 1)) # 1
print(mayor(1, -1)) # 1
print(mayor(-1, -1)) # None
print(mayor(1, -2)) # 1
print(mayor(-2, 1)) # 1
