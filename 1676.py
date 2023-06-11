import sys

N = int(sys.stdin.readline())
sum = 1
result = 0

for i in range(1,N+1):
    sum *= i

strSum = list(str(sum))[::-1]

for number in strSum:
    if number != '0':
        break
    else:
        result += 1

print(result)