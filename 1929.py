### 미해결
# 시간초과, 에라토스테네의 체?
import sys
A, B = map(int, sys.stdin.readline().split())

for number in range(A, B+1):
    count = 0
    for part in range(2, number):
        if number % part == 0:
            count += 1
            break
    if count == 0:
        print(number)

