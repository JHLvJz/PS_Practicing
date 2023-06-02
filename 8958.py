# 나의 실수 찾는 거 재밌었다ㅎㅎ...

import sys

testCase = int(sys.stdin.readline())

for i in range(testCase):
    score = 0
    sequence = 1
    
    result = sys.stdin.readline()
    result = list(result)

    for i in range(len(result)):
        if result[i] == 'O':
            score += sequence
            sequence += 1
        else:
            sequence = 1
    print(score)