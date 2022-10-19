from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=u0CqY27IFyo&list=PLKRIguIRieq_lnxT6FbzTSkvuQDAtyl0r&index=21")

print(video.title + ".mp3")