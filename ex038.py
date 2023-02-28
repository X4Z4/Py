import pygame
pygame.init()

nome = input('Qual seu nome?')
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()

print('mto prazer em te conhecer {}{}{}'.format('\033[1;34;45m', nome,'\033[m'))
print('\033[7;31;45m bom dia\033[m')
input()

