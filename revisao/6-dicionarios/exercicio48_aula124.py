"""
Crie um dicionario com jogos que você gosta e sua pontuação para o jogo;
Imprima estes valores no terminal
"""
jogos = {
    "cod": 10,
    "lol": 5,
    "tibia": 1,
    "poe2": 9
}

print(jogos)

for x in jogos:
    print(f'O jogo {x}, na minha opniao é nota {jogos[x]}')