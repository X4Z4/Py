#teste de condicionais
import pygame
pygame.init()
pygame.mixer.music.load('ex022m.mp3')
pygame.mixer.music.play()
i = int(input('Quantos anos vc tem??'))
if i >=19:
    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()
    print('eita ja ta ficando velho')
    print('espero que tenha aproveitado bem sua infancia :)')
else :
    pygame.mixer.music.load('ex022m.mp3')
    pygame.mixer.music.play()
    print('relaxa po tu ta novo')
    print('aproveita melhor a vida po vai fazer exercicio e estudar')
print('fim')
input()