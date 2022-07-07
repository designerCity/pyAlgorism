n = int(input())

count = 0
for i in range(1, n+1):
    # i 가 각 자리 수가 등치수열인지 판별해야한다.
    # map method 를 통해 새로운 list 를 생성
    num_list = list(map(int, str(i)))


    # 두 자리일 경우 모두 등차수열이다. 
    if i < 100:
        count += 1
    # 세 자리일 경우에는 차를 따져줘야 한다.
    # elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
    elif int(num_list[0] + num_list[2]) == int(num_list[1]) * 2:
        count += 1
print(count)


## 두 번째 방법
# n = int(input())

# count = 0
# for i in range(1, n+1):
#     # i 가 각 자리 수가 등치수열인지 판별해야한다.
#     # map method 를 통해 새로운 list 를 생성
#     num_list = list(map(int, str(i)))


#     # 두 자리일 경우 모두 등차수열이다. 
#     if i < 100:
#         count += 1
#     # 세 자리일 경우에는 차를 따져줘야 한다.
#     elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
#         count += 1
# print(count)