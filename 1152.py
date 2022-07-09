stnce = input()

count = 0
if stnce[0] != ' ':
    count += 1
for i in range(1, len(stnce)):
    # 0 일때는 상관 없음
    # if stnce[0] == ' ':
    #     count += 0
    # else:
    #     count += 1
    if (stnce[i] != ' ') and (stnce[i-1] == ' '):
        count += 1

print(count)