#achar sen e cos
import math
n1 = int(input('me diga o angulo em questao: '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tg =  math.tan(math.radians(n1))
print('aqui estão os valores seno {:.2}, cos {:.2}, tg {:.2}'.format(sen, cos,tg))