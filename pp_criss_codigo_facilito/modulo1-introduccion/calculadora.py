print("Bienvenido a mi calculadora")

numero_uno = float(input("Inresa primer número: "))
operacion = input("Inresa la operación: ")
numero_dos = float(input("Inresa segundo número: "))
resultado = 0
if operacion == "+": resultado = numero_uno + numero_dos
elif operacion == "-":  resultado = numero_uno - numero_dos
elif operacion == "*":  resultado = numero_uno * numero_dos
elif operacion == "/":  resultado = numero_uno / numero_dos
else: print("Operador incorrecto")

print(f"El resultado de {numero_uno} {operacion} {numero_dos} = {resultado}" )