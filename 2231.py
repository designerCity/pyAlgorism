n = int(input())
result = 0
for i in range(1, n+1):
    s = i
    slc = []
    # 10으로 나눈 수를 나머지로
    while s > 0:
        slc.append(s % 10)
        s -= (s % 10)
        s = s // 10
    
    if (sum(slc) + i) == n:
        result = i
        break

print(result)