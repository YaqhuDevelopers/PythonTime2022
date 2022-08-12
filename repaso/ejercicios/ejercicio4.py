# Ejercicio 4 - Repaso

# Crea un programa que pida al usuario su nombre y su edad. 
# Imprime un mensaje que diga "Hola {nombre}, el año pasado tenías {edad - 1} años y el año que viene tendrás {edad + 1} años". 
# Si la edad es mayor o igual a 18 y menor que 64, imprime un mensaje que diga "Eres adulto". 
# Si la edad es menor a 18, imprime un mensaje que diga "Eres menor de edad". 
# Si la edad es mayor o igual a 65, imprime un mensaje que diga "Eres jubilado".
# Si la edad es menor a 0, imprime un mensaje que diga "Edad inválida".

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
print("Hola {}, el año pasado tenías {} años y el año que viene tendrás {} años.".format(nombre, edad - 1, edad + 1))

if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 64:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Eres jubilado")
