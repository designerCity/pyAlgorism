# 내 코드 4580ms
a, b = map(int, input().split())

hv_list = []
for _ in range(a):
    hv_list.append(input())
srch = []
for _ in range(b):
    srch.append((input()))

cnt = 0
for i in range(b):
    if srch[i] in hv_list:
        cnt +=1
        
print(cnt)

# # 다른 사람 코드 156ms
# import sys

# input = sys.stdin.readline
# tmp = 0
# N, M = map(int, input().split())

# S = set([input() for _ in range(N)])

# strs = [input() for _ in range(M)]

# for i in strs:
#     if i in S:
#         tmp += 1

# print(tmp)