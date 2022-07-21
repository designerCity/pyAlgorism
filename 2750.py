n = int(input()) # 입력값의 개수
n_list = []

for i in range(n):
    num_input = int(input())
    n_list.append(num_input)

n_list.sort()
for i in range(n):
    print(n_list[i])