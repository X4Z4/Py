#escolha de ordem
import random
n1 = input('primeiro grupo')
n2 = input('segundo grupo')
n3 = input('terceiro grupo')
n4 = input('quarto grupo')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem de apresentação dos grupos vai ser ')
print(lista)