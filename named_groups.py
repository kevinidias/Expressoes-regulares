"""
Faz com que tenhamos a capacidade de criar Regex flexíveis.
"""

from re import match


html1 = '<input type="text" id="id_cpf" name="cpf">'

pattern = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(?P<id>.+?)"|name="(?P<name>.+?)") ?)*'

m = match(pattern, html1)

print(m.groups())

print(m.groupdict())