#딕셔너리 다루는 거 아직도 부족

import sys 
freq = dict()
result = 0

for i in range(10):
    num = int(sys.stdin.readline())
    num = num % 42

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(len(freq.keys()))