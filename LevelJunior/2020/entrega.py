# GITHUB = gabrieldantasoli
# OBI - 2021 , Entrega das caixas

caixa1 = int(input())
caixa2 = int(input())
caixa3 = int(input())

if caixa1 == caixa2 and caixa2 == caixa3:
    viagems = 3
elif caixa1 + caixa2 < caixa3:
    viagems = 1
elif caixa1 < caixa2 and caixa2 == caixa3:
    viagems = 2
elif caixa1 == caixa2 and caixa2 < caixa3:
    viagems = 2
elif caixa1 < caixa2 and caixa2 < caixa3:
    viagems = 1
elif caixa1 ==  caixa2 and caixa2 <  caixa3:
    viagems = 22 

print(viagems)
