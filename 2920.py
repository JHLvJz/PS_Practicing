# 단순히 반복문의 탈출이 아니라 프로그램 종료를 하고 싶을 때 sys.exit()를 쓸 수 있다
# 여전히 리스트 메소드 익숙하지 않다

import sys

temp = sys.stdin.readline().split()

for i in range(7):
    test = int(temp[i]) - int(temp[i+1])
    if test < 0:
        test *= -1
    
    if test != 1:
        print('mixed')
        sys.exit()

if(temp.index(max(temp)) == len(temp)-1):
    print('ascending') 
   
else:
    print('descending')


        
