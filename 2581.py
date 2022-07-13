## 내 코드 틀림..

# num1 = int(input())
# num2 = int(input())
# sosu_list = []

# # 범위
# for i in range(num1, num2+1):
#     sosu_list.append(i)
#     if i > 1:        
#         # i 는 두 범위 사이의 수 
#         for j in range(2, i):
#             if i % j == 0: # 소수가 아님
#                 sosu_list.remove(i)
#                 break

# if len(sosu_list) > 0:
#     print(sum(sosu_list))
#     print(min(sosu_list))
# else:
#     print(-1)


start_num = int(input())
last_num = int(input())

sosu_list = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가
            
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)