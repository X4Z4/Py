#achar a hipotenusa
import math
co = int(input('me diga o valor do cateto oposto: '))
ca = int(input('me diga o valor do cato adjacente: '))
qhip= co*co + ca*ca
hip = math.sqrt(qhip)
print('a hipotenusa do triangulo retangulo vale {}'.format(hip))