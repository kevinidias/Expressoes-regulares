"""
| pipe = OU
Funciona como alternativas para o teste de expressão regular.
"""

from re import match

print(match('a|b', 'abc')) # pegou o a



print(match('a|b', 'bce')) # pegou o b