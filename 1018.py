# m 행, n 열
m, n = map(int, input().split())

row = []
min_num = []
for _ in range(m):
    row.append(input())


for a in range(m - 7):
    for i in range(n - 7): # 위의 두 코드는 기준점을 잡는 코드 -> 여기서 왜 -7이지?
        index1 = 0 # 기준이 B일때
        index2 = 0 # 기준이 W일때
        for b in range(a, a + 8): # 탐색 코드
            for j in range(i, i+8):
                if (j +b)%2 == 0:
                    if row[b][j] != 'W': index1 +=1
                    if row[b][j] != 'B': index2 +=1
                else:
                    if row[b][j] != 'B': index1 +=1
                    if row[b][j] != 'W': index2 +=1
        min_num.append(index1)
        min_num.append(index2)

print(min(min_num))
# white - black 이 최대로 겹치는 8 * 8 의 부분을 구해야한다. 
    
# list slicing 을 해야할 것 같다.

# 또는 4개를 한 묶음으로 보고 이 4개의 쌍이 16개 만들어지면 된다. 

# 가운데가 b 인 경우와 white 인 경우를 나누어서 접근하면 좋을 것 같다.