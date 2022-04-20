# GITHUB = gabrieldantasoli
# OBI - 2020 , Jogo dos Pinos

lista = []
totalJogos = 0

for c in range(7):
    lista.append(input())

for x in range(len(lista) - 2):
    for y in range(len(lista) - 2):
        if lista[x][y] == 'o' and lista[x+1][y] == 'o' and lista[x+2][y] == '.':
            totalJogos += 1
        if lista[x+2][y] == 'o' and lista[x+1][y] == 'o' and lista[x][y] == '.':
            totalJogos += 1
        if lista[x][y] == 'o' and lista[x][y+1] == 'o' and lista[x][y+2] == '.':
            totalJogos += 1
        if lista[x][y+2] == 'o' and lista[x][y+1] == 'o' and lista[x][y] == '.':
            totalJogos += 1

print(totalJogos)
