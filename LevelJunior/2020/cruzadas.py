# GITHUB = gabrieldantasoli
# OBI - 2020 , Palavras Cruzadas

horizontal = input()
vertical = input()

retorno = []

for h in range(len(horizontal) - 1, -1,-1):
    for v in range(len(vertical) - 1,-1,-1):
        if horizontal[h] == vertical[v]:
            retorno.append([h+1,v+1])

for x in range(len(retorno) - 1):
    for y in range(len(retorno) - 1):
        if retorno[x] > retorno[x+1]:
            retorno[x] , retorno[x+1] = retorno[x+1] , retorno[x]


if len(retorno) > 0:
    print(retorno[len(retorno)-1])
else:
    print('-1 -1')
