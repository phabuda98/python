from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View:", yt.views)

yd = yt.streams.get_highest_resolution()

#Specify the download location on your pc
yd.download('Enter location here')