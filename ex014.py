import math
n1 = int(input("digite um numero: "))
raiz = math.sqrt(n1)
fato = math.factorial(n1)
sen = math.sin(n1)
cos = math.cos(n1)

print('aqui esta\n'
      ' a raiz {:.2f}\n'
      ' o fatorial {:.2f},\n'
      ' o sen {:.2f} \n'
      ' o cos {:.2}'.format(raiz,fato,sen,cos))

print("a raiz de {:.2f} é igual a {:.2f}".format(n1,raiz))
print('a raiz arrendondada para cima vale {} e para baixo vale {}'.format(math.ceil(raiz),math.floor(raiz)))