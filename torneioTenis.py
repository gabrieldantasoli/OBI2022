# Github: gabrieldantasoli
# OBI - 2021 , Torneio de Tenis

ganhou = 0

for partida in range(6):
    situacao = input()
    if situacao == 'V':
        ganhou += 1

if ganhou == 6 or ganhou == 5: print(1)
elif ganhou == 4 or ganhou == 3: print(2)
elif ganhou == 2 or ganhou == 1: print(3)
else: print(-1)
