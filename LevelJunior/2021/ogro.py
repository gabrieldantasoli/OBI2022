# GITHUB = gabrieldantasoli
# OBI - 2021 , Ogro

numero = int(input())

mao1 = ''
mao2 = ''

if numero > 5:
    mao1 = 'I' * 5
    numero -= 5
    mao2 = 'I' * numero
else:
    if numero == 0: mao1 = '*' 
    else: mao1 = 'I' * numero
    mao2 = '*'

print(mao1)
print(mao2)
