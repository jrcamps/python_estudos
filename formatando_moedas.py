import locale

class FormatarMoeda:
    def __init__(self,valor,moeda_destino):
        self.valor = valor
        self.moeda_destino = moeda_destino
        self.formatando_moeda(self.moeda_destino)

    def __str__(self):
        return f'{self.formatando_moeda(self.moeda_destino)}'

    def formatando_moeda(self,moeda_destino):
        locale_brasil = 'pt_BR.UTF-8'
        locale_usa = 'en_US.UTF-8'
        locale_portugal = 'pt_PT.UTF-8'
        
        if moeda_destino == 'brasil':
            locale.setlocale(locale.LC_MONETARY,locale_brasil)
            return locale.currency(self.valor, grouping=True)
        elif moeda_destino == 'usa':
            locale.setlocale(locale.LC_MONETARY,locale_usa)
            return locale.currency(self.valor, grouping=True)
        elif moeda_destino == 'portugal':
            locale.setlocale(locale.LC_MONETARY,locale_portugal)
            return locale.currency(self.valor, grouping=True)
        
#TESTE
teste_brasil = FormatarMoeda(5350.23,'brasil')
print(teste_brasil)

# br = 5,30

# valor_dolar = 4,95
# valor_euro = 5,37

# locale_brasil = 'pt_BR.UTF-8'
# locale_usa = 'en_US.UTF-8'
# locale_portugal = 'pt_PT.UTF-8'

# locale.setlocale(locale.LC_MONETARY,locale_brasil)
# valor_real_formatado = locale.currency(5000,30, grouping=True)

# print(valor_real_formatado)


