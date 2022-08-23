# N - Queen

# N - Queen 문제는 크기가 N * N 인 체스판 위에 퀸 N 개를 서로 공격할 수 없게 놓는 문제이다. 
# N 이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성해라

# Queen 은 같은 index 를 가질 수도, 같은 줄에 있을 수도 없다.
# # 대각선도 안됨.
n = int(input())
# 체스판 한 줄
chess = [0] * n

def is_promising(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
            return False    
    return True

cnt = 0
# # 경우의 수를 탐색
def dfs(depth): # idx 는 각 줄을 의미
    global cnt
    if depth == n: # Queen 이 n개 배치되었을 때, 
        cnt += 1
        return # 함수에서 종료됨

    else:
        for i in range(n): # i 는 row 의 인덱스 을 의미한다.
            chess[depth] = i
            if is_promising(depth):
                dfs(depth + 1)
# dfs 실행            
dfs(0)
# 출력
print(cnt)
