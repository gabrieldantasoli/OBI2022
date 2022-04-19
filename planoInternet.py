# Github = gabrieldantasoli
# OBI - 2021 , plano de internet

quotaMensal = int(input())

meses = int(input())

mesSeguinte = quotaMensal

for mes in range(meses):
    mesAtual = int(input())
    if mesAtual <= mesSeguinte:
        mesSeguinte -= mesAtual
        mesSeguinte += quotaMensal

print(mesSeguinte)
