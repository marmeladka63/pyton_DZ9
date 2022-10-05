

from asyncio import streams
from pytube import YouTube
url=input("Введите URL видео:")
print("Качество видео необходимо?\n 640x480- введите цифру 1\n 1920х1080 - введите цифру 2")
a = input('Введите цифру: ')
def grab(url):
    if a == '1':
        video480  = YouTube(url).streams.filter(res='480p').desc().first()
        video480.download()
    else:
        video1280 = YouTube(url).streams.filter(res='1080p').desc().first()
        video1280.download()
        
    YouTube(url).streams.filter(only_audio=True).first().download() 

print ("Видео заданного качества и аудио успешно скачано в Вашу папку")
grab(url)