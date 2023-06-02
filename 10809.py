#오 재밌어

import sys
word = sys.stdin.readline()

howMany = ord('z') - ord('a') + 1
positions = [0] * howMany

for i in range(ord('a'), ord('z')+1):
    if chr(i) in word:
        positions[i - ord('a')] = word.index(chr(i))
    else:
        positions[i-ord('a')] = -1

for position in positions:
    print(position, end=' ')
