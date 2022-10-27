import getpass
from pytube import YouTube

user = getpass.getuser()
default_path = f"C:/Users/{user}/Downloads"

def GetNameFile(link):
    video = YouTube(link)
    return video.title


def DownloadVideoInHigh(link, path):
    video = YouTube(link)
    return video.streams.get_highest_resolution().download(output_path=path)


def DownloadVideoInLow(link, path):
    video = YouTube(link)
    return video.streams.get_lowest_resolution().download(output_path=path)


def DownloadAudioOnly(link, path):
    video = YouTube(link)
    return video.streams.get_audio_only().download(output_path=path, filename=video.title+".mp3")
def DownloadCustomResolution(resolution, link, path):
    video = YouTube(link)
    return video.streams.get_by_resolution(resolution=resolution).download(output_path=path)
