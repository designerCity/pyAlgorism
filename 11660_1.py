# 시간 초과 실패
n, m = map(int, input().split())
matrix = [] # 이 matrix 는 n * n 이다.
for _ in range(n):
    matrix.append(list(map(int, input().split())))

try_li = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    # 한 행에서 y1 ~ 
    # 한 행에서 실행되어야 하는 횟수 : y2 - y1 + 1
    for i in range(x1 - 1, x2):
        # 몇 번의 행이 실행되어야 하는가? : x2 - x1 + 1
        for j in range(y1 - 1, y2):
            cnt += matrix[i][j]
    print(cnt)
