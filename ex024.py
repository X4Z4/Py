
#print(len(frase))
#fatiamento: print(frase[:21])assim ele vai do inicio ate o caracter 21
# [21:] assim é do caracter 21 pra frente
# [9:21] assim ele vai so do caracter 9 ate o 21, e assim [9:21:2] ele vai do 9 ao 21 pulando de 2 em 2
# ele esta fatiando a frase para que so apareça do caracter 21 adiante
#numero que vem no inicio mostra onde o fatiamento começa, o do meio mostra onde acaba e o do final mostra pulando de quanto em quantos
#frase.count('o') conta quantos 'o' tem na frase, se escrito assim frase.count(o,0,13) ele vai contar todos os 'o' do 0 ate o 12
#frase.find() esse comando significa encontrar letras especificas e dizer em qual caractere eles começam
#se digitarmos curso in frase, ele vai responder com a palavra true, pois dentro da frase escolhida existe a palavra curso
#frase.replace(python,android) ele substituiria a palavra python por android
#frase.upper() ele torna a frase maiuscula
#frase.lower() ele torna a frase minuscula
#frase.capitalize() ele troca todo mundo pra minusculo menos o primeiro caracter
#frase.title() separa todas as palavras dentro da frase
#frase.strip() ele mata todos os caracteres de espaço em branco no inicio e no fim exitem variaçoes frase.rstrip ele so retira os caracteres a direita e se inves de r for L ele retira so os da esquerda
#frase.split() ele cria varias divisões dentro do string tirando os espaços
#'-'.join(frase) ele desfaz o split trocando o lugar que seriam espaços por - se quiser outro caracter para essa substituição é so trocar nas aspas
n = input('digite seu nome por favor: ').strip()
separa = n.split()
print('calculando...')
print('seu nome em maiusculo é {}'.format(n.upper()))
print('seu nome em minusculo é {}'.format(n.lower()))
print('seu primeiro tem esse numero de letras {} '.format(n.find(' ')))
print('seu nome ao todo tem {} letras'.format(len(n) - n.count(' ')))
print('seu primeiro nome é {}'.format(separa[0]))
