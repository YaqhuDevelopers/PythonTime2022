
i = 1
    
fileName = input("Ingresa el nombre del archivo .txt que quieres crear: ")
archivo = fileName + ".txt"
    
while i < 28:
    archivo = fileName + str(i) + ".txt"
    with open(archivo, "w") as file:
        file.write("hola mundo!")
    i+=1