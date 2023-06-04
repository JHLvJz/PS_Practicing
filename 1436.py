### 미해결
### 참고한 답1
# https://god-gil.tistory.com/63 

N = int(input())
first = 666#처음 666인 수
while N != 0:# N 이 0이 아니면 계속 반복
    if '666' in str(first): # 만약 666이란 문자열이 문자열(first)안에 있으면
        N = N-1# N을 1 감소시키고
        if N == 0:# 만약 N 이 0이면
            break# 반복문을 탈출한다.
    first = first + 1#first의 값을 1 증가시킨다.
print(first)

# 대부분이 이런 식이네... 나는 수학적 규칙을 찾으려고 했는데
# 브루트포스 방식의 패턴들을 정리하고 기억해보자 ...