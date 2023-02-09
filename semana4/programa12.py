"""
   Programa12
   Nombre: Gustavo DRR
   Fecha: 09/02/2023
   Descripcion: Comentarios multilinea, variables con input, if, elif y else
"""


def mayor(numero1:int, numero2:int)->int | None:
    result = None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    return result





print(mayor(2, 1))
print(mayor(1, 2))
print(mayor(45.7, 22.7))
print(mayor(-15, -13))
print(mayor(90, 74))
print(mayor(99.9, 99.8))
print(mayor(4, 7))
print(mayor(-16, -88))
