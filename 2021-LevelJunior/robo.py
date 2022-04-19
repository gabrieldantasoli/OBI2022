# GITHUB = gabrieldantasoli
# OBI - 2021 , robo

info = input()
info = info.split()

estacoes = int(info[0])
comandos = int(info[1])
proxima = int(info[2])

sequencia = input()
sequencia = sequencia.split()

estacaoAtual = 1
total = 0

if estacaoAtual == proxima:
    total += 1

for comando in sequencia:
    estacaoAtual += int(comando)
    if estacaoAtual < 1:
        estacaoAtual = estacoes
    elif estacaoAtual > estacoes:
        estacaoAtual = 1
    if estacaoAtual == proxima:
        total += 1

print(total)
