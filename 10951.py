# try / except 쓸 때✅
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break

# sys모듈 쓸 때
import sys

lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a+b)