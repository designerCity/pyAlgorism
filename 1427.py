# 84ms
N = int(input())
n_list = []
for i in str(N):
    n_list.append(int(i))
n_list.sort()
n_list.reverse()

num = ''
for j in n_list:
    num += str(j)
print(num)

# 72ms
import sys

input = sys.stdin.readline

num = list(input().rstrip())

num.sort(reverse=True)

print(''.join(num))