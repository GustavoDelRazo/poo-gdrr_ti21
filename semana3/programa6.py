"""
   Programa6
   Nombre: Gustavo DRR
   Fecha: 30/01/2023
   Descripcion: Comentarios multilinea, variables con input y prints
"""


lado1 = input("Ingresa el lado 1: ") #Asigna el valor de la variable lado1
lado2 = input("Ingresa el lado 2: ") # Asigna el valor de la variable lado2
base = input("Ingresa la base: ") # Asigna el valor de la variable base
altura = input("Ingresa la altura: ") # Asigane el valor de la variable altura

perimetro = float(lado1) + float(lado2) + float(base) #Hace la operacion de de las variables de lados y base
area = float(base) * float(altura) / (2) #Hace la operacion de la variable base y altura

print("El perimetro del triangulo es: ", perimetro) #Imprime el resultado de la variable perimetro
print("El area del triangulo es: ", area) # Imprime el resultado de la variable area
