w, h, x, y, p = map(int, input().split())

circle_x1, circle_y1 = x, (y+ (h / 2))
circle_x2, circle_y2 = x + w, (y+ (h / 2))

cnt = 0
# 선수들 탐색
for i in range(p):
    srch_x, srch_y = map(int, input().split())
    if x <= srch_x <= x + w and y <= srch_y <= y + h : # 직사각형
        cnt += 1
    elif (h / 2)** 2 >= ((circle_x1 - srch_x) ** 2 + (circle_y1 - srch_y)**2): # 반원 1
        cnt += 1
    elif (h / 2)** 2 >= ((circle_x2 - srch_x) ** 2 + (circle_y2 - srch_y)**2): # 반원 2
        cnt += 1
print(cnt)