"""
Classes de caracteres
"""

from re import match, search, findall
import re

print(findall('[aeiou]', 'Kevin Dias')) #traz um conjunto de caracteres


print(findall('[^aeiou]', 'Kevin Dias')) #traz uma negação de caracteres


print(findall('[a-fA-Z]', 'Kevin Dias')) #traz um conjunto dentro do range


# \d == [0-9]

#\D == [^0-9] negação

#\s == [\t\n\r\f\v]

# \S == [^\t\n\r\v] negação

# \w - representa de a-z, A-Z, 0-9 ou _

# \W - representa de ^a-z, A-Z, 0-9 ou _ negação




