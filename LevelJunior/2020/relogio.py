# GITHUB = gabrieldantasoli
# OBI - 2021 , Relógio de Atleta

FreCardRepouso = int(input())
FreCardAtual = int(input())
OxigenAtual = int(input())

if FreCardAtual > FreCardRepouso * 3 or OxigenAtual < 95:
    print('diminuir')
elif FreCardAtual < FreCardRepouso or OxigenAtual > 97:
    print('aumentar')
else:
    print('manter')
