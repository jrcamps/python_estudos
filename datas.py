from datetime import datetime, timedelta

class DataCadastro:
    def __init__(self):
        self.momento_cadastro = datetime.today() #Pegando a data/hora atuais

    def mes_atual(self):
        meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro']
        indice_mes = self.momento_cadastro.month - 1
        return meses[indice_mes]
    
    def dia_da_semana(self):
        dia_da_semana = ['segunda-feira','terca-feira','quarta-feira','quinta-feira','sexta-feira','sabado','domingo']
        indice_dia = self.momento_cadastro.weekday()
        return dia_da_semana[indice_dia]

#TESTE
cadastro = DataCadastro()
print(cadastro.momento_cadastro)
print(cadastro.mes_atual())
print(cadastro.dia_da_semana())