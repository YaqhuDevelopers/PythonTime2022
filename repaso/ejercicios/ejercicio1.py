# Ejercicio 1 - Repaso

# Crea un programa que pida al usuario su nombre y su edad. 
# Imprime un mensaje que diga "Hola {nombre}, tienes {edad} años".

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")

print("Hola {}, tienes {} años.".format(nombre, edad))
print("Hola " + nombre + ", tienes " + edad + " años.")