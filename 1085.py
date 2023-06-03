import sys

x, y, w, h = map(int, sys.stdin.readline().split())

minDis = 1000
distances = [x, y, w-x, h-y]

for i in range(4):
    if minDis > distances[i]:
        minDis = distances[i]

print(minDis)