"""
Validação CPF - Deve contem 11 dígitos e utilizar biblioteca de validação
Máscara - 000.000.000-00

Validação CNPJ - Deve contem 14 dígitos e utilizar biblioteca de validação
Máscara - 00.000.000/0000-00
"""

from validate_docbr import CPF,CNPJ

class Documento:
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return CriarCPF(documento)
        elif len(documento) == 14:
            return CriarCNPJ(documento)
        else:
            raise ValueError('Quantidade de digitos incorreta!')
        
class CriarCPF():
    def __init__(self, documento):
        documento = str(documento)
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF invalido!')

    def __str__(self):
        return self.formatar()
    
    def validar(self,documento):
          cpf =  CPF()
          return cpf.validate(documento) 
        
    def formatar(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
class CriarCNPJ():
    def __init__(self, documento):
        documento = str(documento)
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ invalido!')

    def __str__(self):
        return self.formatar()

    def validar(self,documento):
          cnpj =  CNPJ()
          return cnpj.validate(documento) 

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj) 
    
# TESTE
    
doc = '39049714099' #CPF válido
#doc = '39049714098' #CPF inválido
#doc = '3904971409'  #CPF com menos de 11 digitos
#doc = '74233403000117' #CNPJ válido
#doc = '74233403000116' #CNPJ inválido
#doc = '7423340300011' #CNPJ com menos de 14 digitos

teste = Documento.criar_documento(doc)
print(teste)