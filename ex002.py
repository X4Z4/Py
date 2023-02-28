#programa de reconhecimento de tipo
n = input('digite algo: ')
print(type(n))
print('n é apenas letras?',n.isalpha())
print('n esta apenas em minusculo?',n.islower())
print('n é so numero?',n.isdecimal())
print('n esta apenas em caixa alta?',n.isupper())
print('n é conjunto vazio?',n.isspace())
