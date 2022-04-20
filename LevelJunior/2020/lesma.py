# GITHUB = gabrieldantasoli
# OBI - 2020 , Dona Lesma

altura = int(input())
sobedia = int(input())
descenoite = int(input())

alturaLesma = 0
dias = 0

while True:
    alturaLesma += sobedia
    dias += 1
    if alturaLesma >= altura: break
    alturaLesma -= descenoite

print(dias)
