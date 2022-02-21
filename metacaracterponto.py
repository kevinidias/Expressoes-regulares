from re import match, search, findall
import re

print(match('.', 'abc'))


print(match('.', '012'))

print(match('.', ' '))

#âncoras ^ $

print(findall('^.', 'abc\ndef\nghi')) # todas ocorrencias de um caracter que esteja no inicio de uma string


print(findall('^.', 'abc\ndef\nghi', re.MULTILINE)) # ultimo caracter de cada linha.

print(findall('.$', 'abc\ndef\nghi')) # retorna caracter no fim da string.


print(findall('.$', 'abc\ndef\nghi', re.MULTILINE)) # ultimo caracter de cada linha.