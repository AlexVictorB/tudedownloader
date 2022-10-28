from pytube import YouTube
import getpass
import os
user = getpass.getuser()
video = YouTube("https://www.youtube.com/watch?v=XICabZgt8RE")
default_path = f"C:/Users/{user}/Downloads"

print(video.title)

arquivo = f"C:/Users/{user}/Downloads/{video.title}.mp4"

print(os.path.exists(arquivo))


#video.streams.get_lowest_resolution().download(output_path=default_path)