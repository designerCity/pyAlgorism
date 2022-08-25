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
def srch(line):
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
# 가로줄 탐색
for j in range(9):
    zero = 0
    for i in range(9):
        if sudoku[j][i] == 0:
            zero += 1
    # zero 가 1개 이면
    if zero == 1:
        srch(j)
print(sudoku)