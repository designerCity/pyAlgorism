n = int(input())

n_list = list(map(int, input().split()))

li = []
for i in range(n): # 기준이 되는 index
    a = [n_list[i]]
    for j in range(i): # 각 index 에서의 길이
        if n_list[i] > n_list[j] :
            if j == 0:
                a.append(n_list[j])
            if j != 0 and a[-1] < n_list[j]:
                a.append(n_list[j])
    li.append(a)
print(len(max(li)))
