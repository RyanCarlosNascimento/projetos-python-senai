# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
# Inicializar a biblioteca do pygame
pygame.mixer.init()

# Carregar o arquivo de música
pygame.mixer.music.load('Ex021.mp3')

# Tocar a música
pygame.mixer.music.play()

# Encerrar o programa
input("Pressione Enter para parar a música.")
pygame.mixer.music.stop()