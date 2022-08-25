# N - Queen pypy 로 통과

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


# # 다른 사람 코드 python 으로 통과 
import sys
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# Passed in pypy3 and python3
def bit_queen(n: int, strt: int = 0, left: int = 0, right: int = 0) -> int:
    bitmap = (1 << n) - 1
    if strt == bitmap:
        return 1

    count = 0
    nxtrt = bitmap & ~(strt | left | right)
    while nxtrt > 0:
        cur = nxtrt & -nxtrt
        count += bit_queen(n, strt | cur, (left | cur) << 1, (right | cur) >> 1)
        nxtrt -= cur

    return count

# @timer
def solve(n: int) -> int:
    return bit_queen(n)

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
