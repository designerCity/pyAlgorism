n, k = map(int, input().split())
num_li = list(map(int, input().split()))

sum_li = [0]
sum_num = 0
for i in num_li:
    sum_num += i
    sum_li.append(sum_num)
# print(sum_li)
li = []
for i in range(k, n+1):
    li.append(sum_li[i] - sum_li[i - k])
# print(li)
print(max(li))
