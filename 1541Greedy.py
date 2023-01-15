num = input().split('-')
sum_num = 0
for i in range(1):
    all_num = num[i].split('+')
    for j in all_num:
        sum_num += int(j)



# 빼는 코드
for i in range(1, len(num)):
    all_num = num[i].split('+')
    for j in all_num:
        sum_num-= int(j)
        # print(int(j))

print(sum_num)
