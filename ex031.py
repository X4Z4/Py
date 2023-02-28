import pygame
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
nome= (input('digite seu nome todo: ')).strip()
nome1= nome.split()
print('bom dia senhor {}'.format(nome1[len(nome1)-1]))
n1 = float(input('por favor digite sua primeira nota: '))
n2 = float(input('agr por favor digite sua segunda nota: '))
m= (n1+n2)/2
s = float(input('quanto você ganhou no simulado: '))
mt = m+s
pp = (7-mt)*3
print('Calculando...')
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
if m+s < 7:
    print('vc precisa estudar mais, suas notas tao muito baixas')
    print('para você fica na media vc precisa de {} pontos na media'.format(7 - mt))
    print('isso equivale {} pontos na prova'.format(pp))
else:
    print('muito bom vc parece estar se esforçando')
print('sua media é igual a {}'.format(m))

input()