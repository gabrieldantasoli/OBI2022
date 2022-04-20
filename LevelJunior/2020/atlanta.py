# GITHUB = gabrieldantasoli
# OBI - 2020 , Atlanta

Azuis = int(input())
Brancos = int(input())

dimensoesBrancos = ''
divisores = []

if (Brancos ** (1 / 2)) *( Brancos ** (1/2))  == Brancos:
    dimensoesBrancos = f'{int(Brancos ** (1/2))+2} {int(Brancos ** (1/2))+2}'
else:
    for divisor in range(1,Brancos + 1):
        if Brancos % divisor == 0:
            divisores.append(divisor)
    if (divisores[0] * 2) + (divisores[1] * 2) + 4 == Azuis:
        dimensoesBrancos = f'{divisores[int((len(divisores)/2)-1)]+2} {divisores[int(len(divisores)/2)]+2}'
    else: 
        dimensoesBrancos = '-1 -1'

print(dimensoesBrancos)
