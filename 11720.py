#처음에 숫자 개수를 testCase로 받아야 하는 이유가 뭐지..?

import sys

testCase = int(sys.stdin.readline())
number = list(sys.stdin.readline().rstrip())

sum = 0
for num in number:
    sum += int(num)
print(sum)