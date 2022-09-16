# RGB 거리
from operator import index


h = int(input())
all =[]
for _ in range(h):
    
    all.append(list(map(int, input().split())))


value = 0
li = [] # 기준이
# 각 집이 최솟값이 되는 리스트들을 담아할 것 같다.
for i in range(h):
    tmp = min(all[i])
    idx = all[i].index(tmp) # list min index 를 구하는 방법
    
    print(idx)
        

print(all)