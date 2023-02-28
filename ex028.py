n = input('me diga uma frase: ').upper().strip()
print('o numero de vezes que a letra "a" aparece é {}'.format(n.count("A")))
print('a primeira letra a apareceu na posição {}'.format(n.find("A")+1))
print('a ultima vez que a letra A aparece é na posição {}'.format(n.rfind('A')+1))