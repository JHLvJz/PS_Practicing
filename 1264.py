#입력 받는 방식 고민

import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '#':
        break

    count = 0

    for letter in line.lower():
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            count += 1
    print(count)
