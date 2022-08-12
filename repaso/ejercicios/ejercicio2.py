# Ejercicio 2 - Repaso

# Crea un programa que pida al usuario su nombre y su edad.
# Imprime un mensaje que diga "Hola {nombre}, el año pasado tenías {edad - 1} 
# años y el año que viene tendrás {edad + 1} años".

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
print("Hola {}, el año pasado tenías {} años y el año que viene tendrás {} años.".format(nombre, edad - 1, edad + 1))
print("Hola " + nombre + ", el año pasado tenías " + str(edad - 1) + " años y el año que viene tendrás " + str(edad + 1) + " años.")