# n = int(input())
# n_list = []
# for _ in range(n):
#     n_list.append(input())
# n_list = list(set(n_list))
# n_list.sort()
# n_list.sort(key= len)

# [print(i) for i in n_list]
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())
print(n_list)
n_list = list(set(n_list))
n_list.sort()
n_list.sort(key= len)

print(n_list)
[print(i) for i in n_list]