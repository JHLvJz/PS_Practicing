
#문제를 제대로 읽자 ...

import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0
for number in numbers:
    flag = 0
    for i in range(2, number):
        if number % i == 0:
            flag += 1
    if flag == 0 and number != 1:
        count += 1

print(count)
