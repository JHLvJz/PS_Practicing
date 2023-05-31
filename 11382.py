# readine()과 readlines() 구분을 못했다. rstrip()은 어떨 때 필요한 것일까?
# https://velog.io/@ohjiae/sys.stdin.readline%EC%99%80-readlines%EC%9D%98-%EC%B0%A8%EC%9D%B4feat.%EB%B0%B1%EC%A4%80

import sys

a, b, c = map(int, sys.stdin.readline().split())
print(a + b + c)