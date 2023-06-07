import sys
while True:

    numbers = list(map(int, sys.stdin.readline().split()))
    endFlag = 0

    maxLen = 0
    maxIndex = numbers.index(max(numbers))

    largest = 0
    rest = 0

    for num in numbers:
        if num == 0:
            endFlag += 1
    
    if(endFlag == 3):
        break


    for i in range(3):
        if i == maxIndex:
            largest += numbers[i] * numbers[i]
        else:
            rest += numbers[i] * numbers[i]
    if rest == largest:
        print('right')
    else:
        print('wrong')


