import requests

class BuscarCEP:
    def __init__(self,cep):
        if self.validar_cep(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError('CEP invalido!')
        
    def __str__(self):
        return f'{self.formatar_cep()}\n{self.buscar_cep_api()}'
        
    def validar_cep(self,cep):
        if len(cep) == 8:
            return True
        else:
            raise ValueError('O CEP deve conter 8 digitos')
        
    def formatar_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def buscar_cep_api(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        json = r.json()
        logradouro = json['logradouro']
        bairro = json['bairro']
        localidade = json['localidade']
        uf = json['uf']
        return f'{logradouro}, {bairro}, {localidade}-{uf}'

#TESTE
cep = 13505543
buscar_cep = BuscarCEP(cep)
print(buscar_cep)
# print(buscar_cep.buscar_cep_api())