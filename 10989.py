# import sys
# n = int(input())
# n_list = []

# for i in range(n):
#     num_input = int(sys.stdin.readline())
#     n_list.append(num_input)

# n_list.sort()
# for i in n_list:
#     print(i)
# ## 입력값을 하나씩 append 하였기 때문에 메오리 초과가 날 수 밖에 없다.

import sys
n = int(sys.stdin.readline())
n_list = [0] * 10001

# 입력값을 받을 때마다, 그 입력값과 같은 인덱스에 +1을 헤준다.
for _ in range(n):
    n_list[int(sys.stdin.readline())] += 1


for i in range(10001):
    if n_list[i] != 0:
        for _ in range(n_list[i]):
            print(i)