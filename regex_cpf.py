import re

padrao = 'xxx.xxx.xxx-xx'
regex_padrao = '[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}'
texto = 'O cpf é esse 71689941255 ou 7416898941255'

buscar = re.search(regex_padrao,texto)
print(buscar.group())