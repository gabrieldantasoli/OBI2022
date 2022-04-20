# GITHUB = gabrieldantasoli
# OBI - 2020 , Cobertura para Celular

import math

ilhas = []
distancias = [0]
arquipelago = int(input())

for num in range(arquipelago):
    ilha = input().split()
    ilhas.append(ilha)

cobertura = int(input())

for ilha in range(len(ilhas)-1):
    distancia = math.sqrt((int(ilhas[ilha][0]) - int(ilhas[ilha+1][0])) ** 2 - (int(ilhas[ilha][1]) - int(ilhas[ilha+1][1])))
    distancias.append(float(distancia))

for ilha1 in range(len(distancias) - 1):
    for ilha2 in range(1,len(distancias) - 1):
        if type(distancias[ilha1]) != str and type(distancias[ilha2]) != str:
            if distancias[ilha2] < cobertura:
                distancias[ilha1] = 'checado'
                break

if distancias.count('checado') == len(distancias) - 1:
    print('S')
else:
    print('N')
