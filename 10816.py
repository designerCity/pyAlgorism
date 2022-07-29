import sys
input = sys.stdin.readline

n = int(input())
all = list(map(int, input().split()))
dict_all = dict()
# dictionary 는 key-value 로 이루어져 있다.
for i in all:
    if i in dict_all: # 아래 코드에서 1인 value 에 1 씩 더해준다.
        dict_all[i] += 1
    else: # 처음 실행에 key - value 를 이어주는 역할을 한다.
        dict_all[i] = 1

num = int(input())
srch = list(map(int, input().split()))

for i in srch:
    if i in dict_all:
        print(dict_all[i], end=' ')
    else:
        print(0, end=' ')