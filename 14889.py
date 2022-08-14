N = int(input())
score_li = []
num_li = []
for i in range(N):
    score_li.append(list(map(int, input().split())))
    num_li.append(i)

min = 0
# 모든 경우의 수는 총 N / 2 개로 이루어져 있고, 
def dfs(index, each_total):
    global num_li, min
    min = max(min, each_total)
    

# 능력치의 합을 구하는 코드
print(num_li)
print(score_li)