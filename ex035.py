n = int(input('qual a distancia da sua viagem em quilometros?: '))
if n<=200:
    print('sua passagem vai custar{} reais'.format(n*0.5))
if n>=200:
    print('sua viagem vai custar {} reais'.format(n*0.45))