nombre_archivo = input("Introduce el nombre del archivo: ")
cantidad = int(input("Introduce la cantidad de archivos a crear: "))

for i in range(cantidad+1):
    archivo = "{}_{}.txt".format(nombre_archivo, i)
    with open(archivo, "w") as file:
        file.write("Hola")

