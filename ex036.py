from datetime import date
n = int(input('que ano vc quer analisar?: '))
escolhido = n%4

if n%4 == 0 and escolhido %100 !=0 or escolhido%400 == 0:
    print('é bissexto')
if escolhido == 0:
    escolhido= date.today().year
else:
    print('não é bissexto')