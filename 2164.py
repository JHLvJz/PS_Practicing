#시간초과? (2초 제한시간을 어떻게 인식해야하지)
#큐를 사용할 때랑 리스트 사용할 때랑 처리시간이 어떻게 다른 거지
#https://codingpractices.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%99%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8C%80%EC%8B%A0-%ED%81%90-%EB%8D%B0%ED%81%AC-deque-%EB%A5%BC-%EC%93%B8%EA%B9%8C

import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque(x for x in range(1, N+1))

#헐 컴프리핸션 안 쓴 게 문제였어 왜지...

while len(cards) > 1:
    #맨 위에 카드 버리기
    # del cards[0]
    cards.popleft()

    if(len(cards) == 1):
        break

    #그 위에 카드 맨 아래로 넣기

    # temp = cards[0]
    # for i in range(len(cards)-1): 
    #     cards[i] = cards[i+1]
    # cards[len(cards)-1] = temp

    # cards.rotate(-1)
    cards.append(cards.popleft())
    
print(cards[0])
