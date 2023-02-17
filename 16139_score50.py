import sys
input = sys.stdin.readline
word = str(input())
n = int(input())

li = []
for _ in range(n):
    li.append(list(map(str, input().split())))

for i in range(n):
    start = int(li[i][1])
    end = int(li[i][2]) + 1
    alpha = li[i][0]
    cnt = 0
    for j in range(start, end):
        if alpha == word[j]:
            cnt += 1
    print(cnt)
