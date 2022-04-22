# GITHUB = gabrieldantasoli
# UFCG - studying for OBI 2022

def reverseSort(list):
    for a in range(len(list)-1):
        for b in range(len(list)-1):
            if int(list[b]) <= int(list[b+1]):
                list[b] , list[b+1] = list[b+1] , list[b]

integers = input().split()
arrayLength = int(integers[0])
queries = int(integers[1])
array = input().split()
reverseSort(array)


for num in range(queries):
    numbers = input().split()
    action = int(numbers[0])
    position = int(numbers[1])
    if action == 1:
        array[position] = str(1 - int(array[position]))
        reverseSort(array)
    elif action == 2:
        print(array[int(int(position) - int(array[0]))])
