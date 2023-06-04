# readline()으로 입력받을 때 '\n'주의

import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '0':
        break
    
    length = len(word)
    middle = length // 2
    flag = 0
    for i in range(middle):
        if word[i] != word[length-i-1]:
            print('no')
            flag += 1
            break
    if flag == 0:
        print('yes')
    