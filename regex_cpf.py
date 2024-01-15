"""
Caracteres:	    Descrição:	                                                     Exemplos:
[]	            Define um range ou um grupo de caracteres	                     [0-9]; [a-z]; [abc]
*	            Marca nenhuma, uma ou mais ocorrências	                         sol*
{}	            Quantidade de repetições de uma ocorrência definida	             [abc]{5}
\d	            Qualquer número de 0 até 9	                                     \d{3,4}
\w	            Qualquer número de a té 9 letra de a até z ou _	                 \w{10}
|	            Um ou outro	                                                     @|$
()	            Captura e agrupa	                                             (\w{4})
"""

import re

padrao = 'xxx.xxx.xxx-xx'
regex_padrao = '[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}'
texto = 'O cpf é esse 71689941255 ou 7416898941255'

buscar = re.search(regex_padrao,texto)
print(buscar.group())