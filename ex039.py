#desafio bandersnatch
from time import sleep
g = input('prefere ser chamado no masculino ou feminino?').strip()
sleep(1)
if g == 'masculino':
    n= input('me diga seu nome, nome cavaleiro: ').strip()
    print('então meu caro {}, vou te contar a historia de nosso mundo e depois tenho uma missão para vc'.format(n))
    sleep(2)
    print('Anos atras durante a guerra dos cavaleiros contra dragões, muitos morreram para que\n'
          'o rei daqueles demonios alados caisse')
    sleep(3)
    print('mas diferentemente do que achavamos o desgraçado sobreviveu')
    print(' ')
    print('Sua missão é ir atras dele e finalizar o serviço que nós não conseguimos, te daremos uma equipe mas você tomara as decisões')
    c1= 'pelo rio'
    c2= 'pela montanha'
    d= input('por onde você gostaria de começar as buscas? pelo rio ou pela montanha?').strip()
    if d== c1:
        print('Otima, ideia dragões adoram peixe')
        sleep(2)
        print('Antes de ir pegue alguns mantimentos:')
        sleep(1)
        print('\033[4m Você recebeu:1 vara de pesca e 4 pães e um explosivo\033[m')
        print(' ')
        print(' ')
        d2 = input('após 10 dias de viagem para chegar no rio você se depara com pegadas grandes, o que você faz?\n'
                   'correr ou esconder ?').strip()
        if d2=='esconder':
            print( 'você morreu, o dragão que vinha faminto em busca de comida te encontrou e te devorou sobrando apenas a vara de pesca que você recebeu')




        if d2=='correr':
            print('você como um grande cagão decidiu correr e fez bem pois o dragão estava vindo procurar comida')
            print('após o dragão comer e ir embora você ve pegadas que levam a montanha e resolve seguir elas')
            d3 = input(
                'ao encontra o ninho do dragão você encontra ovos recem eclodidos, com os filhotes logo ao lado, o que vc faz?\n'
                'explodo a caverna comigo dentro? ou corro dali? ')
            if d3 == 'explodo a caverna':
                print(
                    'você morreu mas salvou todo o reino pois o dragão que acabara de perder os filhotes nunca mais foi visto')

            if d3 == 'corro dali':
                print(
                    'você saiu vivo naquele momento mais os filhotes cresceram em ritmo acelerado e em 6 meses devoraram o reino')

    if d == c2:
        print('Otima, ideia dragões adoram fazer seus ninhos na montanha')
        sleep(2)
        print('Antes de ir pegue alguns mantimentos:')
        sleep(1)
        print('\033[4m Você recebeu:1 picareta e 4 pães e um explosivo\033[m')
        print(' ')
        print(' ')
        d4 = input(
            'após 7 dias de viagem para as montanhas você encontrou um ninho com ovos que ainda não chocaram, o que você faz?\n'
            ' eu os destruo ou eu deixo como estão e vou atras da mãe?').strip()
        if d4 == 'eu os destruo':
            print('você matou os filhotes e a mae desgostosa deixou o reino')

        if d4 == 'eu deixo como estão':
            print('você nao encontrou a mae e apos 6 meses os filhotes cresceram e mataram o reino')



if g == 'feminino':
    n = input('me diga seu nome, minha nobre amazona: ').strip()
    print('então minha cara {}, vou te contar a historia de nosso mundo e depois tenho uma missão para vc'.format(n))
    sleep(2)
    print('Anos atras durante a guerra dos cavaleiros contra dragões, muitos morreram para que\n'
          'o rei daqueles demonios alados caisse')
    sleep(3)
    print('mas diferentemente do que achavamos o desgraçado sobreviveu')
    print(' ')
    print(
        'Sua missão é ir atras dele e finalizar o serviço que nós não conseguimos, te daremos uma equipe mas você tomara as decisões')
    c1 = 'pelo rio'
    c2 = 'pela montanha'
    d = input('por onde você gostaria de começar as buscas? pelo rio ou pela montanha?').strip()
    if d == c1:
        print('Otima, ideia dragões adoram peixe')
        sleep(2)
        print('Antes de ir pegue alguns mantimentos:')
        sleep(1)
        print('\033[4m Você recebeu:1 vara de pesca e 4 pães e um explosivo\033[m')
        print(' ')
        print(' ')
        d2 = input('após 10 dias de viagem para chegar no rio você se depara com pegadas grandes, o que você faz?\n'
                   'correr ou esconder ?').strip()
        if d2 == 'esconder':
            print(
                'você morreu, o dragão que vinha faminto em busca de comida te encontrou e te devorou sobrando apenas a vara de pesca que você recebeu')

        if d2 == 'correr':
            print('você como um grande cagão decidiu correr e fez bem pois o dragão estava vindo procurar comida')
            print('após o dragão comer e ir embora você ve pegadas que levam a montanha e resolve seguir elas')
            d3 = input(
                'ao encontra o ninho do dragão você encontra ovos recem eclodidos, com os filhotes logo ao lado, o que vc faz?\n'
                'explodo a caverna comigo dentro? ou corro dali? ')
            if d3 == 'explodo a caverna':
                print(
                    'você morreu mas salvou todo o reino pois o dragão que acabara de perder os filhotes nunca mais foi visto')

            if d3 == 'corro dali':
                print(
                    'você saiu vivo naquele momento mais os filhotes cresceram em ritmo acelerado e em 6 meses devoraram o reino')

    if d == c2:
        print('Otima, ideia dragões adoram fazer seus ninhos na montanha')
        sleep(2)
        print('Antes de ir pegue alguns mantimentos:')
        sleep(1)
        print('\033[4m Você recebeu:1 picareta e 4 pães e um explosivo\033[m')
        print(' ')
        print(' ')
        d4 = input(
            'após 7 dias de viagem para as montanhas você encontrou um ninho com ovos que ainda não chocaram, o que você faz?\n'
            ' eu os destruo ou eu deixo como estão e vou atras da mãe?').strip()
        if d4 == 'eu os destruo':
            print('você matou os filhotes e a mae desgostosa deixou o reino')

        if d4 == 'eu deixo como estão':
            print('você nao encontrou a mae e apos 6 meses os filhotes cresceram e mataram o reino')



