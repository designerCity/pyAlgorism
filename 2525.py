hour, min = map(int, input().split())
run_time = int(input())

hour += run_time // 60
min += run_time % 60 

if min > 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24

print("%d %d\n", hour, min)