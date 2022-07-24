# # 내 코드 시간 단축 352ms
# import sys
# input = sys.stdin.readline

# N = int(input())
# n_list =[]

# for _ in range(N):
#     a, b = map(int, input().split())

#     n_list.append([a, b])
# n_list.sort()

# for i in n_list:
#     print(i[0], i[1])

### 시간 단축 352ms
# from sys import stdin
# input = stdin.readline

# coord = []
# for _ in range(int(input())):
# 	x, y = map(int, input().split())
# 	coord.append((x, y))

# coord.sort()
# [print(i[0], i[1]) for i in coord]

### 최적 코드 240ms 
import sys

lst = sys.stdin.readlines()[1:]
lst.sort(key=lambda x: int(x.split()[1]))
lst.sort(key=lambda x: int(x.split()[0]))
print(''.join(lst))