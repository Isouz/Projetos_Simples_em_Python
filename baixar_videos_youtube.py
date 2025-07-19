from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input('Link: ')

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()

print('Concluido!')

# Instale o pytubefix através do comando: pip install pytubefix
# Obs: O video estará na mesma pasta do arquivo (baixar_videos_youtube.py) após o download.

# Desenvolvido por Igor Souza.
# GitHub - https://github.com/Isouz
