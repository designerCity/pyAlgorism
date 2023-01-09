n = int(input())
n_list = list(map(int, input().split()))


li = [0] * (n) # 최대 개수를 담는 리스트
for i in range(n): # 기준이 되는 index
    for j in range(i): # 각 index 에서의 길이
        if n_list[j] < n_list[i] and li[j] > li[i]:
            li[i] = li[j]
    li[i] += 1

n_list = n_list[::-1]
a_li = [0] * n
for i in range(n): # 기준이 되는 index
    for j in range(i): # 각 index 에서의 길이
        if n_list[j] < n_list[i] and a_li[j] > a_li[i]:
            a_li[i] = a_li[j]
    a_li[i] += 1

# 리스트를 뒤집어서 해결하는 방법 : 정렬하는데 O(nln(n)) 의 시간을 사용하기 때문에 안되는 것 같음
sum_li = []
for i in range(n):
    # print(li[i] + a_li[i])
    sum_li.append(li[i] + a_li[n - i - 1])
print(max(sum_li) - 1)
