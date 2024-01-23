dados = {
    1: {"nome": "Velozes e Furiosos",
        "avaliacao": "10/10"},
    2: {"nome": "Gente Grande",
        "avaliacao": "9/10"}
}

for value in dados.values():
    print(f'O filme {value['nome']}, possui uma avaliacao de {value['avaliacao']}')