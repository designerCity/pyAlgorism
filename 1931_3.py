n = int(input())
time_li = []

for _ in range(n):
    time_li.append(list(map(int, input().split())))

time_li = sorted(time_li, key = lambda a: a[0])
time_li = sorted(time_li, key = lambda a: a[1])

last_time = 0 # 회의 마지막 시간
count = 0 # 회의 개수 

for i, j in time_li:
    if i >= last_time:
        count += 1
        last_time = j
print(count)
