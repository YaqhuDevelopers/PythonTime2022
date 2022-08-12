# Ejercicio 4 - Repaso

# Crea un programa que verifique si un número es par o impar. 
# El programa debe pedir al usuario un número y luego imprimir un mensaje que diga "El número {numero} es par" o "El número {numero} es impar".

numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número {} es par".format(numero))
else:
    print("El número {} es impar".format(numero))