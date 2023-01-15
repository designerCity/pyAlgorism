persons = int(input())
time_li = list(map(int, input().split()))
time_li.sort()

all_time = []
for i in range(persons):
    time = 0
    for j in range(i+1):
        time += time_li[j]
    all_time.append(time)
print(sum(all_time))
