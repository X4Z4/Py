n = int(input('me diga a velocidade do seu carro: '))
if n>= 80:
    print('vc foi multado hein {} reais'.format((n-80)*7))
if n<= 80:
    print('ta tranquilo o radar nem ligou pra vc')
