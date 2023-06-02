#index메소드 잊었음

import sys
numbers = []
max = 0

for i in range(9):
    tempNum = int(sys.stdin.readline())
    numbers.append(tempNum)

    if (tempNum > max):
        max = tempNum

print(max)
print(numbers.index(max) + 1)
