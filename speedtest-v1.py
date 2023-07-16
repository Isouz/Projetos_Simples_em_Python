import speedtest

print('Testando ...')

teste = speedtest.Speedtest()
velocidade_de_download = teste.download()
velocidade_de_upload = teste.upload()
ping = teste.results.ping

print(f'Velocidade de download: {velocidade_de_download / 10**6:.2f} Mbps.')
print(f'Velocidade de upload: {velocidade_de_upload / 10**6:.2f} Mbps.')
print(f'Ping {ping:.2f} ms.')

# use o comando 'pip install speedtest-cli' no terminal para instalar a biblioteca.


#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz