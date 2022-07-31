import math 
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) 
    distance = math.sqrt((x2 - x1) ** 2 + (y2-y1)** 2)
    r_dt = abs(r1 - r2)
    if distance == 0 and r1 == r2:
        print(-1)
    else:    
        if r_dt == distance or r1 + r2 == distance: # 내접 or 외접
            print(1)
        elif r_dt < distance < r1 + r2:
            print(2)
        else:
            print(0)
