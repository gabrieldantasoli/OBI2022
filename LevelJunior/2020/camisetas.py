# GITHUB = gabrieldantasoli
# OBI - 2021 , Camisetas da olimpiada

premiados = int(input())
lista = input()
lista = lista.split()

tPequeno = int(input())
tMedio = int(input())

pequenas = 0
medias = 0

for num in range(len(lista)):
    if int(lista[num]) == 1:
        pequenas += 1        
    elif int(lista[num]) == 2:
        medias += 1

if tPequeno <= pequenas and tMedio <= medias:
    print('S')
else:
    print('N')

