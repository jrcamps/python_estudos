import re

class Telefone():
    def __init__(self,numero):
        if self.validar(numero):
            self.telefone = numero
        else:
            raise ValueError('Numero invalido!')
        
    def __str__(self):
        return self.formatar_numero()

    def validar(self,numero):
        regex_padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        validando = re.findall(regex_padrao,numero)
        return validando
    
    def formatar_numero(self):
        regex_padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(regex_padrao,self.telefone)
        telefone_formatado = f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
        return telefone_formatado
    
#TESTE
num = '551996543129'
#num = '19965431297'
#num = '965431297'

teste = Telefone(num)
print(teste)