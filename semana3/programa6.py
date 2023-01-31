"""
   Programa6
   Nombre: Gustavo DRR
   Fecha: 30/01/2023
   Descripcion: Comentarios multilinea, variables con input y prints
"""


lado1 = float(input("Ingresa el lado 1: ")) #Asigna el valor de la variable lado1
lado2 = float(input("Ingresa el lado 2: ")) # Asigna el valor de la variable lado2
base = float(input("Ingresa la base: ")) # Asigna el valor de la variable base
altura = float(input("Ingresa la altura: ")) # Asigane el valor de la variable altura

perimetro = (lado1) + (lado2) + (base) #Hace la operacion de de las variables de lados y base
area = (base) * (altura) / (2) #Hace la operacion de la variable base y altura

print("El perimetro del triangulo es: ", perimetro) #Imprime el resultado de la variable perimetro
print("El area del triangulo es: ", area) # Imprime el resultado de la variable area
