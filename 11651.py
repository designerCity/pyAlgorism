import sys
input = sys.stdin.readline

N = int(input())
n_list =[]

for _ in range(N):
    a, b = map(int, input().split())

    n_list.append([a, b])
n_list.sort(key=lambda x: int(x[0]))
n_list.sort(key=lambda x: int(x[1]))

[print(i[0], i[1]) for i in n_list]


# from sys import stdin
# input = stdin.readline

# coord = []
# for _ in range(int(input())):
# 	x, y = map(int, input().split())
# 	coord.append((y, x))

# coord.sort()
# [print(i[1], i[0]) for i in coord]