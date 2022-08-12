import pytube

#https://www.youtube.com/watch?v=dA2Iv9evEK4&list=PLzCxunOM5WFJxaj103IzbkAvGigpclBjt
link = input("Introduce de la lista: ")
filtros = "https://www.youtube.com/"
if link.startswith(filtros):
    playlist = pytube.Playlist(link)
    print(playlist.title + " " + str(len(playlist.video_urls)))
    for video in playlist.video_urls:
        yt = pytube.YouTube(video)
        video = yt.streams.get_highest_resolution()
        video.download()

else:
    print("Introduce un link valido")
