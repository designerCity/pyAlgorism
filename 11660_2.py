# 반복문으로 input 을 받을 때는 sys.stdin.readline 을 사용하는 곳이 매우 좋다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
matrix = [] # 이 matrix 는 n * n 이다.
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sum_matrix = [[0] * (n+1) for i in range(n+1)]
for i in range(1, n+ 1):
    for j in range(1, n + 1): # 좌측 우측에 한 행, 한 열이 matrix 보다 sum_matrix 가 많다.   
        sum_matrix[i][j] = sum_matrix[i][j-1] - sum_matrix[i-1][j-1] + sum_matrix[i-1][j] + matrix[i-1][j-1]


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 모두의 합에서 x2, y2을 기준으로 처음의 열을 빼고, 시작의 전 행 전부를 빼고 시작의 대각선을 더해주면 됨.
    print(sum_matrix[x2][y2] -  sum_matrix[x2][y1-1] - sum_matrix[x1-1][y2] + sum_matrix[x1-1][y1-1])
