"""
Validação - CPF deve contem 11 dígitos e utilizar biblioteca de validação
Máscara - 000.000.000-00
"""

from validate_docbr import CPF

class Cpf:
    def __init__(self,cpf):
        documento = str(cpf)
        if self.validar_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')
        
    def __str__(self):
        return self.formatar_cpf()

    def validar_cpf(self,documento):
        if len(documento) == 11:
          cpf =  CPF()
          return cpf.validate(documento) 
        else:
            raise ValueError('O CPF deve conter 11 dígitos!')
        
    def formatar_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

# TESTANDO
    
teste_cpf = Cpf('44705391802')
print(teste_cpf)