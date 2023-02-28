#Calculadora basica

from time import sleep
import pygame
from math import sqrt
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
nome = input('Diga seu nome por favor: ')
e =input('digite 1 se quiser usar a calculadora1, 2 se quiser saber quanto de tinha vc vai precisar pra pinta uma parede: ').strip()

if e== '1':
    print('\033[7;32;40m Agora vamos la {} \033[m'.format(nome))
    n1 = int(input('digite o primeiro numero: '))
    n2 = int(input('digite o segundo numero: '))
    s = n1 + n2  # soma
    d = n1 / n2  # divisão
    rd = n1 % n2  # resto da divisão
    m = n1 * n2  # multiplicação
    sub = n1 - n2  # subtração
    p = n1 ** n2  # potencia obs:para achar a raiz basta pegar o numero e elevar ele a 1/2
    dvinteira = n1 // n2  # divisao inteira de dois numeros
    raiz1 = sqrt(n1)
    raiz2 = sqrt(n2)
    print('\033[2;35m calculando... \033[m')
    sleep(3)
    print('\033[4;35m então, o resultado dessas contas é: \033[m')
    sleep(2)
    print('=' * 20)
    print('a soma vale:', s)
    # print('a soma entre', n1 ,'e' ,n2 ,'vale', s)
    print('a soma entre {} e {} vale {}'.format(n1, n2, s))
    print('=' * 20)
    print('a subtração vale', sub)
    print('a subtração entre', n1, 'e', n2, 'vale', sub)
    print('=' * 20)
    print('a divisão entre', d)
    print('a divisão entre', n1, 'e', n2, 'vale', d)
    print('=' * 20)
    print('o resto da divisao vale', rd)
    print('o resto da divisão de', n1, 'e', n2, 'é', rd)
    print('=' * 20)
    print('a divisão inteira é', dvinteira)
    print('a divisao inteira entre', n1, 'e', n2, 'vale', dvinteira)
    print('=' * 20)
    print('a multiplicação vale', m)
    print('a multiplicação entre', n1, 'e', n2, 'vale', m)
    print('=' * 20)
    print('a potencia vale', p)
    print('a potencia de', n1, 'elevado a', n2, 'vale', p)
    print('=' * 20)
    print('a raiz de', n1, 'é {:.2}'.format(raiz1))
    print('a raiz de', n2, 'é {:.2}'.format(raiz2))
    print("=" * 20)
    print('Posso te ajudar em algo mais??')

    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()

elif e== '2':
    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()
    n1 = float(input('me diga a altura da parede em metros: '))
    n2 = float(input('me diga a largura em metros da sua parede por favor: '))
    n3 = int(input('quanto cada galão de tinta quase pinta em metros quadrados: '))
    A = n1*n2
    G = (n1*n2)/n3
    print('aqui esta a area de sua parede {}'.format(A))
    print("aqui esta o numero de galões necessarios para a pintura {}".format(G))

input()




