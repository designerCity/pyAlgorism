# N - Queen

# N - Queen 문제는 크기가 N * N 인 체스판 위에 퀸 N 개를 서로 공격할 수 없게 놓는 문제이다. 
# N 이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성해라

# Queen 은 같은 index 를 가질 수도, 같은 줄에 있을 수도 없다.
# # 대각선도 안됨.
n = int(input())
# 체스판
# # list 안에 list 를 집어 넣어야 한다.
chess = []
for i in range(n):
    chess.append(True)

all = []
for j in range(n):
    all.append(chess)



cnt = 0
# # 경우의 수를 탐색
def dfs(idx): # idx 는 각 줄을 의미
    global all, cnt
    if idx == n:
        cnt += 1
        return
    # Queen이 각 줄에서 올 수 있는 경우의 수
    for i in range(len(all[idx])):
        if all[idx][i] == True:
            dfs(idx + 1)
            
    # # 안되는 것을 지우는 코드
    # for i in range(len(all[idx])):
    #     all[idx][idx] = True
    #     if idx + i <= len(idx) - 1:
    #         all[idx][idx + i] = True
    #     if idx - i >= 0:
    #         all[idx][idx - i]

dfs(0)
print(cnt)
