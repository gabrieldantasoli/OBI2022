# GITHUB = gabrieldantasoli
# OBI - 2020 , Aplicativo de Calorias

#e1=minima 
#e2=maxima
#if :e3=e2-e1>x

E1 = int(input())
E2 = int(input())
E3 = int(input())
x = int(input())

if E2 - E1 <= x:
    print(E2)
elif E2 - E1 > x:
    print(E3)

