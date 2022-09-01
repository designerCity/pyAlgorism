# 기본적인 아이디어
# 1. 가로줄, 세로줄, 3 * 3 정사각형 중에 빈칸이 하나만 있는 것 탐색
# 2. 빠진 숫자 채우기
import sys
# input 의 구성은 9 * 9 이다. 
input = sys.stdin.readline
sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

# 1-9에서 탐색하여 채워 넣는 코드 / line 은 list
def srchRow(line):
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx = 0
    for i in range(9):
        if sudoku[line][i] == 0:
            idx = i
            continue
        else:
            oneToNine.remove(sudoku[line][i])
    sudoku[line][idx] = oneToNine[0]
    return sudoku[line]

def srchColumn(line):
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx = 0
    for i in range(9):
        if sudoku[i][line] == 0:
            idx = i
            continue
        else:
            oneToNine.remove(sudoku[i][line])
    sudoku[idx][line] = oneToNine[0]
    return sudoku
# 세로줄 탐색
# 3 * 3 의 네모 박스를 해결하면 완료된다.

def srch_box(c, r):
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx1 = 0
    idx2 = 0
    for i in range(c - 1, c + 2):
        for j in range(r - 1, r + 2):
            if sudoku[i][j] == 0:
                idx1 = i
                idx2 = j
                # continue
            else:
                oneToNine.remove(sudoku[i][j])
    if len(oneToNine) == 1:
        sudoku[idx1][idx2] = oneToNine[0]
    return sudoku

# 가로줄 탐색
for j in range(9):
    zero = 0
    for i in range(9):
        if sudoku[j][i] == 0:
            zero += 1
    # zero 가 1개 이면
    if zero == 1:
        srchRow(j)

for j in range(9):
    zero_vtcl = 0
    for i in range(9):
        if sudoku[i][j] == 0:
            zero_vtcl += 1
    if zero_vtcl == 1:
        srchColumn(j)

c = 1
while c <= 7:
    r = 1
    # srch_box(c, r)
    while r <= 7:
        srch_box(c, r)
        r += 3
    c += 3
for i in range(9):
    li = sudoku[i]
    for j in range(9):
        if j == 8:
            print(li[j])
        else:
            print(li[j], end=' ')

