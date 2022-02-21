"""
Linguagem que detecta padrões, é expressado um pattern ao um texto.
"""

import re # 3 funções principais

#match encontra padrões
print(re.match('abc', 'abc'))


#search encontra padrões ao longo da string
print(re.search('abc', 'efgabc'))


#findall todas as ocorrencias de padrões no texto
print(re.findall('abc', '123abc456abc'))


from re import match, search, findall