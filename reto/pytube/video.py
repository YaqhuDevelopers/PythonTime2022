import pytube

link = pytube.YouTube(input("Introduce el enlace del video: ")) #Declarado el enlace como un video de Youtube
titulo = link.title #Obtenemos el titulo del video
descripcion = link.description #Obtenemos la descripcion

video = link.streams.get_highest_resolution()
video.download()

with open("archivo.txt" , "w") as file:
    file.write(titulo + "\n")
    file.write(descripcion + "\n")