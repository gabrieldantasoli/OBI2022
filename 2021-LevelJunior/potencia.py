# GITHUB = gabrieldantasoli
# OBI - 2021 , Potência

nmr = int(input())

soma = 0

for num in range(nmr):
    num = int(input())
    if num >= 10:
        numero = num // 10
        expoente = num % 10
        soma += numero ** expoente
    else:
        soma += num

print(soma)
