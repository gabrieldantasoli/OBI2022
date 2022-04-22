# GITHUB - gabrieldantasoli
# UFCG - studying to OBI - 2022

tests = int(input())

for indice in range(tests):
    yes = True
    testMade = ''
    tasks = int(input())
    test = input().upper()
    for task in test:
        if testMade == '':
            testMade += task
        else:
            if testMade[len(testMade) - 1] == task:
                testMade += task
            else:
                if not task in testMade:
                    testMade += task
                else:
                    yes = False
                    break
    if yes:
        print('YES')
    else:
        print('NO')
