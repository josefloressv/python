# Variables para realizar comparaciones
numero_uno = 10
numero_dos = 20

# Operadores relacionales
# Nos permiten comparar dos valores
# su resultado es un valor booleano
"""
    == Igual
    != Diferente
    > Mayor que
    < Menor que
    >= Mayor o igual que
    <= Menor o igual que
"""

# Comparacion de igualdad
resultado = numero_uno == numero_dos
print(resultado)

# Comparacion de desigualdad
resultado = numero_uno != numero_dos
print(resultado)

# Comparacion de mayor que
resultado = numero_uno > numero_dos
print(resultado)

# Comparacion de menor que
resultado = numero_uno < numero_dos
print(resultado)

# Comparacion de mayor o igual que
resultado = numero_uno >= numero_dos
print(resultado)


# comparacion de datos de tipo String
# la comparacion de datos de tipo String es sensible a mayusculas y minusculas
# Pyhton raliza la comparacion caracter por caracter a traves de su codigo ASCII
print(">>Comparacion de datos de tipo String<<")
nombre_uno = "jose"
nombre_dos = "Jose"

resultado = nombre_uno == nombre_dos
print(resultado)

resultado = nombre_uno != nombre_dos
print(resultado)

resultado = nombre_uno > nombre_dos
print(resultado)