import sys
finalNum = 1
freqs = [0,0,0,0,0,0,0,0,0,0]

for i in range(3):
    finalNum *= int(sys.stdin.readline())

result = list(str(finalNum))

for num in result:
    freqs[int(num)] += 1

for freq in freqs:
    print(freq)