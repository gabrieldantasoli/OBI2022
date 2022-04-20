# GITHUB = gabrieldantasoli
# OBI = 2021 , Escher

nmrsSequencia = int(input())
sequencia = input().split()

escher = True
pares = []

if len(sequencia) % 2 == 0:
    for num in range(int(len(sequencia) / 2)):        
        pares.append(int(sequencia[num]) + int(sequencia[(num * -1) - 1]))
else: escher = False

if len(pares) > 0:
    if pares.count(pares[0]) != len(pares):
        escher = False

if escher:
    print('S')
else:
    print('N')
