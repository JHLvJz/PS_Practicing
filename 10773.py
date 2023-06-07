import sys

howMany = int(sys.stdin.readline())
numbers = []
sum = 0

for i in range(howMany):
    newNum = int(sys.stdin.readline())

    if(newNum == 0):
        numbers.pop()
    else:
        numbers.append(newNum)

for number in numbers:
    sum += number

print(sum)