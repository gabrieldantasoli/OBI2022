# GITHUB = gabrieldantasoli
# UFCG - studying for OBI

tests = int(input())

for test in range(tests):
    lis = input().split()

    valor1 = int(lis[0])
    valor2 = int(lis[1])

    operations1 = 0
    operations2 = 0
    
    while not valor1 > int(lis[2]):
        valor1 += int(lis[1])
        print(valor1)
        operations1 += 1
    
    while not valor2 > int(lis[2]):
        valor2 += int(lis[0]) 
        print(valor2)
        operations2 += 1
    
    if operations1 > operations2:
        print(operations2)
    elif operations1 < operations2:
        print(operations1)
    else:
        print(operations1)
