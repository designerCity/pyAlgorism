# # 좌표 압축
# n = int(input())
# n_list = list(map(int, input().split()))
# num = 0
# set_list = list(set(n_list))
# # 탐색하고자 하는 index 
# for i in range(n):
#     num = 0
#     for j in range(len(set_list)):
#         if n_list[i] > set_list[j]:
#             num += 1
#     print(num, end=' ')

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
set_list = sorted(list(set(n_list)))
dict = {set_list[i] : i for i in range(len(set_list))}
for i in n_list:
    print(dict[i], end=' ')
