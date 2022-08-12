# Ejercicio 3 - Repaso

# Crea un programa que pida al usuario su nombre y su edad. 
# Imprime un mensaje que diga "Hola {nombre}, el año pasado tenías {edad - 1} años y el año que viene tendrás {edad + 1} años". 
# Si la edad es mayor o igual a 18, imprime un mensaje que diga "Eres mayor de edad". 
# Si la edad es menor a 18, imprime un mensaje que diga "Eres menor de edad".

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
print("Hola {}, el año pasado tenías {} años y el año que viene tendrás {} años.".format(nombre, edad - 1, edad + 1))

if edad >= 18:
    print("Eres mayor de edad")
elif edad < 18:
    print("Eres menor de edad")