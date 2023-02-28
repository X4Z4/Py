#exercicio de tocar audio
import pygame
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('bom a dia a todos')

input()



