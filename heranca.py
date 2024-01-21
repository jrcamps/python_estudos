class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Estado: {'Ligado' if self._ligado == True else 'Desligado'}'
    
    def ligar_veiculo(self):
        self._ligado = True
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{super().__str__()} | Portas: {self.portas}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} | Tipo: {self.tipo}'
    

carro1 = Carro('Chevrolet', 'Agile', 4)
carro2 = Carro('Citroen', 'C4', 4)
carro3 = Carro('Ferrari', '458', 2)

moto1 = Moto('Honda', 'Titan', 'Casual')
moto2 = Moto('Yamaha', 'Fazer 250', 'Casual')
moto3 = Moto('Kawasaki', 'Z1000', 'Esportiva')

# carro1.ligar_veiculo()

print('---- Carros:')
print(carro1)
print(carro2)
print(carro3)



print('---- Motos:')
print(moto1)
print(moto2)
print(moto3)