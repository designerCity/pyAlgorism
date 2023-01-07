## 풀이 2
n = int(input())
n_list = list(map(int, input().split()))

li = [0] * (n)
for i in range(n): # 기준이 되는 index
    for j in range(i): # 각 index 에서의 길이
        if n_list[j] < n_list[i] and li[j] > li[i]:
            li[i] = li[j]
    li[i] += 1 
# print(li)
print(max(li))
