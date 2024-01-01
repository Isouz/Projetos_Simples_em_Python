from pytube import YouTube

def baixar(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        if stream:
            stream.download()
            print('Concluído')
        else:
            print('Não foi possível encontrar uma stream adequada para download.')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

link = input('Link: ')
baixar(link)

# Obs: O video estará na mesma pasta do arquivo (baixar_videos_youtube.py) após o download.


# Use o comando 'pip install pytube' no terminal para instalar a biblioteca.

# Desenvolvido por Igor Souza.
# GitHub - https://github.com/Isouz