# ## 처음에 최단 거리에 원을 뚫고 지나가는지에 대한 문제라고 생각하고 풀었다
# from math import sqrt

# T = int(input())

# for _ in range(T):
#     x1, y1, x2, y2 = map(int, input().split())
#     n = int(input())
#     cnt = 0
#     for _ in range(n):
#         a, b, r = map(int, input().split())
#         distance = abs((a * (y2-y1) - b * (x2-x1) -x1* y2 + x2*y1) / sqrt((y2-y1)**2 + (x2-x1)**2))
#         if distance < r:
#             cnt += 1
        
#     print(cnt)

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        a, b, r = map(int, input().split())
        d1 = (((x1 - a) ** 2) + ((y1 - b) ** 2)) ** 0.5
        d2 = (((x2 - a) ** 2) + ((y2 - b) ** 2)) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    print(cnt)