from re import match

print('1\n2') 

print('1\\n2') # para ter uma barra entre os números temos que adicionar duas barras.

print('\section\n') #imprime \section e uma nova linha.

text = '\\section\n'

#r = raw string, é uma string que passa a sinalizar para o python que ela não tem caracter de controle
print(match(r'\\section', text))







