import pygame
print('TOCADOR MP3')
pygame.init() #iniciando o Pygame
pygame.mixer.music.load('vsme.mp3') #Selecionado a música
pygame.mixer.music.play() #Tocando a música
input()
pygame.event.wait() #Parando o Pygame


