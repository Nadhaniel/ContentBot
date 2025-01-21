from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.filter(only_video=True, file_extension="mp4").order_by('bitrate').desc().first()

    ys.download()