# Queen 은 같은 index 를 가질 수도, 같은 줄에 있을 수도 없다.
# # 대각선도 안됨.
n = int(input())
# 체스판 한 줄
chess = []
for i in range(n):
    chess.append(True)
# # 체스판
all = []
for j in range(n):
    all.append(chess)

cnt = 0
# # 경우의 수를 탐색
def dfs(depth): # idx 는 각 줄을 의미
    global all, cnt
    if depth == n :
        cnt += 1
        return

    # Queen이 각 줄에서 올 수 있는 경우의 수
    for i in range(n): # i 는 row 의 인덱스 을 의미한다.
        if all[depth][i] == True:     # depth 줄의 i 번째 index 가 기준이 된다.
            for j in range(depth, n): # j 지울려고 하는 row
                all[j][i] = False     # 같은 세로 줄
                if i + j - depth < n:
                    all[j][i + j - depth] = False  # 대각선 오른쪽
                if i - j + depth >= 0:
                    all[j][i - j + depth]  = False # 대각선 오른쪽
            dfs(depth + 1)
            
dfs(0)
print(cnt)
