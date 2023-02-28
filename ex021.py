#teste novamente de randomicos
import random
print('Olá turma, eu que irei escolher a ordem de apresentação de trabalho de vcs\n me digam os grupos pfvr')
n1 = input('primeiro grupo:')
n2 = input('segundo grupo:')
n3 = input('terceiro grupo:')
n4 = input('quarto grupo:')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem que eu decidi vai ser: {} '.format(lista))