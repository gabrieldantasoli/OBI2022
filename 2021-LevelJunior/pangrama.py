alfabeto = 'abcdefghijlmnopqrstuvxz'

palavra = input()

retorno = True

for letra in alfabeto:
    try:
        x = palavra.index(letra)
    except:
        retorno = False
        break

if retorno:
    print('S')
else:
    print('N')
