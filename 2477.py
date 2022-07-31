# 1, 2 반대 방향
# 3, 4 반대 방향

n = int(input()) # 1m^2 에 자라는 참외의 개수
arr =[]
for _ in range(6):
    a, a_idx = map(int, input().split())
    arr.append([a, a_idx])
# 가장 긴 것들의 기준으로 양변을 빼면 된다. 
max_x = 0
x_idx = 0
max_y = 0
y_idx = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_x < arr[i][1]:
            max_x = arr[i][1]
            x_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if max_y < arr[i][1]:
            max_y = arr[i][1]
            y_idx = i
all = max_x * max_y
subW = abs(arr[(x_idx-1)%6][1] - arr[(x_idx+1)%6][1])
subH = abs(arr[(y_idx-1)%6][1] - arr[(y_idx+1)%6][1])
result = (all - (subW * subH)) * n
print(result)