#Github : gabrieldantasoli
#OBI - 2021 , idade de camila

idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

if idade3 < idade1:
    idade3 , idade1 = idade1 , idade3
if idade2 < idade1:
    idade2 , idade1 = idade1 , idade2
if idade3 < idade2:
    idade3 , idade2 = idade2 , idade3

print(idade2)
