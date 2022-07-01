# sys 모듈을 이용해서 빠르게 더하기

import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
