import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 찾아야하는 빈칸 부터 탐색
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# # # a 가 들어 갈 수 있는 수 
# 각 Row 들을 탐색
def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

# Column 들을 탐색
def checkColumn(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkSquare(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx + i][ny + j]:
                return False
    return True

def sudoko(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i]) # * 빼고 실행 -> list 에서 벗어날 수 있음
        exit(0)
    
    for i in range(10):
        # 공백인 blank 의 좌표를 하나씩 받고, 그 이후에 차례로 실행시켜서 실행횟수와 blank 좌표 개수가 같을 때 벗어난다.
        x = blank[idx][0] 
        y = blank[idx][1]

        if checkRow(x, i) and checkColumn(y, i) and checkSquare(x, y ,i):
            graph[x][y] = i
            sudoko(idx + 1)
            graph[x][y] = 0
sudoko(0)