"""
   Programa7
   Nombre: Gustavo DRR
   Fecha: 31/01/2023
   Descripcion: Comentarios multilinea, variables con input y prints
"""


radio = float(input("Ingresa el radio del circulo: ")) #Asigna el valor de la variable radio

perimetro = (radio) * (2) * (3.1416) # Hace la operacion de la variable radio por pi y 2
area = (3.1416) * (radio) ** (2) #Hace la operacion de la variable radio por pi

print("El area de un criculo de {} de radio es {}".format(radio, area)) # Imprime el resultado de la variable area
print("El perimetro de un circulo de {} de radio es {}".format(radio, perimetro)) # Imprime el resultado de la variable perimetro
print("---------------------------------------------------------------")

lado = float(input("Ingresa el lado del cuadrado: ")) # Asigna el valor de la variable lado

perimetro = (lado) * (4) # Hace la operacion de la variable perimetro
areac = (lado) ** (2) # Hace la operacion de la variable area

print("El area de un cuadrado de {} de lado es {}".format(lado, areac)) # Imprime el resultado de la variable area
print("El perimetro de un cuadrado de {} de lado es {}".format(lado, perimetro)) # Imprime el resultado de la variable perimetro
