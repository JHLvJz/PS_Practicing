#파이썬 딕셔너리 다루는 것을 거의 하나도 모른다

import sys

word = sys.stdin.readline().rstrip().upper()
freq = dict()

for letter in word:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

maxWords = []

for key, value in freq.items():
    if value == max(freq.values()):
        maxWords.append(key)

if len(maxWords) > 1:
    print('?')
else:
    print(maxWords[0])