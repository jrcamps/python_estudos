from datetime import datetime, timedelta

class DataCadastro:
    def __init__(self):
        self.momento_cadastro = datetime.today() #Pegando a data/hora atuais

    def __str__(self):
        return self.formatar_data()

    def get_mes_atual(self):
        meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro']
        indice_mes = self.momento_cadastro.month - 1
        return meses[indice_mes]
    
    def get_dia_da_semana(self):
        dia_da_semana = ['segunda-feira','terca-feira','quarta-feira','quinta-feira','sexta-feira','sabado','domingo']
        indice_dia = self.momento_cadastro.weekday()
        return dia_da_semana[indice_dia]
    
    def formatar_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada
    
#TESTE
cadastro = DataCadastro()
print(cadastro.momento_cadastro)
print(cadastro.get_mes_atual())
print(cadastro.get_dia_da_semana())
# print(cadastro.formatar_data())
print(cadastro)