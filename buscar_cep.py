class BuscarCEP:
    def __init__(self,cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP invalido!')
        
    def __str__(self):
        return self.formatar_cep()
        
    def validar_cep(self,cep):
        if len(cep) == 8:
            return True
        else:
            raise ValueError('O CEP deve conter 8 digitos')
        
    def formatar_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

#TESTE
cep = '13505534'
buscar_cep = BuscarCEP(cep)
print(buscar_cep)