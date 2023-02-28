#exercicio de montar um 'abaco'
n = int(input('Me diga um numero: '))
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10
mm = n//10000%10
print('Aqui está:')
print('unidade= {}'.format(u))
print('dezenas= {}'.format(d))
print('centena= {}'.format(c))
print('milhares= {}'.format(m))