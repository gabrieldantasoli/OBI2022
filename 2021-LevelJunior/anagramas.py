# Github = gabrieldantasoli
# OBI - 2021 , Anagramas

nmrLetras = int(input())
palavra1 = input()
palavra2 = input()

retorno = True

alfabeto = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'


for letra in palavra1:
    if palavra1.count(letra) != palavra2.count(letra) and letra in alfabeto:
        retorno = False 
        break

print(retorno)
