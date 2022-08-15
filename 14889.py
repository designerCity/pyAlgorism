    
N = int(input())

score_li = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_num = int(1e9)

# # 각 점수를 더하는 함수
# def plusNum(num1, num2):
#     total = score_li[num1][num2]
#     return total

# 모든 경우의 수는 총 N / 2 개로 이루어져 있고, 
def dfs(depth, index):
    global min_num
    if depth == N // 2:
        team1, team2 = 0, 0 # 각 team 의 점수
        # 능력치의 합을 구하는 코드
        for i in range(N): 
            for j in range(N):
                if visited[i] and visited[j]: # T and T -> T
                    team1 += score_li[i][j]
                elif not visited[i] and not visited[j]: # F and F
                    team2 += score_li[i][j]
        min_num = min(min_num, abs(team1-team2))
        return

    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min_num)

    
N = int(input())

score_li = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_num = int(1e9)

# 각 점수를 더하는 함수
def plusNum(num1, num2):
    total = score_li[num1][num2] + score_li[num2][num1]
    return total

# 모든 경우의 수는 총 N / 2 개로 이루어져 있고, 
def dfs(depth, index):
    global min_num
    if depth == N // 2: # 이떄, visited 는 T  N //2 개, F N // 2개로 이루어져 있다.
        team1 = [] # 각 team 의 점수
        team2 = []
        team1_sc = 0
        team2_sc = 0
        # 능력치의 합을 구하는 코드
        for i in range(N):
            if visited[i] == True:
                team1.append[i]
            else:
                team2.append[i]
            print(team1)
        for i in range(N//2):
            for j in range(N//2):
                if visited[i] and visited[j]: # T and T -> T
                    team1 += plusNum(i, j)
                elif not visited[i] and not visited[j]: # F and F
                    team2 += plusNum(i, j)


            # for j in range(N):
            #     if visited[i] and visited[j]: # T and T -> T
            #         team1 += plusNum(i, j)
            #     elif not visited[i] and not visited[j]: # F and F
            #         team2 += plusNum(i, j)
        # min_num = min(min_num, abs(team1-team2))
        return 

    for i in range(index, N):
        
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min_num)

# def dfs(depth, index):
#     global minAns
#     # 백트래킹 답 체크 시점
#     if depth == N // 2:
#         startSum = 0
#         linkSum = 0
#         for i in range(0,N):
#             if i not in team1:
#                 team2.append(i)
#         for i in range(0, N // 2 - 1):
#             for j in range(i+1, N // 2):
#                 startSum += score_li[team1[i]][team1[j]] + score_li[team1[j]][team1[i]]
#                 linkSum += score_li[team2[i]][team2[j]] + score_li[team2[j]][team2[i]]
#         diff = abs(linkSum-startSum)
#         if minAns > diff:
#             minAns = diff
#         # 링크팀을 항상 계산이 끝나면 비워줘야한다.
#         team2.clear()
#         return
#     #dfs 시행
#     for i in range(index, N):
#         if i in team1: continue
#         if len(team1)>0 and team1[len(team1)-1]> i : continue
#         team1.append(i)
#         dfs(depth + 1,index + 1)
#         team1.pop()


# N = int(input())

# score_li = []
# team1 = []
# team2 = []
# for i in range(N):
#     score_li.append(list(map(int, input().split())))

# minAns = float('Inf')
# dfs(0, 0)
# print(minAns)