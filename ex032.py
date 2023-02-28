#descubra o numero
import random
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
print('descubra o numero q estou pensando')

n = 1
n2 =2
n3 = 3
n4 = 4
n5 =5
r = input('de 1 a 5 qual vc acha q eu vou escolher?: ').strip().upper()
lista= [n,n2,n3,n4,n5]

random.shuffle(lista)
alfa = lista[1]
print('Se acalme eu to vendo se vc acertou')
sleep(7)
print( )
print( )
print('o numero que pensei foi {}'.format(alfa))

if r == alfa:
    print('acertou, mizeravi')
    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()
else:
    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()
    print('não foi dessa vez amigão tenta dnv')
input()