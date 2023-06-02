#파이썬 입력받은 것 중 str그대로와 Int로 바꿔 활용할 것들을 구별 잘하기
#제한 시간 1초의 의미? 삼중 반복문을 안 쓰는 방법? 찾아보다가 엄청 오래걸렸다

import sys

testCase = int(sys.stdin.readline())

for i in range(testCase):
    newcode = ''

    repeat, code = sys.stdin.readline().split()
    for letter in code:
        for j in range(int(repeat)):
            newcode += letter
    
    print(newcode)
            
