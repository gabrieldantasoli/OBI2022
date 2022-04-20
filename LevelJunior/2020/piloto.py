# GITHUB = gabrieldantasoli
# OBI - 2021 , Piloto Automático

A = int(input())
B = int(input())
C = int(input())

#1=acelerar 0=manter -1=desacelerar

B_A = B - A
C_B = C - B

if B_A < C_B:
    print(1)
elif B_A == C_B:
    print(0)
elif B_A > C_B:
    print(-1)
