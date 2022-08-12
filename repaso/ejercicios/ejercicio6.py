# Ejercicio 6 - Repaso

# Crea un programa que invierta el orden de las palabras de una frase. 
# El programa debe pedir al usuario una frase y luego imprimir la frase invertida. 
# Por ejemplo, si el usuario ingresa "Hola mundo", el programa debe imprimir "mundo Hola".

frase = input("Introduce una frase: ")
frase = frase.split() # Convertir la frase en una lista de palabras separadas por espacios
frase = frase[::-1] # Invertir el orden de la lista de palabras
frase = " ".join(frase) # Convertir la lista de palabras en una frase separada por espacios
print(frase) # Imprimir la frase invertida