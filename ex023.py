#teste 2 de tocar musica
import pygame
import emoji
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('bom dia, vamos la? Eu sou o Xaza seu robo contador e vou te entregar as operações matematicas')
n1 = int(input('me diga um numero: '))
n2 = int(input('me diga um segundo numero: '))
s = n1+n2
p = n1**n2
d = n1/n2
sub = n1-n2
m = n1*n2
print('Aqui estão os resultados das contas pedidas')
print('soma {} e subtração {}'.format(s,sub))
print('divisão {} e multiplicação {}'.format(d,m))
print('aqui esta {} elevado a {} que vale {} '.format(n1,n2,p))















