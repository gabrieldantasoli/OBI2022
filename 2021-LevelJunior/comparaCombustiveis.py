# Github: gabrieldantasoli
# OBI - 2021 , Pesquisa de Preços

nmrEstados = int(input())

estados = []

for estado in range(nmrEstados):
    estado = input()
    estado = estado.split()
    if float(estado[1]) <= float(estado[2]) * 0.7:
        estados.append(estado[0])

if len(estados) > 0:
    for c in estados:
        print(c)
else:
    print('*')
