import re

padrao = '(xx)xxxxx-xxxx'
regex_padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto = 'O telefone é esse 7218975211 ou 115554898856'

buscar = re.search(regex_padrao,texto)
print(buscar.group())