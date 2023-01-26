"""
   Programa4
   Nombre: Gustavo DRR
   Fecha: 26/01/2023
   Descripcion: Comentarios multilinea, comentarios de una linea, variables int, string y print tipo 
   format
"""


numero1 = 10 #Variable de tipo int
numero2 = 5 #Variable de tipo int


print("{} + {} = {}".format(numero1, numero2, numero1 + numero2)) # Este esta  bien

print("{n1} + {n2} = {suma}".format(n1=numero1, n2=numero2, suma=numero1 + numero2)) # Sirve por que declaramos el valor

print("{n2} + {n2} = {n2}".format(n1=numero1, n2=numero2, suma=numero1 + numero2)) # Solo imprime el valor de n2

print("{n4} + {n4} = {suma}".format(n1=numero1, n2=numero2, suma=numero1 + numero2)) # No funciona por que no declaramos la variable n4

print("{numero1} + {numero2} = {suma}".format(numero1=numero1, numero2=numero2, suma=numero1 + numero2)) # Permite imprimir valores sin importar el tipo de dato