from time import sleep
import pygame
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
print('vou te prova que sou inteligente,te direi qual numero é maior')
p1 =int(input('me diga um numero: '))
p2 = int(input('me diga outro numero: '))
print( 'calculando...')
sleep(3)
if p1>p2:
    print('o numero {} é \033[4 mmaior\033[m que {}'.format(p1,p2))
elif p2>p1:
    print('o numero {} é \033[4m maior\033[m que o {}'.format(p2,p1))
else :
    print('vc tentou me enganar seu safado, eles são \033[4m iguais !!')
sleep(2)

pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
print('\033[4m agr acredita que sou esperto? \033[m')

input()

