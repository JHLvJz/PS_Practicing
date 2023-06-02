# 입력 받을 때 내가 해당 값을 어떻게 변형하여 변수에 저장했는지 유의하자
# 최대 최소를 판단해야하는 '값의 범위'를 정확히 보자! 입력 받을 수 있는 숫자 범위가 다 다르다.

import sys

testCase = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

maxNum = -1000000
minNum = 1000000

for i in range(testCase):
    if numbers[i] > maxNum:
        maxNum = numbers[i]
    if numbers[i] < minNum:
        minNum = numbers[i]

print(minNum, maxNum)