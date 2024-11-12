# Operadores logicos
# Nos permiten combinar dos o más valores booleanos
# su resultado es un valor booleano

# """
#     and: Devuelve True si todos los valores son True
#     or: Devuelve True si alguno de los valores es True
#     not: Devuelve True si el valor es False y viceversa
# """

# Variables para realizar comparaciones

# and
print(">>Operador logico and<<")
resultado_final = True and True
print(resultado_final)

resultado_final = True and True and True
print(resultado_final)

resultado_final = True and True and False
print(resultado_final)

# or
print(">>Operador logico or<<")
resultado_final = True or True
print(resultado_final)

resultado_final = True or True or True
print(resultado_final)

resultado_final = True or True or False
print(resultado_final)

# not
print(">>Operador logico not<<")
resultado_final = not True
print(resultado_final)

resultado_final = not False
print(resultado_final)

# Agrupacion de operadores logicos
print(">>Agrupacion de operadores logicos<<")
resultado_final = True and (True and False)
print(resultado_final)

resultado_final = True and (True or False)
print(resultado_final)

# Combinando operadores relacionales y logicos
print(">>Combinando operadores relacionales y logicos<<")
resultado_final = 10 > 20 and 10 < 20
print(resultado_final)

resultado_final = 10 > 20 or 10 < 20
print(resultado_final)

# Combinando operadores relacionales y logicos con variables
print(">>Combinando operadores relacionales y logicos con variables<<")
numero_uno = 10
numero_dos = 20

resultado_final = numero_uno > numero_dos and numero_uno < numero_dos
print(resultado_final)

# usar parentesis para agrupar las operaciones y hacer mas legible el codigo
resultado_final = (numero_uno > numero_dos) and (numero_uno < numero_dos)
print(resultado_final)
