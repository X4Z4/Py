s = float(input('Quanto é o seu salario?'))
q = float(input('Qual o valor da casa?'))
a = int(input('Em quantos ano você quer pagar?'))
p = q/(a*12)
m = s*0.3
if p > m:
    print('seu pedido foi negado')
    print('sua prestação é {} e 30% do seu salario é {}'.format(p,m))
elif p<= m:
    print('seu pedido foi aceito')
print('para pagar uma casa de {} reais em {} anos,sua prestação mensal vai ser igual a: {:.2f} '.format(q,a,p) )