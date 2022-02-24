"""
Expressões regulares suportam repetições.
"""
from re import match

#Com quantidades específicas

print(match(r'\d{4}', '1234')) #pega apenas 4 e se tiver menos retorna None

print(match(r'\d{2,}', '12'))

print(match(r'\d{2,}?', '12345'))


#Min e max

print(match(r'\d{2,4}', '12345'))

print(match(r'\d{2,4}?', '12345'))


# 0 ou 1 ocorrência

print(match(r'\d{0,1}', '12345'))

print(match(r'\d{,1}', '12345'))


# 0 ou mais 

print(match(r'\d{0,}', '12345'))

print(match(r'\d{,}', '12345'))



#Match Object

m = match(r'\d+', '12345')

print(type(m))

#group retorna com quem ele fez match
print(m.group())

#start onde começou o match
print(m.start())

#end onde termina o match
print(m.end())

#span primeiro e ultimo
print(m.span())

html1 = '<input type="text" id="id_cpf" name="cpf">'


pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'

m = match(pattern, html1)

print(m)

print(m.groups())

print(m.group())






