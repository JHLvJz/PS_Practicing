### 메모리 초과 관리하기
# sort / sorted를 쓰는 게 메모리에 어떤 영향이 있는가?
# 파이썬 배열은 메모리에 얼만큼의 영향을 미치는가? (배열이 차지하는 메모리의 문제는 아니었던 것 같다)
# 배열.append는 메모리 재할당이 이루어진다는데, 무슨 말인지?
# 파이썬이 메모리를 관리하는 방법? C언어랑 다르게 자료형 지정도 안하니까 .. 어떤 과정을 거칠까?

import sys

N = int(sys.stdin.readline())
numbers = [0] * 10001

for i in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)
