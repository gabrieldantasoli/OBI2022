# GITHUB = gabrieldantasoli
# OBI - 2021 , Casamento de Inteiros

numeroA = input()
numeroB = input()

listaA = []
listaB = []

for a in numeroA:
    listaA.append(a)

for b in numeroB:
    listaB .append(b)

while len(listaB) != len(listaA):
    if len(listaA) > len(listaB):
        listaB.insert(0,0)
    elif len(listaA) < len(listaB):
        listaA.insert(0,0)

numeroA = ''
numeroB = ''

for index in range(len(listaA)):
    if int(listaA[index]) > int(listaB[index]):
        listaB[index] = 'removed'
    elif int(listaA[index]) < int(listaB[index]):
        listaA[index] = 'removed'

    if listaA[index] != 'removed':
        numeroA += listaA[index]
    if listaB[index] != 'removed':
        numeroB += listaB[index]

if numeroA == '':
    numeroA = -1

if numeroB == '':
    numeroB = -1

saida = [int(numeroA),int(numeroB)]
saida.sort()

print(f'{saida[0]} {saida[1]}')
