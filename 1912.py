# 연속합
# 메모리 초과
t = int(input())
li = list(map(int, input().split()))

# 연속된 몇 개의 수를 선택해서 구할 수 있는 합
max_li = []
for i in range(t): # 기준이 되는 index
    if li[i] >=0 and t - i != 0: # 탐색 가능
        max_num = 0
        num = 0
        for j in range(t - i):  
            max_num += li[i + j]
            max_li.append(max_num)

print(max_li)
print(max(max_li))