#절대오차, 상대오차의 개념

import sys

subjectNum = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

maxScore = max(scores)
sum = 0

for i in range(subjectNum):
    scores[i] = scores[i] / maxScore * 100
    sum += scores[i]

print( sum / subjectNum)