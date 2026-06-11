"""
import pygame;
pygame.init()
pygame.mixer.music.load('anirapwb.mp3')
pygame.mixer.music.play()
pygame.event.wait()
"""

import pygame

pygame.init()
pygame.mixer.music.load('anirapwb.mp3')
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Evita que o processo consuma 100% da sua CPU

