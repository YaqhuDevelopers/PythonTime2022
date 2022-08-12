import os

archivo = input("Introduce el nombre del archivo: ")

corruptos = []

for dir in os.listdir():
    if dir == archivo:
        print("Tu archivo existe, generamos el reporte")
    else:
        corruptos.append(dir)

with open("log.txt", "a") as file:
    for elemento in corruptos:
        file.write("{}\n".format(elemento))

        